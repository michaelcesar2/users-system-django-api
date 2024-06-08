from django.contrib import admin
from users.models import CustomUser, Address


admin.site.register(CustomUser)
admin.site.register(Address)
