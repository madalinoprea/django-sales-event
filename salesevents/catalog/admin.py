from django.contrib import admin
from catalog.models import Product, Category, Event

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent', )
    list_filter = ('parent', )

class ProductAdmin(admin.ModelAdmin):
    pass

class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'enabled', 'status_text', 'start_date', 'end_date')
    list_filter = ('enabled', )
    

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Event, EventAdmin)
