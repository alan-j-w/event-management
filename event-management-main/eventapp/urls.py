from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('events/', views.events, name='events'),   # ✅ events listing page
    path('events/<int:event_id>/', views.event_detail, name='event_detail'),  # ✅ event detail page
    path('booking/', views.booking, name='booking'),
    path('contact/', views.contact, name='contact'),
    path('register/signup/', views.signup_view, name='signup'),
]
