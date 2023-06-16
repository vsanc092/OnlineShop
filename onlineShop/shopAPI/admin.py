from django.contrib import admin
from .models import Comment, Good, Category

admin.site.register(Comment)
# admin.site.register(SubCategory)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(Category, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'available', 'stock']
    list_filter = ['available']
    list_editable = ['price', 'stock', 'available']


admin.site.register(Good, ProductAdmin)
