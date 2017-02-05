from django.conf import settings
from django.test import TestCase
from django.utils.unittest import skipIf

from billing import get_integration


@skipIf(not settings.MERCHANT_SETTINGS.get("ogone_payments", None), "gateway not configured")
class OgonePaymentsTestCase(TestCase):
    def setUp(self):
        self.op = get_integration("ogone_payments")
        self.data = {
            'orderID': 21,
            'ownerstate': '',
            'cn': 'Venkata Ramana',
            'language': 'en_US',
            'ownertown': 'Hyderabad',
            'ownercty': 'IN',
            'exceptionurl': 'http://127.0.0.1:8000/offsite/ogone/failure/',
            'ownerzip': 'Postcode',
            'catalogurl': 'http://127.0.0.1:8000/',
            'currency': 'EUR',
            'amount': '579',
            'declineurl': 'http://127.0.0.1:8000/offsite/ogone/failure/',
            'homeurl': 'http://127.0.0.1:8000/',
            'cancelurl': 'http://127.0.0.1:8000/offsite/ogone/failure/',
            'accepturl': 'http://127.0.0.1:8000/offsite/ogone/success/',
            'owneraddress': 'Near Madapur PS',
            'com': 'Order #21: Venkata Ramana',
            'email': 'ramana@agiliq.com'
        }
        self.op.add_fields(self.data)

    def testFormFields(self):
        self.assertEqual(self.op.fields, {
            'orderID': 21,
            'ownerstate': '',
            'cn': 'Venkata Ramana',
            'language': 'en_US',
            'ownertown': 'Hyderabad',
            'ownercty': 'IN',
            'exceptionurl': 'http://127.0.0.1:8000/offsite/ogone/failure/',
            'ownerzip': 'Postcode',
            'catalogurl': 'http://127.0.0.1:8000/',
            'currency': 'EUR',
            'amount': '579',
            'declineurl': 'http://127.0.0.1:8000/offsite/ogone/failure/',
            'homeurl': 'http://127.0.0.1:8000/',
            'cancelurl': 'http://127.0.0.1:8000/offsite/ogone/failure/',
            'accepturl': 'http://127.0.0.1:8000/offsite/ogone/success/',
            'owneraddress': 'Near Madapur PS',
            'com': 'Order #21: Venkata Ramana',
            'email': 'ramana@agiliq.com'
        })
