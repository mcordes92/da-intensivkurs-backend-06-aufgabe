from django.contrib import admin
from .models import Participant,  Booking 

# Register Participant model
@admin.register(Participant)
class ParticipantAdmin(admin.ModelAdmin):
    prepopulated_fields = {"full_name": ["first_name", "last_name"]}

# Register Booking model
@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_filter =["confirmed"]
    readonly_fields = ["booking_date"]