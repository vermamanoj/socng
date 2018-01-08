from django.test import TestCase
from .models import Customer
import pytest
from django.db.models.query import QuerySet


class CustomerTestCase(TestCase):
    def setUp(self):
        pass

    def test_animals_can_speak(self):
        c = Customer.objects.all()
        self.assertIsInstance(c, QuerySet, "c should be a queryset")
