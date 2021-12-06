from django.db import models
from django.urls import reverse
from django.conf import settings

import misaka

from projects.models import Project
# Create your models here.

from django.contrib.auth import get_user_model
User = get_user_model()

class Report(models.Model):
    report_id = models.CharField(max_length=255,unique=True)
    user = models.ForeignKey(User,related_name='reports',on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    manday = models.CharField(max_length=255,null=True)
    start_date = models.DateField(max_length=255,null=True)
    end_date = models.DateField(max_length=255,null=True)
    message = models.TextField()
    message_html = models.TextField(editable=False)
    project_id = models.ForeignKey(Project,related_name='reports',null=True,blank=True,on_delete=models.CASCADE)

    def __str__(self):
        return self.report_id

    def save(self,*args,**kwargs):
        self.message_html = misaka.html(self.message)
        super().save(*args,**kwargs)

    def get_absolute_url(self):
        return reverse('reports:single',kwargs={'username':self.user.username,
                                              'pk':self.pk})
    class Meta:
        ordering = ['report_id']
