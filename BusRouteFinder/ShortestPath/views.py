from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from .models import Edge,Station

# Create your views here.
def home (request):
    return render(request, 'home.html') 


def Routes(request):
    startDest=request.GET["From"]
    endDest=request.GET["To"]
    st = Station.objects.all()

    
    return render(request, 'next.html', {'From':startDest, 'To':endDest, 'station': st})
