# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import uuid

from django.contrib.gis.db import models
from django.core.validators import MaxValueValidator, MinValueValidator



class CardPayment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email_address = models.CharField(max_length=255, null=True)
    stripe_id = models.CharField(max_length=255, null=True)
    card_id = models.CharField(max_length=255, null=True)
    amount = models.IntegerField(null=True)

    creation_dt = models.DateTimeField(auto_now_add=True,null=False)

    fulfilled = models.BooleanField(default=False)
    block_hash = models.CharField(max_length=255, null=True)
    extrinsic_hash = models.CharField(max_length=255, null=True)

    class Meta:
        ordering = ['-creation_dt']

    def __str__(self):
        return self.creation_dt