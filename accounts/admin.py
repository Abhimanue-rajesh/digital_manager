from django.contrib import admin
from accounts.models import User, Notification


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("username", "email", "user_type", "is_staff", "can_approve")
    list_filter = ("user_type", "is_staff", "can_approve")
    search_fields = ("username", "email")


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ("username", "content", "date", "is_read")
    list_filter = ("is_read", "date")
    search_fields = ("content", "username__username")
