from django.test import TestCase
import requests
from epam.settings import API_KEY


class TestLogic(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.response = requests.get(url=f'https://api.openweathermap.org/data/2.5/weather?APPID={API_KEY}&q=london')

    def test_1_openweather_api_availability(self):
        """
        Test for availability of api.openweathermap.org
        :return: Boolean
        """
        self.assertEqual(self.response.status_code, 200)

    def test_2_openweather_api_check_json(self):
        """
        Test of getting json response with temperature in
        """
        data = self.response.json()
        self.assertIn('main', data)
