from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class Event(models.Model):
    img = models.ImageField(upload_to="pic")
    name = models.CharField(max_length=100)
    desc = models.TextField()
    date = models.DateField(null=True, blank=True)
    location = models.CharField(max_length=200, null=True, blank=True)
    
    def __str__(self):
        return self.name

class Booking(models.Model):
    name_validator = RegexValidator(r'^[a-zA-Z\s]*$', 'Only letters and spaces are allowed.')
    phone_validator = RegexValidator(r'^\d{10,15}$', 'Phone number must be between 10 to 15 digits.')

    cus_name = models.CharField(max_length=100, validators=[name_validator], verbose_name="Customer Name")
    cus_ph = models.CharField(max_length=15, validators=[phone_validator], verbose_name="Phone Number")
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="bookings", null=True, blank=True)
    booking_date = models.DateField()
    booked_on = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.cus_name} - {self.event.name if self.event else 'No Event'}"
