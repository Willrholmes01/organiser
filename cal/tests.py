from django.test import TestCase
from cal.views import home
from cal.models import Events
from cal.forms import EventForm
from datetime import datetime, date

_date = date.today()
whole_date = "%s/%s/%s" % (
    _date.strftime('%d'), _date.strftime('%m'), _date.strftime('%Y'))

class HomepageTestCase(TestCase):

    def test_home(self):
        response = self.client.get('/cal/')
        self.assertTemplateUsed(response, 'calendar.html')

    def test_home_is_calendar(self):
        response = self.client.get('/cal/')

        month = _date.strftime("%B")
        year = _date.strftime("%Y")

        html = response.content.decode('utf8')
        self.assertIn(month, html)
        self.assertIn(year, html)
        self.assertIn("Create New Event", html)

        # Check all days for given month in calendar
        days = int(_date.strftime("%d"))
        for day in range(1, days):
            self.assertIn(str(day), html)

class EventsTestCase(TestCase):

    def test_for_events(self):
        new_event = Events.objects.create(
            title="Event 1", start_date=_date, description="Testing...")

        self.assertEqual(new_event.title, "Event 1")
        self.assertEqual(new_event.start_date, _date)
        self.assertEqual(new_event.description, "Testing...")

    def test_create_event_page(self):
        response = self.client.get('/cal/newevent/')
        html = response.content.decode('utf8')

        self.assertEqual(response.status_code, 200)
        self.assertIn("Title", html)
        self.assertIn("Start date", html)
        self.assertIn("Private?", html)
        self.assertIn("Submit", html)

    def test_events_show_in_calendar(self):
        new_event = Events.objects.create(
            title="Event 1", start_date=_date, description="Testing...")
        response = self.client.get('/cal/')
        html = response.content.decode('utf8')
        self.assertIn(new_event.title, html)

    def test_event_view(self):
        new_event = Events.objects.create(
            title="Event 1", start_date=_date, description="Testing...")
        response = self.client.get('/cal/events/1/')
        html = response.content.decode('utf8')
        self.assertIn("Event 1", html)
        self.assertIn("Testing...", html)

class calFormTest(TestCase):

    def test_initial_date(self):
        response = self.client.get('/cal/newevent/?')
        html = response.content.decode('utf8')
        self.assertIn(str(whole_date), html)

    def test_edit_form_test(self):
        event = Events.objects.create(
            title="Event 1", start_date=_date, description="Testing...")
        instance = Events.objects.get(id=1)
        form = EventForm(instance=instance)
        self.assertIn("Event 1", form.as_p())
        self.assertIn(str(whole_date), form.as_p())
        self.assertIn("Testing...", form.as_p())

class navigationTestCase(TestCase):

    def test_month(self):
        response = self.client.get('/cal/2/2017?')
        html = response.content.decode('utf8')
        self.assertIn('February 2017', html)
