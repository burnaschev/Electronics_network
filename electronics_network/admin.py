from django.contrib import admin
from django.utils.html import format_html

from electronics_network.models import Contact, Product, Node


class ContactInline(admin.TabularInline):
    model = Contact


class ProductInline(admin.TabularInline):
    model = Product
    extra = 0


@admin.register(Node)
class NodeAdmin(admin.ModelAdmin):
    inlines = [ContactInline, ProductInline]
    list_display = ("id", "name", "level", "supplier_link", "debt_to_the_supplier")
    list_display_links = ('name', 'supplier_link')

    search_fields = ('name',)
    list_filter = ('contact__city',)

    actions = ('clear_debt',)

    def supplier_link(self, obj):
        if obj.supplier:
            return format_html('<a href="{id}">{name}</a>',
                               id=obj.supplier.id,
                               name=obj.supplier.name
                               )

    supplier_link.short_description = 'Поставщик'

    @admin.action(description='Очистить долг поставщику')
    def clear_debt(self, request, queryset):
        queryset.update(debt_to_the_supplier=0)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'model', 'release_date', 'owner', 'selling_price')
    search_fields = ['name', 'model', 'owner__name']
    list_display_links = ('name', 'owner')
