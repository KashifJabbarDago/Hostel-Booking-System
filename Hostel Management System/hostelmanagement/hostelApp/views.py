from django.shortcuts import render
from .models import BookVacancy,RegisterHostel,SignUp,ContactUs
# Create your views here.
from rest_framework.renderers import JSONRenderer
import io
from rest_framework.parsers import JSONParser
from django.http import JsonResponse
import requests
import json
from .serializer import VacancyBookSerializer

def homepage(reqeuest):
    return render(reqeuest,'home.html')


def viewHostel(request):
    return render(request,'viewhostel.html')

def bookVacancy(request):
    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        serializer = VacancyBookSerializer(data=python_data)
        if serializer.is_valid():
            serializer.save()
        
    
    return render(request,'book vacancy.html')

def dumData(data):
    URL = 'http://127.0.0.1:8000/book_vacancy/'
    query = json.dumps(data)
    create = requests.post(url=URL,data=query)
    return create

def registerHostel(request):
    return render(request,'register hostel.html')


def contact(request):
    return render(request,'contact.html')

def FAQ(request):
    return render(request,'faq.html')
