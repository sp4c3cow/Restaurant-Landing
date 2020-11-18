from django.shortcuts import render
from .models import ReservationForm

def index(request):
    return render(request, 'html/index.html')

def reserve_table(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        date_reservation = request.POST['date_reservation']
        time = request.POST['time']
        num_of_people = request.POST['people']
        message = request.POST['message']

        reservation = ReservationForm(name=name, email=email, phone=phone,
                                      date_reservation=date_reservation, time=time,
                                      num_of_people=num_of_people, message=message)
        reservation.save()

        return render(request, 'html/success.html')
    else:
        return render(request, 'html/index.html')

