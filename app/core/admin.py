"""
Django admin customization.
"""
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# whenever your use this translation this will automaticaly translate text (Future Proof, Best Practice)
from django.utils.translation import gettext_lazy as _

# Register your models here.
from core import models

# FOR CHANGE(Edit) to work we need to change the default settins from  django.contrib.auth.admin the USERAdmin Class

class UserAdmin(BaseUserAdmin):
    """Define the admin pages for users."""
    ordering = ['id'] #also because we got rid of username?
    list_display = ['email', 'name', 'bio']
    # (None) = The Title Section like how Personl info is the Title
    # Customiszed fields set and customized field set that we created, and overridde the default one so no missing uername error
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal Info'), {'fields': ('name', 'bio',)}),
        (
            _('Permissions'),
            {
                'fields': (
                    'is_active',
                    'is_staff',
                    'is_superuser',
                )
            }
        ),
        (_('Important dates'), {'fields': ('last_login',)}),
    )
    readonly_fields = ['last_login']

admin.site.register(models.User, UserAdmin) # user UserADmin class instead of Model manager default?