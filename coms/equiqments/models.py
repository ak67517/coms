from django.db import models

# Create your models here.

class Equiqment(models.Model):
    equiqment_id = models.CharField(max_length=255,unique=True)
    equiqment_name = models.CharField(max_length=255,unique=True)

    def __str__(self):
        return self.equiqment_id