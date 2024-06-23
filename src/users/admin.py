from django.contrib import admin
from .models import Profile

# name can be chosen, usually model + 'Admin'
class ProfileAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)
    
admin.site.register(Profile, ProfileAdmin)