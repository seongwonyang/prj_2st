from django.contrib import admin
from dkea.models import Category
from dkea.models import Product
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display1 = ('c_id', 'c_code', 'c_name', 'i_code', 'i_name')

class CategoryAdmin(admin.ModelAdmin):
    list_display2 = ('p_id', 'c_id', 'p_name', 'img_src', 'price', 'link')

admin.site.register(Category)
admin.site.register(Product)