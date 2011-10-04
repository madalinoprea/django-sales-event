"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""
from datetime import datetime, timedelta

from django.test import TestCase
from catalog.models import Event, Category


class SimpleTest(TestCase):

    
    def setUp(self):
        c = Category(name='Test category')
        c.save()

#        self.openEvent

    def test_create_event(self):
        e = Event()
        e.start_date = datetime.now()
        e.end_date = e.start_date + timedelta(days=1)
        e.name = 'Test event'
        e.category = Category.objects.get(name='Test category')
        e.save()

        
