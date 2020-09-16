# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Lead(models.Model):
    """
    {
    "id": ,                     ---------> integer, primary key, unique, non-null
    "first_name": "",           ---------> string, non-null
    "last_name": "",            ---------> string, non-null
    "mobile": ,                 ---------> string, non-null, length:10, unique
    "email": "",                ---------> string, non-null, unique
    "location_type": ,          ---------> enum ("Country"/"City"/"Zip"), non-null
    "location_string": "",      ---------> string, non-null
    "status": ,                 ---------> enum("Created"/"Contacted"), non-null
    "communication": ""         ---------> string, default: null
}
    """
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100, null=False, blank=True)
    last_name = models.CharField(max_length=100, null=False, blank=True)
    mobile = models.CharField(max_length=10, null=False, unique=True)
    email = models.CharField(max_length=100, null=False, unique=True)
    location_type = models.CharField(max_length=100, null=False, blank=True)
    location_string = models.CharField(max_length=200, null=False, blank=True)
    status = models.CharField(max_length=50, null=False, default='Created')
    communication = models.TextField(default=None, blank=True, null=True)

    # class Meta:
    #     ordering = ['created']