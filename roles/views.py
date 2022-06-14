from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.decorators import login_required
from .models import Profile, Role, Group
from genres.models import Genre, Influence

# Create your views here.
@login_required
def index(request):
    people = Profile.objects.all()
    template = loader.get_template('roles/index.html')
    context = {
            'members_list' : people
            }
    return HttpResponse(template.render(context, request))



def role_detail(request, role_id):
    return HttpResponse("Role Detail")

def roles(request):
    response = "All Roles Here"
    return HttpResponse(response)

def people(request):
    people = Profile.objects.all()
    template = loader.get_template('roles/all_people.html')
    context = {
            'all_people' : people
            }
    return HttpResponse(template.render(context, request))

def person_detail(request, person_id):
    person = Profile.objects.get(pk=person_id)
    template = loader.get_template('roles/person_detail.html')
    context = {
            'person' : person
            }
    return HttpResponse(template.render(context, request))

