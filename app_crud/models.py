from enum import auto
from functools import update_wrapper
from django.db import models
from django.contrib.auth import get_user_model
import datetime

# Create your models here.

class Crud(models.Model):
    STATUS=(
        ('doing','Doing'),
        ('done','Done')
    )
    nome=models.CharField(max_length=255)
   
    done=models.CharField(
        max_length=5,
        choices=STATUS,
    )
    created_at=models.DateTimeField(default=datetime.datetime.now)
    update_at=models.DateTimeField(default=datetime.datetime.now)
    
    def __str__(self) -> str:
        return self.nome