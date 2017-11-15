from django.db import models
from django.utils import timezone
from django.db.models import F


class Wifi(models.Model):

    AUTH_TYPES = ((0, 'other'), (1, 'wap'))

    wifiId = models.CharField(max_length=256, primary_key=True)
    wifiAuthType = models.CharField(max_length=10, choices=AUTH_TYPES, default=AUTH_TYPES[0])
    wifiAverageThroughPutRating = models.FloatField(default=0)
    createdAt = models.DateTimeField(default=timezone.now)

    def add_wifi(self):
        if Wifi.is_wifi_exists(self.wifiId):
            return
        Wifi.save(self)

    @staticmethod
    def update_average_through_put_rating(wifi_id, avg_rating):
        Wifi(wifiId=wifi_id, wifiAverageThroughPutRating=avg_rating).save()

    @staticmethod
    def get_wifi(wifi_id):
        return Wifi.objects.get(wifiId=wifi_id)

    @staticmethod
    def is_wifi_exists(wifi_id):
        try:
            Wifi.objects.get(wifiId=wifi_id)
        except (KeyError, Wifi.DoesNotExist):
            return False
        return True


class Devices(models.Model):
    deviceUdid = models.CharField(max_length=256)
    createdAt = models.DateTimeField(default=timezone.now)

    @staticmethod
    def get_device(device_udid):
        return Devices.objects.get(deviceUdid=device_udid)

    def add_device_to_devices_table(self):
        try:
            Devices.objects.get(deviceUdid=self.deviceUdid)
        except (KeyError, Devices.DoesNotExist):
            Devices.save(self)


class WifiStatusReports(models.Model):
    wifiId = models.ForeignKey(Wifi, on_delete=models.DO_NOTHING)
    deviceId = models.ForeignKey(Devices, on_delete=models.DO_NOTHING, default=0)
    wifiThroughPut = models.FloatField(default=0)

    def add_wifi_status_report(self):
        WifiStatusReports.save(self)


class AggregatedWifiData(models.Model):
    wifiId = models.ForeignKey(Wifi, on_delete=models.DO_NOTHING)
    totalReportersCount = models.IntegerField(default=0)
    totalThroughPutRating = models.FloatField(default=0)
    createdAt = models.DateTimeField(default=timezone.now)

    def aggregate_wifi_data(self, through_put):
        if not AggregatedWifiData.objects.filter(wifiId=self.wifiId):
            AggregatedWifiData.objects.create(wifiId=self.wifiId).save()
        self.update_existing_wifi_details(through_put)

    def update_existing_wifi_details(self, through_put):
        AggregatedWifiData.objects.filter(wifiId=self.wifiId)\
            .update(totalReportersCount=F('totalReportersCount')+1
                    , totalThroughPutRating=F('totalThroughPutRating')+through_put)

    def get_new_throughput_avg(self):
        record = AggregatedWifiData.objects.get(wifiId=self.wifiId)
        return record.totalThroughPutRating / record.totalReportersCount






