# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Wifi
from .models import WifiStatusReports
from .models import Devices
from .models import AggregatedWifiData


admin.site.register(Wifi)
admin.site.register(WifiStatusReports)
admin.site.register(Devices)
admin.site.register(AggregatedWifiData)

