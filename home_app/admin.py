from django.contrib import admin
from .models import BookTable, Category, MenuItem, MenuItemImage


admin.site.register(BookTable)
admin.site.register(Category)

class MenuItemImageAdmin(admin.StackedInline):
    model = MenuItemImage

class MenuItemAdmin(admin.ModelAdmin):
    list_display = [
        'item_name', 
        'price',
        'slug'
    ]
    inlines = [MenuItemImageAdmin]

admin.site.register(MenuItem, MenuItemAdmin)
admin.site.register(MenuItemImage)