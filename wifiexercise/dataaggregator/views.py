# Create your views here.
import json
from django.http import HttpResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.db import IntegrityError
from .models import Devices, Wifi, WifiStatusReports, AggregatedWifiData


appName = 'dataaggregator'

@csrf_exempt
def get_wifi_stats(request):
    wifi_id = request.GET.get('wifiId')
    wifi = Wifi.get_wifi(wifi_id)
    # data = {'wifiId': wifi.wifiId, 'avgThroughput': wifi.wifiAverageThroughPutRating, 'authType': wifi.wifiAuthType}
    return HttpResponse({"asdasd": "asdasdas"}, content_type="application/json")


@require_http_methods(["POST"])
@csrf_exempt
def store_device_report(request):
    device_udid = request.POST.get('deviceUdid')
    wifi_id = request.POST.get('wifiId')
    wifi_auth_type = request.POST.get('wifiAuthType')
    wifi_through_put = request.POST.get('throughPut')

    register_device(device_udid)
    register_wifi(wifi_id, wifi_auth_type)

    wifi = Wifi.get_wifi(wifi_id)
    device = Devices.get_device(device_udid)

    add_user_report(wifi, device, wifi_through_put)
    update_aggregated_wifi_data(wifi, wifi_through_put)
    updated_avg = get_wifi_avg_thp(wifi)
    Wifi.update_average_through_put_rating(wifi_id, updated_avg)

    return HttpResponse({'deviceUdid': device_udid, 'wifiId': wifi_id, 'throughPut': wifi_through_put,
                        'updated_avg': updated_avg}, content_type="application/json")


def get_wifi_avg_thp(wifi):
    return AggregatedWifiData(wifiId=wifi).get_new_throughput_avg()


def update_aggregated_wifi_data(wifi, wifi_through_put):
    AggregatedWifiData(wifiId=wifi).aggregate_wifi_data(wifi_through_put)


def add_user_report(wifi, device, through_put):
    try:
        wifi_status_report = WifiStatusReports(wifiId=wifi, deviceId=device,
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







