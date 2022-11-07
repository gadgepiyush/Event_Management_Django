from django.shortcuts import render, redirect
from .forms import NewUserForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm 
from django.contrib.auth import login, authenticate, logout
from .models import *
from django.db.models import Q


# Create your views here.
def index(request):
	available = Event.objects.filter(~Q(available_seats = 0)).order_by('-date')
	unavailable = Event.objects.filter(available_seats = 0)
	
	city_set = set()
	for city in available:
		city_set.add(city.city)

	category_set = set()
	for category in available:
		category_set.add(category.event_category)

	context = {
		'available' : available,
		'unavailable' : unavailable,
		'cities' : list(city_set),
		'categories' : list(category_set)
	}

	return render(request=request, template_name='index.html', context=context)



def ticket_booking(request, id):
	#Fetch Product using ID
	event_detail = Event.objects.filter(id=id)
	
	context = {
		'event_detail' : event_detail
	}
	return render(request=request, template_name='ticket_booking.html', context=context)


def filter_event(request):
	context = {}
	available = []
	unavailable =[]

	city_set = set()
	for city in Event.objects.filter(~Q(available_seats = 0)):
		city_set.add(city.city)

	category_set = set()
	for category in Event.objects.filter(~Q(available_seats = 0)):
		category_set.add(category.event_category)

	if request.method == "POST":
		city = request.POST.get('city', '')
		category = request.POST.get('category', '')
		if len(city)>0 and len(category)>0:
			available = Event.objects.filter(~Q(available_seats = 0)).filter(city=city).filter(event_category=category).order_by('-date')
			unavailable = Event.objects.filter(available_seats = 0).filter(city=city).filter(event_category=category).order_by('-date')
		elif len(city)>0:
			available = Event.objects.filter(~Q(available_seats = 0)).filter(city=city).order_by('-date')
			unavailable = Event.objects.filter(available_seats = 0).filter(city=city).order_by('-date')
		elif len(category)>0:
			available = Event.objects.filter(~Q(available_seats = 0)).filter(event_category=category).order_by('-date')
			unavailable = Event.objects.filter(available_seats = 0).filter(event_category=category).order_by('-date')
		else:
			available = Event.objects.filter(~Q(available_seats = 0)).order_by('-date')
			unavailable = Event.objects.filter(available_seats = 0).order_by('-date')
		
	context = {
		'available' : available,
		'unavailable' : unavailable,
		'cities' : list(city_set),
		'categories' : list(category_set)
	}
	
	return render(request=request, template_name='index.html', context=context)


def checkout(request):
	if request.method == "POST":
		username = request.POST.get('username', '')
		event_id = request.POST.get('event_id', '')
		
		event_details = Event.objects.get(pk=event_id) #pk is the primary key
		
		#reducing the available seats by 1
		event_details.available_seats = (event_details.available_seats)-1
		event_details.save()

		new_ticket = Ticket(
			event_name = event_details.event_name,
			city = event_details.city,
			date = event_details.date,
			time = event_details.time,
			username = username,
			status = "Booked",
			event_id = event_details
		)	

		new_ticket.save()
		
		


	return render(request=request, template_name='checkout.html', context={})


def bookings(request):
	user_bookings = Ticket.objects.filter(username=request.user)
	context = {
		'tickets' : user_bookings
	}
	return render(request=request, template_name='bookings.html', context=context)


def cancel_booking(request, id):
	ticket_details = Ticket.objects.get(pk=id)
	ticket_details.status = "Cancelled"
	ticket_details.save()

	print(ticket_details.event_id.available_seats)
	ticket_details.event_id.available_seats = ticket_details.event_id.available_seats +1
	ticket_details.event_id.save()
	print(ticket_details.event_id.available_seats)

	return redirect('bookings')




def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
            
				return redirect("home")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="login.html", context={"login_form":form})



def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("home")

        messages.error( request, "Unsuccessful registration. Invalid information.")

    form = NewUserForm()
    return render(request=request, template_name="register.html", context={"register_form": form})


def log_out(request):
	logout(request)
	return redirect('home')