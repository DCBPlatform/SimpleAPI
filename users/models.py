from __future__ import unicode_literals
import json
import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models

from phonenumber_field.modelfields import PhoneNumberField

class CustomUser(AbstractUser):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, blank=True)
    phone = PhoneNumberField(null=True)
     
    USER_TYPE_OPTION = [
        ('AD','Admin'),
        ('IN','Internal User'),
        ('EX','External User'),
    ]

    user_type = models.CharField(max_length=2,choices=USER_TYPE_OPTION,default='EX')

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name