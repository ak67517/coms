from django.shortcuts import render
from django.contrib import messages

# Create your views here.
from django.contrib.auth.mixins import (LoginRequiredMixin,PermissionRequiredMixin)
from django.urls import reverse
from django.views import generic


from projects.models import Project
from projects import models

class CreateProject(LoginRequiredMixin,generic.CreateView):
    fields = ('project_name','project_id','start_date','tasks','description','estimated_required_day')
    model = Project

class SingleProject(generic.DetailView):
    model = Project    

class ListProjects(generic.ListView):
    model = Project