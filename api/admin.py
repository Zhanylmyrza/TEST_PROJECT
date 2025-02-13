from django.contrib import admin
from .models import User, Product, Profile

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "username", "email")
    search_fields = ("username", "email")

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "price", "owner")
    list_filter = ("owner",)

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "bio")
