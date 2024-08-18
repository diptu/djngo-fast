from django.contrib import admin

# Register your models here.
from .models import Emission

admin.site.register(
    Emission,
)
