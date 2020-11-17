from django.db import models

class ReservationForm(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField(max_length=200)
    phone = models.CharField(max_length=16)
    date_reservation = models.CharField(max_length=10)
    time = models.CharField(max_length=5)
    num_of_people = models.IntegerField(max_length=2)
    message = models.TextField(max_length=600)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.phone