# Create your views here.
import json

from django.http import HttpResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.db import IntegrityError
from .models import Devices, Wifi, WifiStatusReports

appName = 'dataaggregator'


@require_http_methods(["POST"])
@csrf_exempt
def store_device_report(request):

    register_device(request.POST.get('deviceUdid'))
    register_wifi(request.POST.get('wifiId'), request.POST.get('wifiAuthType'))
    add_user_report(request.POST.get('wifiId'), request.POST.get('deviceUdid'), request.POST.get('throughPut'))

    data = json.dumps(['foo', {'bar': ('baz', None, 1.0, 2)}])
    return HttpResponse(json.dumps(data), content_type="application/json")


def add_user_report(wifi_id, device_udid, through_put):
    try:
        wifi_status_report = WifiStatusReports(wifiId=Wifi.get_wifi(wifi_id), deviceId=Devices.get_device(device_udid),
                                               wifiThroughPut=through_put)
        wifi_status_report.add_wifi_status_report()
    except IntegrityError as e:
        return HttpResponseBadRequest(str(e))


def register_wifi(wifi_id, wifi_auth_type):
    try:
        Wifi(wifiId=wifi_id, wifiAuthType=wifi_auth_type).add_wifi()
    except IntegrityError as e:
        return HttpResponseBadRequest(str(e))


def register_device(device_udid):
    try:
        Devices(deviceUdid=device_udid).add_device_to_devices_table()
    except IntegrityError as e:
        return HttpResponseBadRequest(str(e))







