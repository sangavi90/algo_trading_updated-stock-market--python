from django.contrib import admin
from .models import *
# Register your models here.




class CompanyNameAdmin(admin.ModelAdmin):
    list_display = ('company_name',)
    ordering = ('company_name',)

admin.site.register(company_name,CompanyNameAdmin)

class OptionsAdmin(admin.ModelAdmin):
    search_fields=['company_name__company_name']
    ordering = ('company_name__company_name',)

admin.site.register(options, OptionsAdmin)

class ExpiryPriceAdmin(admin.ModelAdmin):
    search_fields=['company_name__company_name']
    ordering = ('company_name__company_name',)

admin.site.register(expirystrikeprice,  ExpiryPriceAdmin)

class strategyadmin(admin.ModelAdmin):
    list_display=('get_user_id','strategy_id','strategy_name')

    def get_user_id(self, obj):
        """
        Custom method to get the user_id of the associated SignInUser.
        """
        if obj.user_id:
            return obj.user_id.user_id  # Assuming user_id is the field representing the user's ID in SignInUser model
        else:
            return None  # Or any other default value you prefer

    get_user_id.short_description = 'User ID'  # Set a short de

admin.site.register( Strategy,strategyadmin)

admin.site.register(Leg)

class signuseradmin(admin.ModelAdmin):
    list_display=('user_id','username')

admin.site.register(SignInUser,signuseradmin)