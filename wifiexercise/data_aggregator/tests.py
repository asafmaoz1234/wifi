

from django.test import TestCase
from .models import Wifi


# Create your tests here.

class WifiModelTests(TestCase):

    def test_tt(self):
        Wifi.tt()
