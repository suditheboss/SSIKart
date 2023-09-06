from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# Register your models here.
from accounts.models import Account

class AccountAdmin(UserAdmin):
   list_display = ('id','email', 'first_name', 'last_name', 'username', 'last_login','date_joined', 'is_active')
   list_display_links = ('email','username')
   readonly_fields = ('last_login', 'date_joined')
   ordering = ('date_joined',)

   filter_horizontal = ()
   list_filter = ('date_joined',)
   fieldsets = ()

admin.site.register(Account, AccountAdmin)

