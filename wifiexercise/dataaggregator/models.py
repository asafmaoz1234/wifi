from django.db import models
from django.utils import timezone


# class ValidateAggregateDataRequestParams(request):
#     pass


class Wifi(models.Model):
    AUTH_TYPES = (('other', 'other'), ('wap', 'wap'))

    wifiId = models.CharField(max_length=256, primary_key=True)
    wifiAuthType = models.CharField(max_length=10, choices=AUTH_TYPES, default=AUTH_TYPES[0])
    wifiAverageThroughPutRating = models.FloatField(default=0)
    createdAt = models.DateTimeField(default=timezone.now)

    def add_wifi(self):
        if Wifi.is_wifi_exists(self.wifiId):
            return
        Wifi.save(self)

    def update_average_through_put_rating(self, wifi_id, avg_rating):
        Wifi(wifiId=wifi_id, wifiAverageThroughPutRating=avg_rating).save()

    def get_wifi_stats(self):
        wifi_data = Wifi.objects.get(wifiId=self.wifiId)
        # response_dict = {'wifiId': wifi_data.}


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

    def add_device_to_devices_table(self):
        # TODO add clean
        try:
            Devices.objects.get(deviceUdid=self.deviceUdid)
        except (KeyError, Devices.DoesNotExist):
            Devices.save(self)


class WifiStatusReports(models.Model):
    wifiId = models.ForeignKey(Wifi, on_delete=models.DO_NOTHING)
    deviceId = models.ForeignKey(Devices, on_delete=models.DO_NOTHING, default=0)
    wifiThroughPut = models.FloatField(default=0)

    def add_wifi_status_report(self):
        pass


class AggregatedWifiData(models.Model):
    wifiId = models.ForeignKey(Wifi, on_delete=models.DO_NOTHING)
    totalReportersCount = models.IntegerField(null=True)
    totalThroughPutRating = models.FloatField()
    createdAt = models.DateTimeField(default=timezone.now)

    def increment_total_report_count(self):
        pass

    def update_total_through_put_rating(self):
        pass

    def get_aggregated_average_through_put_rating(self):
        pass









