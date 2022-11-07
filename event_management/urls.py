from django.contrib import admin
from django.urls import path
from event_management import views
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = "Event Management"
admin.site.site_title = "Event Management Admin"
admin.site.index_title = "Welcome to Event Management"

urlpatterns = [
    path('', views.index, name="home"),
    path('<int:username>', views.index, name='home'),
    path("login", views.login_request, name="login"),
    path("logout", views.log_out, name='logout'),
    path('register', views.register_request, name='register'),
    path('ticketbooking/<int:id>', views.ticket_booking, name='ticketbooking'),
    path('filterevent', views.filter_event, name='filterevent'),
    path('checkout', views.checkout, name="checkout"),
    path('bookings', views.bookings, name='bookings'),
    path('cancelbooking/<int:id>', views.cancel_booking, name='cancelbooking')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)