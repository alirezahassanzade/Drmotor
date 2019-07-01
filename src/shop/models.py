from django.db import models
from users.models import User
from django.core.validators import MinValueValidator
CHARFIELD_MAXLENGTH = 50


class Product(models.Model):
    title = models.CharField(max_length=CHARFIELD_MAXLENGTH)
    # Maximum amount of wallet is 10^9 + 3 decimal places
    price = models.DecimalField(max_digits=13, decimal_places=3)
    vote = models.PositiveSmallIntegerField()
    description = models.TextField()
    categories = models.ManyToManyField('Category', blank=True)
    tags = models.ManyToManyField('Tag', blank=True)
    colors = models.ManyToManyField('Color')

    def __str__(self):
        return self.title


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
    name = models.CharField(max_length=CHARFIELD_MAXLENGTH, blank=True, null=True)
    family = models.CharField(max_length=CHARFIELD_MAXLENGTH, blank=True, null=True)
    phone_number = models.CharField(max_length=10, blank=True, null=True)

    def get_info(self):
        if self.user_id:
            # if there is a user, return back the user basic info
            return self.user.name, self.user.family
        else:
            # if there is no user, return back the basic info
            return self.name, self.family

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
    end_date = models.DateTimeField()
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
    usage_limit = models.IntegerField(verbose_name='Maximum number of times that the code can be used.')


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


class BasketLine(models.Model):
    basket = models.ForeignKey(Basket, on_delete=models.CASCADE)
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE
    )
    quantity = models.PositiveIntegerField(
        default=1, validators=[MinValueValidator(1)]
    )

# End basket
