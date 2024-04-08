from django.contrib.auth.models import User
from django.test import TestCase

# Write your tests here
from django.test import TestCase
from django.urls import reverse
from .models import ServiceRequest


class ServiceRequestTestCase(TestCase):
    def setUp(self):
        # Create test data
        self.user = User.objects.create_user(username='tester', password='password123')
        self.request = ServiceRequest.objects.create(customer=self.user, request_type='Test Request',
                                                     details='This is a test request')

    def test_service_request_created(self):
        # Test if a service request was created successfully
        self.assertEqual(ServiceRequest.objects.count(), 1)

    def test_submit_service_request_view(self):
        # Test submit service request view
        url = reverse('submit_service_request')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_request_tracking_view(self):
        # Test request tracking view
        url = reverse('request_tracking')
        self.client.force_login(self.user)  # Log in user for this test
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
