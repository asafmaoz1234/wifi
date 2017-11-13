import random
import string

from django.test import TestCase

from models import Devices


# Create your tests here.

class DeviceModelTests(TestCase):

    deviceUdid = ''

    def setUp(self):
        self.deviceUdid = ''.join(random.choice(string.lowercase) for x in range(20))

    def test_add_device_to_devices_table_insert_success(self):
        devices = Devices(deviceUdid=self.deviceUdid)
        devices.add_device_to_devices_table()
        self.assertIs(devices.pk, 1)

    def test_add_device_to_devices_table_duplicate_skip_insert(self):
        devices = Devices(deviceUdid=self.deviceUdid)
        devices.add_device_to_devices_table()
        self.assertIs(devices.pk, 1)
        devices.add_device_to_devices_table()
        self.assertIs(devices.pk, 1)




