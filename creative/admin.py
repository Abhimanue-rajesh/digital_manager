from django.contrib import admin
from creative.models import Creative


@admin.register(Creative)
class CreativeAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "status",
        "posting_date",
        "stage_1_approval",
        "stage_2_approval",
        "final_approval",
    )
    list_filter = ("status", "stage_1_approval", "stage_2_approval", "final_approval")
    search_fields = ("title", "rejection_reason")
