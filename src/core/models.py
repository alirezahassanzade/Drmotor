from django.db import models

CHARFIELD_MAXLENGTH = 50
# TODO: Double check on_delete of all fields

class User(models.Model):
    FirstName = models.CharField(max_length=CHARFIELD_MAXLENGTH)
    LastName = models.CharField(max_length=CHARFIELD_MAXLENGTH)
    DateOfBirth = models.DateField(auto_now=False, auto_now_add=False)
    IdentificationCode = models.CharField(max_length=10)
    # PhoneNumber must be like (0)xxxxxxxxxx where 0 is excluded:
    PhoneNumber = models.CharField(max_length=10)
    # TelephoneNumber must be like (0)xxxxxxxxxx where 0 is excluded
    TelephoneNumber = models.CharField(max_length=10)
    Email = models.EmailField(max_length=254)
    JoinedDate = models.DateTimeField(auto_now=False, auto_now_add=True)
    # TODO: add upload_to argument
    Picture = models.ImageField(upload_to='')
    Vote = models.PositiveSmallIntegerField()
    # Maximum amount of wallet is 10^9 + 3 decimal places
    Wallet = models.DecimalField(max_digits=13, decimal_places=3)
    Status = models.ForeignKey(UserStatus, on_delete=models.CASCADE)
    Address = models.ForeignKey(Address, on_delete=models.CASCADE)
    Type = models.ForeignKey(UserStatus, on_delete=models.CASCADE)


class UserType(models.Model):
    Title = models.CharField(max_length=CHARFIELD_MAXLENGTH)


class UserStatus(models.Model):
    Title = models.CharField(max_length=CHARFIELD_MAXLENGTH)


class Motor(models.Model):
    Title = models.CharField(max_length=CHARFIELD_MAXLENGTH)
    LicensePlate = models.CharField(max_length=8)
    Type = models.ForeignKey(MotorType, on_delete=models.SET_NULL)
    Owner = models.ForeignKey(User, on_delete=models.CASCADE)


class MotorType(models.Model):
    Title = models.CharField(max_length=CHARFIELD_MAXLENGTH)


class Address(models.Model):
    Title = models.CharField(max_length=CHARFIELD_MAXLENGTH)
    Country = models.CharField(max_length=CHARFIELD_MAXLENGTH)
    City = models.CharField(max_length=CHARFIELD_MAXLENGTH)
    Region = models.CharField(max_length=CHARFIELD_MAXLENGTH)
    Details = models.CharField(max_length=CHARFIELD_MAXLENGTH)
    # TODO: Check if max length is OK
    PostalCode = models.CharField(max_length=10)
    # TODO: Change max length of Latitude & Longitude according to the range
    Latitude = models.CharField(max_length=CHARFIELD_MAXLENGTH)
    Longitude = models.CharField(max_length=CHARFIELD_MAXLENGTH)


class Transaction(models.Model):
    # Maximum amount of wallet is 10^9 + 3 decimal places
    Price = models.DecimalField(max_digits=13, decimal_places=3)
    Time = models.DateTimeField(auto_now=False, auto_now_add=True)
    # TODO: Complete other fields
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    Type = models.ForeignKey(TransactionType, on_delete=models.SET_NULL)
    Status = models.ForeignKey(TransactionStatus, on_delete=models.SET_NULL)


class TransactionType(models.Model):
    Title = models.CharField(max_length=CHARFIELD_MAXLENGTH)


class TransactionStatus(models.Model):
    Title = models.CharField(max_length=CHARFIELD_MAXLENGTH)


class Good(models.Model):
    Title = models.CharField(max_length=CHARFIELD_MAXLENGTH)
    # Maximum amount of wallet is 10^9 + 3 decimal places
    Price = models.DecimalField(max_digits=13, decimal_places=3)
    Vote = models.PositiveSmallIntegerField()
    Description = models.TextField()


class RequestGood(models.Model):
    Request = models.ForeignKey(Request, on_delete=models.CASCADE)
    Good = models.ForeignKey(Good, on_delete=models.CASCADE)


class Request(models.Model):
    # StartDate will automatically set when an instance is created
    StartDate = models.DateTimeField(auto_now=False, auto_now_add=True)
    EndDate = models.DateTimeField(auto_now=False, auto_now_add=True)
    Description = models.TextField()
    # Maximum amount of wallet is 10^9 + 3 decimal places
    TotalPrice = models.DecimalField(max_digits=13, decimal_places=3)
    Service = models.ForeignKey(Service, on_delete=models.CASCADE)
    Address = models.ForeignKey(Address, on_delete=models.CASCADE)
    Mechanic = models.ForeignKey(User, on_delete=models.CASCADE)
    Motor = models.ForeignKey(Motor, on_delete=models.CASCADE)


class RequestService(models.Model):
    Request = models.ForeignKey(Request, on_delete=models.CASCADE)
    Service = models.ForeignKey(Service, on_delete=models.CASCADE)


class Service(models.Model):
    Title = models.CharField(max_length=CHARFIELD_MAXLENGTH)
    # Maximum amount of wallet is 10^9 + 3 decimal places
    Price = models.DecimalField(max_digits=13, decimal_places=3)
    # TODO: add field "available on" in order to specify motor type


class System(models.Model):
    Status = models.PositiveSmallIntegerField()
