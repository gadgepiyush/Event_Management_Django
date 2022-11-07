from django.db import models


# Create your models here.
class Event(models.Model):
    event_options = [
            ("Social Event","Social Event"), 
            ("Concert","Concert"), 
            ("Music Show","Music Show"), 
            ("Movie Show", "Movie Show"),
            ("Charity Event", "Charity Event"),
            ("Comedy Show", "Comedy Show")    
        ]
    
    event_name = models.CharField(max_length = 30)
    city = models.CharField(max_length = 30)
    event_category = models.CharField(max_length=30 ,choices = event_options)
    date = models.DateField()
    time = models.TimeField()
    available_seats  = models.IntegerField()
    ticket_price = models.IntegerField()
    image = models.ImageField(upload_to="event_management/images", default="")



class Ticket(models.Model):
    event_name = models.CharField(max_length = 30)
    city = models.CharField(max_length = 30)
    date = models.DateField()
    time = models.TimeField()
    username = models.CharField(max_length = 30)
    status = models.CharField(max_length = 30)
    event_id = models.ForeignKey(Event, default=None, on_delete=models.CASCADE)











