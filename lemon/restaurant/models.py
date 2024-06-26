from django.db import models

# Create your models here.
class Booking(models.Model):
    Name = models.CharField(max_length=255)
    No_of_guests=models.IntegerField()
    BookingDate=models.DateTimeField()

class Menu(models.Model):
    Title=models.CharField(max_length=255)
    Price = models.DecimalField(max_digits=6,decimal_places=2)
    Inventory=models.IntegerField()