from django.test import TestCase
import requests


class RepairServiceViewsTestClass(TestCase):

    def test_home_page_should_return_200(self):
        url = 'http://localhost:8000/'
        response = requests.get(url)
        self.assertEqual(response.status_code, 200)

    def test_service_list_page_should_return_200(self):
        url = 'http://localhost:8000/services'
        response = requests.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_service_page_should_return_403(self):
        url = 'http://localhost:8000/services/create'
        response = requests.post(url)
        self.assertEqual(response.status_code, 403)
