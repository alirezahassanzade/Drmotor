from django.db import models

CHARFIELD_MAXLENGTH = 50


# TODO: Multi address on profile
# BUG: Change address from Foreignkey to many to one field
class User(models.Model):
    STATUS_CHOICES = (
        ('A', 'Active'),
        ('D', 'Deactive'),
    )
    TYPE_CHOICES = (
        ('S', 'Staff'),
        ('C', 'Customer'),
        ('M', 'Mechanic'),
    )
    firstname = models.CharField(max_length=CHARFIELD_MAXLENGTH)
    lastname = models.CharField(max_length=CHARFIELD_MAXLENGTH)
    dateofbirth = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True)
    identificationcode = models.CharField(max_length=10, null=True, blank=True)
    # PhoneNumber must be like (0)xxxxxxxxxx where 0 is excluded:
    phonenumber = models.CharField(max_length=10)
    # TelephoneNumber must be like (0)xxxxxxxxxx where 0 is excluded
    telephonenumber = models.CharField(max_length=10, null=True, blank=True)
    email = models.EmailField(max_length=254, null=True, blank=True)
    joinedDate = models.DateTimeField(auto_now=False, auto_now_add=True)
    # TODO: add upload_to argument
    picture = models.ImageField(upload_to='', null=True, blank=True)
    vote = models.PositiveSmallIntegerField(null=True, blank=True)
    # Maximum amount of wallet is 10^9 + 3 decimal places
    wallet = models.DecimalField(max_digits=13, decimal_places=3)
    addresses = models.ManyToManyField('Address', blank=True)
    status = models.CharField(null=True, blank=True, choices=STATUS_CHOICES, max_length=CHARFIELD_MAXLENGTH)
    type = models.CharField(null=True, blank=True, choices=TYPE_CHOICES, max_length=CHARFIELD_MAXLENGTH)
    password = models.CharField(max_length=CHARFIELD_MAXLENGTH)


class Address(models.Model):
    title = models.CharField(max_length=CHARFIELD_MAXLENGTH)
    country = models.CharField(max_length=CHARFIELD_MAXLENGTH)
    city = models.CharField(max_length=CHARFIELD_MAXLENGTH)
    region = models.CharField(max_length=CHARFIELD_MAXLENGTH)
    details = models.CharField(max_length=CHARFIELD_MAXLENGTH)
    # TODO: Check if max length is OK
    postalcode = models.CharField(max_length=10)
    # TODO: Change max length of Latitude & Longitude according to the range
    lat = models.CharField(max_length=CHARFIELD_MAXLENGTH)
    lng = models.CharField(max_length=CHARFIELD_MAXLENGTH)


class Motor(models.Model):
    TYPE_CHOICES = (
        ('A', 'Type A'),
        ('B', 'Type B'),
    )
    title = models.CharField(max_length=CHARFIELD_MAXLENGTH)
    licenseplate = models.CharField(max_length=8)
    type = models.CharField(null=True, blank=True, choices=TYPE_CHOICES, max_length=CHARFIELD_MAXLENGTH)
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
