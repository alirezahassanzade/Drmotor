from django.db import models
from users.models import User
from django.db.models.signals import pre_save
from django.dispatch import receiver
from Drmotori.utils import unique_slug_generator
import logging
from django.core.validators import MinValueValidator
CHARFIELD_MAXLENGTH = 50


logger = logging.getLogger(__name__)


class Product(models.Model):
    title = models.CharField(max_length=CHARFIELD_MAXLENGTH)
    # Maximum amount of wallet is 10^9 + 3 decimal places
    price = models.DecimalField(max_digits=13, decimal_places=3)
    slug = models.SlugField(max_length=50, blank=True, unique=True)
    vote = models.PositiveSmallIntegerField()
    description = models.TextField()
    categories = models.ManyToManyField('Category', blank=True)
    tags = models.ManyToManyField('Tag', blank=True)
    colors = models.ManyToManyField('Color')
    in_stock = models.BooleanField(default=True)
    stock_count = models.IntegerField()
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


@receiver(pre_save, sender=Product)
def product_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


class Comment(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    text = models.TextField(max_length=200)
    commentor = models.ForeignKey('Commentor', on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)
    date_edited = models.DateTimeField(auto_now=True)
    approved = models.BooleanField(default=False)

    def __str__(self):
        name, family = self.commentor.get_info()
        return f'"{name} {family}" on post "{self.product.title}"'


class Commentor(models.Model):
    # if authenticated: store user
    # if not: store name, family, email
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    first_name = models.CharField(max_length=CHARFIELD_MAXLENGTH, blank=True, null=True)
    last_name = models.CharField(max_length=CHARFIELD_MAXLENGTH, blank=True, null=True)
    phone_number = models.CharField(max_length=10, blank=True, null=True)

    def get_info(self):
        if self.user_id:
            # if there is a user, return back the user basic info
            return self.user.first_name, self.user.last_name
        else:
            # if there is no user, return back the basic info
            return self.first_name, self.last_name

    def __str__(self):
        name, family = self.get_info()
        return f"{name} {family}"


class Category(models.Model):
    title = models.CharField(max_length=CHARFIELD_MAXLENGTH)
    parent = models.ForeignKey('self', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Color(models.Model):
    title = models.CharField(max_length=CHARFIELD_MAXLENGTH)

    def __str__(self):
        return self.title


class Tag(models.Model):
    title = models.CharField(max_length=CHARFIELD_MAXLENGTH)
    parent = models.ForeignKey('self', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Image(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='static_img/', null=True, blank=True)

    def __str__(self):
        return self.image.url


# Section Discounts


class Sales(models.Model):
    SALES_TYPE = (
        (10, 'Percent'),
        (20, 'Fixed'),
    )
    title = models.CharField(max_length=CHARFIELD_MAXLENGTH)
    discount_value = models.DecimalField(max_digits=13, decimal_places=3)
    discount_type = models.IntegerField(verbose_name='Sales Type', choices=SALES_TYPE, default=10)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(blank=True, null=True)
    products = models.ManyToManyField(Product)
    catrgories = models.ManyToManyField(Category)


class Voucher(models.Model):
    SALES_TYPE = (
        (10, 'Percent'),
        (20, 'Fixed'),
    )
    # BUG: Add Condition for example (if basket gt 20000)
    code = models.CharField(max_length=CHARFIELD_MAXLENGTH)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=CHARFIELD_MAXLENGTH, blank=True, null=True)
    discount_value = models.DecimalField(max_digits=13, decimal_places=3)
    discount_type = models.IntegerField(verbose_name='Sales Type', choices=SALES_TYPE, default=10)
    usage_limit = models.IntegerField(verbose_name='Maximum number of times that the code can be used.', blank=True, null=True)


# End Discounts


# Section basket

class Basket(models.Model):
    OPEN = 10
    SUBMITTED = 20
    STATUSES = ((OPEN, "Open"), (SUBMITTED, "Submitted"))
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    status = models.IntegerField(choices=STATUSES, default=OPEN)

    def is_empty(self):
        return self.basketline_set.all().count() == 0

    def count(self):
        return sum(i.quantity for i in self.basketline_set.all())

    def create_order(self, billing_address, shipping_address):
        if not self.user:
            raise Exception.BasketException(
                "Cannot create order without user"
            )

        logger.info(
            "Creating order for basket_id=%d"
            ", shipping_address_id=%d, billing_address_id=%d",
            self.id,
            shipping_address.id,
            billing_address.id,
        )

        order_data = {
            "user": self.user,
            "billing_name": billing_address.name,
            "billing_address1": billing_address.address1,
            "billing_address2": billing_address.address2,
            "billing_zip_code": billing_address.zip_code,
            "billing_city": billing_address.city,
            "billing_country": billing_address.country,
            "shipping_name": shipping_address.name,
            "shipping_address1": shipping_address.address1,
            "shipping_address2": shipping_address.address2,
            "shipping_zip_code": shipping_address.zip_code,
            "shipping_city": shipping_address.city,
            "shipping_country": shipping_address.country,
        }
        order = Order.objects.create(**order_data)
        c = 0
        for line in self.basketline_set.all():
            for item in range(line.quantity):
                order_line_data = {
                    "order": order,
                    "product": line.product,
                }
                order_line = OrderLine.objects.create(**order_line_data)
                c += 1

        logger.info(
            "Created order with id=%d and lines_count=%d",
            order.id,
            c,
        )

        self.status = Basket.SUBMITTED
        self.save()
        return order


class BasketLine(models.Model):
    basket = models.ForeignKey(Basket, on_delete=models.CASCADE)
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE
    )
    quantity = models.PositiveIntegerField(
        default=1, validators=[MinValueValidator(1)]
    )

# End basket


# Section Checkout

class Order(models.Model):
    NEW = 10
    PAID = 20
    DONE = 30
    STATUSES = ((NEW, "New"), (PAID, "Paid"), (DONE, "Done"))
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.IntegerField(choices=STATUSES, default=NEW)
    shipping_name = models.CharField(max_length=60)
    shipping_address1 = models.CharField(max_length=60)
    shipping_address2 = models.CharField(
        max_length=60, blank=True
    )
    shipping_zip_code = models.CharField(max_length=12)
    shipping_city = models.CharField(max_length=60)
    shipping_country = models.CharField(max_length=3)
    date_updated = models.DateTimeField(auto_now=True)
    date_added = models.DateTimeField(auto_now_add=True)


class OrderLine(models.Model):
    NEW = 10
    PROCESSING = 20
    SENT = 30
    CANCELLED = 40
    STATUSES = (
        (NEW, "New"),
        (PROCESSING, "Processing"),
        (SENT, "Sent"),
        (CANCELLED, "Cancelled"),
    )
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, related_name="lines"
    )
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    status = models.IntegerField(choices=STATUSES, default=NEW)
