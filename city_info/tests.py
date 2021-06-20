from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase

from .models import City

class CityModelTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        test_user = get_user_model().objects.create_user(username='tester',password='pass')
        test_user.save()

        test_city = City.objects.create(
            name = 'Amman',
            country = 'Jordan',
            population = 4000000,
            founder = test_user,
        )
        test_city.save()

    def test_city_info(self):
        city = City.objects.get(id=1)

        self.assertEqual(str(city.founder), 'tester')
        self.assertEqual(city.name, 'Amman')
        self.assertEqual(city.population, 4000000)
        self.assertEqual(city.country, 'Jordan')
