from django.urls import path
from projects import views

app_name = 'projects'

urlpatterns = [
    path('',views.ListProjects.as_view(),name='all'),
    path('new/',views.CreateProject.as_view(),name='create'),
    path('projects/in/<slug>/',views.SingleProject.as_view(),name="single"),
    
]