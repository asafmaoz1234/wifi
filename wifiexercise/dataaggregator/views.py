# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from requests import request

appName = 'dataaggregator'


class AggregateData(request):
    template_name = appName+'/aggregatedata.html'

    def get_queryset(self):
        pass



