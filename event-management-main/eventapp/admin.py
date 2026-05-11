from django.contrib import admin
from .models import Event,Booking
# Register your models here.
@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'desc_short')
    search_fields = ('name',)

    def desc_short(self, obj):
        return obj.desc[:50] + "..." if len(obj.desc) > 50 else obj.desc
    desc_short.short_description = "Description"

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('cus_name', 'cus_ph', 'event', 'booking_date', 'booked_on')
    list_filter = ('event', 'booking_date')
    search_fields = ('cus_name', 'cus_ph')