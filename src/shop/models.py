from django.db import models
CHARFIELD_MAXLENGTH = 50


class Good(models.Model):
    title = models.CharField(max_length=CHARFIELD_MAXLENGTH)
    # Maximum amount of wallet is 10^9 + 3 decimal places
    price = models.DecimalField(max_digits=13, decimal_places=3)
    vote = models.PositiveSmallIntegerField()
    description = models.TextField()
    images = models.ManyToManyField('Image', blank=True)

    def __str__(self):
        return self.title


class Image(models.Model):
    image = models.ImageField(upload_to='static_img/', null=True, blank=True)

    def __str__(self):
        return self.image.url
