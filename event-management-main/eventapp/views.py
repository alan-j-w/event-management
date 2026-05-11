from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Event
from .forms import BookingForm, ContactForm

# --- Unprotected Views (Accessible to all users) ---

def index(request):
    """
    Renders the homepage. This is a public view.
    """
    latest_events = Event.objects.all().order_by('-id')[:3]
    return render(request, 'index.html', {'latest_events': latest_events})

@login_required
def booking(request):
    """
    Handles the booking form. This is a public view, allowing guests to book.
    """
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '✅ Your booking was successful!')
            return redirect('booking')
    else:
        form = BookingForm()
    
    return render(request, 'booking.html', {'form': form})

# --- Protected Views (Only accessible to logged-in users) ---

@login_required
def about(request):
    """
    Renders the 'About Us' page. Requires a logged-in user.
    """
    return render(request, 'about.html')

@login_required
def events(request):
    """
    Displays a list of all events. Requires a logged-in user.
    """
    context = {
        'eve': Event.objects.all()
    }
    return render(request, 'events.html', context)

@login_required
def event_detail(request, event_id):
    """
    Displays the details of a specific event. Requires a logged-in user.
    """
    event = get_object_or_404(Event, id=event_id)
    return render(request, 'event_detail.html', {'event': event})

@login_required
def contact(request):
    """
    Renders the contact page and handles form submission.
    """
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # In a real app, you might send an email or save to DB here
            messages.success(request, "Thank you for your message! We'll get back to you soon.")
            return redirect('contact')
    else:
        form = ContactForm()
    
    return render(request, 'contact.html', {'form': form})


def signup_view(request):
    return render(request, 'reg.html')  # or 'signup.html' if you rename it