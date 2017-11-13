from django.db import models
from django.utils import timezone


class Wifi(models.Model):
    AUTH_TYPES = (('other', 'other'), ('wap', 'wap'))

    wifiId = models.CharField(max_length=256, primary_key=True)
    wifiAuthType = models.CharField(max_length=10, choices=AUTH_TYPES, default=AUTH_TYPES[0])
    wifiAverageThroughPutRating = models.FloatField(default=0)
    createdAt = models.DateTimeField(default=timezone.now)


class Devices(models.Model):
    deviceUdid = models.CharField(max_length=256)
    createdAt = models.DateTimeField(default=timezone.now)

    def add_device_to_devices_table(self):
        # TODO check empty udid
        if Devices.objects.filter(deviceUdid=self.deviceUdid).exists():
            return
        Devices.save(self)


class UserReports(models.Model):
    wifiId = models.ForeignKey(Wifi, on_delete=models.DO_NOTHING)
    deviceId = models.ForeignKey(Devices, on_delete=models.DO_NOTHING, default=0)
    wifiThroughPut = models.FloatField(default=0)


class AggregatedWifiData(models.Model):
    wifiId = models.ForeignKey(Wifi, on_delete=models.DO_NOTHING)
    totalReportersCount = models.IntegerField(null=True)
    totalThroughPutRating = models.FloatField()
    createdAt = models.DateTimeField(default=timezone.now)









