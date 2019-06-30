from django.db import models
from django.contrib.auth.models import (
    AbstractUser,
    BaseUserManager,
)

CHARFIELD_MAXLENGTH = 50


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, phone_number, password, **extra_fields):
        if not phone_number:
            raise ValueError("The given phone_number must be set")
        user = self.model(phone_number=phone_number, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, phone_number, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(phone_number, password, **extra_fields)

    def create_superuser(self, phone_number, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(
               "Superuser must have is_staff=True."
               )
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(
               "Superuser must have is_superuser=True."
               )
        return self._create_user(phone_number, password, **extra_fields)


class User(AbstractUser):
    username = None
    # PhoneNumber must be lslike (0)xxxxxxxxxx where 0 is excluded:
    phone_number = models.CharField('Phone Number', max_length=10, unique=True)

    USER_TYPE = (
        ('USR', 'User'),
        ('MEC', 'Mechanic'),
    )
    type = models.IntegerField(verbose_name='User Type', choices=USER_TYPE)
    dateofbirth = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True)
    identificationcode = models.CharField(max_length=10, null=True, blank=True)
    # TelephoneNumber must be like (0)xxxxxxxxxx where 0 is excluded
    telephonenumber = models.CharField(max_length=10, null=True, blank=True)
    email = models.EmailField(max_length=254, null=True, blank=True)
    joinedDate = models.DateTimeField(auto_now=False, auto_now_add=True)
    picture = models.ImageField(upload_to='user-img/', null=True, blank=True)
    vote = models.PositiveSmallIntegerField(null=True, blank=True)
    # Maximum amount of wallet is 10^9 + 3 decimal places
    wallet = models.DecimalField(max_digits=13, decimal_places=3)

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []

    objects = UserManager()


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
