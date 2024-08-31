'''from django.shortcuts import render
from .models import person_collection
from django.http import HttpResponse

# Create your views here.

def add(request):
    records = {
        "name": "john"
    }
    person_collection.insert_one(records)
    return HttpResponse("added")'''