from django.test import SimpleTestCase
from django.urls import reverse, resolve
from api.views import *


class TestUrls(SimpleTestCase):
    # List views tests
    def test_appointments_list_url_is_resolved(self):
        url = reverse("api:appointments-list")
        self.assertEqual(
            resolve(url).func.__name__,
            AppointmentViewSet.as_view({"get": "list"}).__name__,
        )

    def test_users_list_url_is_resolved(self):
        url = reverse("api:users-list")
        self.assertEqual(
            resolve(url).func.__name__, UserViewSet.as_view({"get": "list"}).__name__
        )

    def test_ads_list_url_is_resolved(self):
        url = reverse("api:ads-list")
        self.assertEqual(
            resolve(url).func.__name__, AdViewSet.as_view({"get": "list"}).__name__
        )

    # Detail views tests
    def test_appointments_detail_url_is_resolved(self):
        url = reverse("api:appointments-detail", args=[1])
        self.assertEqual(
            resolve(url).func.__name__,
            AppointmentViewSet.as_view({"get": "detail"}).__name__,
        )

    def test_users_detail_url_is_resolved(self):
        url = reverse("api:users-detail", args=[1])
        self.assertEqual(
            resolve(url).func.__name__, UserViewSet.as_view({"get": "detail"}).__name__
        )

    def test_ads_detail_url_is_resolved(self):
        url = reverse("api:ads-detail", args=[1])
        self.assertEqual(
            resolve(url).func.__name__, AdViewSet.as_view({"get": "detail"}).__name__
        )
