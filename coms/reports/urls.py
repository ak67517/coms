from django.urls import path
from reports import views

app_name = 'reports'

urlpatterns = [
    path('',views.ReportList.as_view(),name='all'),
    path('new/',views.CreateReport.as_view(),name='create'),
    path('reports/in/<slug>/',views.ReportDetail.as_view(),name="single"),
]

