from django.contrib import admin

# Register your models here.
from .models import Community, ResidentProfile, SecurityReport, SecurityOfficer

# Register the models in the admin panel
admin.site.register(Community)

admin.site.register(ResidentProfile)

admin.site.register(SecurityReport)

admin.site.register(SecurityOfficer)
