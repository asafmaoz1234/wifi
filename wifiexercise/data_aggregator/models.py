# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from enum import Enum


class Wifi(models.Model):
    # Distinct
    wifiId = models.CharField(max_length=256)
    # create enum for auth type : http://blog.richard.do/index.php/2014/02/how-to-use-enums-for-django-field-choices/
    wifiAuthType = Enum('wpa', 'public')
    # default ZERO
    wifiAverageThroughPut = models.FloatField()

    def tt(self):
        print self.wifiAuthType[1]


