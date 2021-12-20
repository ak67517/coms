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
    select_related = ('user','project_id')

class ReportDetail(SelectRelatedMixin,generic.DetailView):
    model = models.Report
    select_related = ('user','project_id')

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

