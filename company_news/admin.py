from django.contrib import admin
from .models import CompanyNews


@admin.register(CompanyNews)
class CompanyNewsAdmin(admin.ModelAdmin):
    list_display = ("title_en", "is_published", "created_at")
    list_filter = ("is_published", "created_at")
    search_fields = ("title_en", "title_kh", "title_cn")

    fieldsets = (
        ("English", {
            "fields": ("title_en", "short_en", "content_en")
        }),
        ("Khmer", {
            "fields": ("title_kh", "short_kh", "content_kh")
        }),
        ("Chinese", {
            "fields": ("title_cn", "short_cn", "content_cn")
        }),
        ("Photo / Video", {
            "fields": ("image", "video")
        }),
        ("Publish", {
            "fields": ("is_published",)
        }),
    )