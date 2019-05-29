from django.contrib import admin
from core.models import (
                         Transaction, Request, Service, System
                        )


admin.site.register(Transaction)
admin.site.register(Request)
admin.site.register(Service)
admin.site.register(System)
