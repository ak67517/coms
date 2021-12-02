from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib import messages

from django.views import generic
from django.http import Http404
from braces.views import SelectRelatedMixin

from reports import models
from reports import forms

from django.contrib.auth import get_user_model
User = get_user_model()

class ReportList(SelectRelatedMixin,generic.ListView):
    model = models.Report
    select_related = ('user','project')

class ReportDetail(SelectRelatedMixin,generic.DetailView):
    model = models.Report
    select_related = ('user','project')

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user__username__iexact=self.kwargs.get('username'))    

class CreateReport(LoginRequiredMixin,SelectRelatedMixin,generic.CreateView):
    fields = ('report_id','project_id','manday','start_date','end_date','message')
    model = models.Report

    def form_valid(self,form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)

class DeleteReport(LoginRequiredMixin,SelectRelatedMixin,generic.DeleteView):
    model = models.Report
    select_related = ('user','project')
    success_url = reverse_lazy('reports:all')

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user_id = self.request.user.id)

    def delete(self,*args,**kwargs):
        messages.success(self.request,'Report Deleted')
        return super().delete(*args,**kwargs)        
 