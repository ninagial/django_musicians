from django.shortcuts import render
from django.http import HttpResponse
from genres.models import Genre

# Create your views here.
def index(request):
    return HttpResponse("Hello world!")

def genre_detail(request, genre_id):
    response = "Genre Detail"
    return HttpResponse(response)

def genres(request):
    response = "All Genres Here"
    return HttpResponse(response)

def influence_detail(request, influence_id):
    response = "Influence Detail"
    return HttpResponse(response)

def influences(request):
    response = "All Influences Here"
    return HttpResponse(response)
