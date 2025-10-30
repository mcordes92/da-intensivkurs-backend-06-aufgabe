from django.contrib import admin
from .models import  EventCategory , Location , Event

# Register EventCategory model
@admin.register(EventCategory)
class EventCategoryAdmin(admin.ModelAdmin):
    pass

# Register Location model
@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    pass

# Register Event model
@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ["title", "category", "location", "date"]
    search_fields = ["title", "date"]
    list_filter = ["category"]
    date_hierarchy = 'date'

    fieldsets = (
        (
            "Allgemein",
            {
                "fields": ("title", "category", "date"),
            },
        ),
        (
            "Organisation",
            {
                "fields": ("location", "capacity"),
            },
        ),
)
