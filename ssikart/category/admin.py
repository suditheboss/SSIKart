from django.contrib import admin

# Register your models here.
from .models import category
class CategoryAdmin(admin.ModelAdmin):
     list_display = ('id','name','slug')
     prepopulated_fields = {
         'slug':('name',)
         }

admin.site.register(category,CategoryAdmin)
