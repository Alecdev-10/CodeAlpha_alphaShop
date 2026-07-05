from django.contrib import admin

from .models import (
    Product,
    Cart,
    CartItem,
    Order,
    OrderItem
)

from django.contrib import admin

admin.site.site_header = "AlphaShop Administration"

admin.site.site_title = "AlphaShop Admin"

admin.site.index_title = "Welcome to AlphaShop Administration"


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "name",
        "price",
        "stock",
        "slug",
        "createdAt"
    )

    list_filter = (
        "createdAt",
    )

    search_fields = (
        "name",
    )

    prepopulated_fields = {
        "slug": ("name",)
    }

    ordering = (
        "-createdAt",
    )


class CartItemInline(admin.TabularInline):

    model = CartItem

    extra = 0


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "user",
        "status",
        "itemCount",
        "total",
        "createdAt"
    )

    list_filter = (
        "status",
        "createdAt"
    )

    search_fields = (
        "user__username",
    )

    inlines = [
        CartItemInline
    ]


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "cart",
        "product",
        "quantity",
        "subtotal"
    )

    search_fields = (
        "product__name",
        "cart__user__username"
    )


class OrderItemInline(admin.TabularInline):

    model = OrderItem

    extra = 0

    readonly_fields = (
        "price",
        "quantity"
    )


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "user",
        "status",
        "total",
        "createdAt"
    )

    list_filter = (
        "status",
        "createdAt"
    )

    search_fields = (
        "user__username",
    )

    inlines = [
        OrderItemInline
    ]


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "order",
        "product",
        "quantity",
        "price",
        "subtotal"
    )

    search_fields = (
        "order__id",
        "product__name"
    )