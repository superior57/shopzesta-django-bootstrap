from django.contrib import admin
from .models import Category, PropertyProductImage, Product, PropertyProductBlog

class CategoryAdmin(admin.ModelAdmin):
  list_display = ['id', 'name']
  search_fields = ['name']
  ordering = ('id', 'name')

class PropertyProductImageInline(admin.TabularInline):
  model = PropertyProductImage
  extra = 3
class PropertyProductBlogInline(admin.TabularInline):
  model = PropertyProductBlog
  extra = 2

class ProductAdmin(admin.ModelAdmin):
  list_display = ['id', 'title']
  inlines = [ PropertyProductImageInline, PropertyProductBlogInline ]


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)