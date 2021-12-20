from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from django.conf import settings
# Create your models here.

import misaka

from django.contrib.auth import get_user_model
User = get_user_model()

from django import template
register = template.Library()

class Project(models.Model):
    project_name = models.CharField(max_length=255,unique=True)
    project_id = models.CharField(max_length=255,unique=True)
    tasks = models.TextField(max_length=255,null=True)
    slug = models.SlugField(allow_unicode=True,unique=True)
    description = models.TextField(blank=True,default='')
    description_html = models.TextField(editable=False,default='',blank=True)
    start_date = models.DateField(max_length=255,null=True)
    estimated_required_day = models.CharField(max_length=255,null=True)


    def __str__(self):
        return self.project_id

    def save(self,*args,**kwargs):
        self.slug = slugify(self.project_name)
        self.description_html = misaka.html(self.description)
        super().save(*args,**kwargs)

    def get_absolute_url(self):
        return reverse('projects:single',kwargs={'slug':self.slug})

    class Meta:
        ordering = ['project_id']
