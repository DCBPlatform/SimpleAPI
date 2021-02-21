# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import uuid

from django.contrib.gis.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from phonenumber_field.modelfields import PhoneNumberField



class Wallet(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, null=True)
    wallet_address = models.CharField(max_length=255, null=True, unique=True)
    owner_name = models.CharField(max_length=511, null=True)
    owner_nickname = models.CharField(max_length=511, null=True)
    verified = models.BooleanField(default=False)
    kyc_level = models.IntegerField(default=0)
    phone = PhoneNumberField(null=True)
    nric = models.IntegerField(null=True)
    passport = models.CharField(max_length=255, null=True)

    creation_dt = models.DateTimeField(auto_now_add=True,null=False)
    verification_dt = models.DateTimeField(null=True)

    class Meta:
        ordering = ['-creation_dt']

    def __str__(self):
        return self.name

class Evidence(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, null=True)    

    creation_dt = models.DateTimeField(auto_now_add=True,null=False)

    class Meta:
        ordering = ['-creation_dt']

    def __str__(self):
        return self.name        


    # STATUS = [
    #     ('CM', 'Completed'),
    #     ('CR', 'Created'),
    #     ('IE', 'In Evaluation'),
    #     ('IP', 'In Progress'),
    #     ('NA', 'Not Available'),
    #     ('PD', 'Paid'),
    #     ('RJ', 'Rejected'),
    #     ('SM', 'Submitted')
    # ]

    # status = models.CharField(max_length=2, choices=STATUS, default='CR')
    # applied_house = models.ForeignKey(House, on_delete=models.CASCADE, null=True, related_name='applied_house_id')        

    # applicant = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, related_name='application_applicant')
    # evaluator_nominated = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, related_name='application_evaluator_nominated')
    # registration_datetime = models.DatetimeField(null=True)