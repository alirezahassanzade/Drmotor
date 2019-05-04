from django.contrib import admin
from core.models import (UserStatus, Address, UserType, User, MotorType, Motor,
                        TransactionType, TransactionStatus, Transaction, Good,
                        Request, Service, System, Image
                        )

admin.site.register(UserStatus)
admin.site.register(Address)
admin.site.register(UserType)
admin.site.register(User)
admin.site.register(MotorType)
admin.site.register(Motor)
admin.site.register(TransactionType)
admin.site.register(TransactionStatus)
admin.site.register(Transaction)
admin.site.register(Good)
admin.site.register(Request)
admin.site.register(Service)
admin.site.register(System)
admin.site.register(Image)
