from django.contrib import admin
from .models import User, Device, Record

admin.site.register(User)
admin.site.register(Device)
admin.site.register(Record)