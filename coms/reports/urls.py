from django.urls import path
from reports import views

app_name = 'reports'

urlpatterns = [
    path('',views.ReportList.as_view(),name='all'),
    path('new/',views.CreateReport.as_view(),name='create'),
    path('by/<username>/<int:pk>/',views.ReportDetail.as_view(),name="single"),
    path("delete/<int:pk>/",views.DeleteReport.as_view(),name="delete")
]
