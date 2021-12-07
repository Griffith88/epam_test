from unittest.mock import patch
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class EpamApiTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user('test', password="P@ssw0rd!")

    def test_1_not_auth(self):
        """
        Test for not authenticated  users. Test will return 302 status code if everything is ok!
        :return: boolean
        """

        response = self.client.get(path=reverse('weather'), data={'city': 'london'})
        self.assertEqual(response.status_code, status.HTTP_302_FOUND)

    def test_2_working(self):
        """
        Test for authenticated users. In a good case test will return status 200 OK and json data
        :return: boolean & boolean
        """

        login = self.client.login(username=self.user.username, password="P@ssw0rd!")
        self.assertTrue(login)

        with patch('app_weather.business_logic.weather_get.Weather.to_dict') as to_dict:
            to_dict.return_value = {"temperature": -3.211233, "city": "london"}
            response = self.client.get(path=reverse('weather'), data={'city': 'london'})
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.assertEqual(response.content.decode(), '{"temperature": -3.211233, "city": "london"}')
