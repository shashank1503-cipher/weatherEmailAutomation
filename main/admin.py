from django.contrib import admin

# Registering ClientDetails Model to Admin Site
from .models import ClientDetails
admin.site.register(ClientDetails)