from django.contrib import admin

# Register your models here.
from .models import donor
from .models import receiver
from .models import stocks

admin.site.register(donor)
admin.site.register(receiver)
admin.site.register(stocks)