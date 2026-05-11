from django import forms
from . models import Booking
class DateInput(forms.DateInput):
    input_type='date'


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['cus_name', 'cus_ph', 'event', 'booking_date']

        widgets = {
            'cus_name': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Enter your name',
                'pattern': '^[a-zA-Z\s]*$',
                'title': 'Only letters and spaces are allowed.'
            }),
            'cus_ph': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Enter your phone number',
                'pattern': '^\d{10,15}$',
                'title': 'Please enter 10 to 15 digits.'
            }),
            'event': forms.Select(attrs={'class': 'form-control'}),
            'booking_date': DateInput(attrs={'class': 'form-control'}),
        }

        labels = {
            'cus_name': "Customer Name",
            'cus_ph': "Phone Number",
            'event': "Select Event",
            'booking_date': "Booking Date",
        }

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'class': 'form-control', 
        'placeholder': 'Your Name',
        'pattern': '^[a-zA-Z\s]*$',
        'title': 'Only letters and spaces are allowed.'
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Your Email'}))
    subject = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Subject'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Your Message', 'rows': 5}))