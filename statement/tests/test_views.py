import os
from random import randint

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from tax.models import FiscalPosition, Activity
from ..forms import AttachmentFormSet, AttachmentFormSetHelper, StatementForm
from ..models import Statement

SCRIPT_DIR = os.path.dirname(__file__)


def preload_dummy_objects():
    """Creates dummy objects so the tests can have some base data to work with."""

    # 5 dummy objects for FiscalPosition, Activity
    for i in range(5):
        FiscalPosition.objects.create(name='Fiscal Position ' + str(i + 1))
        Activity.objects.create(name='Activity ' + str(i + 1))

    # 2 dummy User and 10 Statements for each one with random FiscalPosition and Activity
    for u in range(3):
        get_user_model().objects.create_user(username='Dummy ' + str(u + 1), password='a-dummy-password')

        for i in range(10):
            Statement.objects.create(year=2018,
                                     fiscal_position_id=randint(1, 5),
                                     activity_id=randint(1, 5),
                                     owner_id=u + 1, )


class StatementListTest(TestCase):
    def setUp(self):
        preload_dummy_objects()
        self.user = get_user_model().objects.create_user(username='Ted', password='a-super-secret-password')
        self.client.login(username='Ted', password='a-super-secret-password')

    def test_get(self):
        # 2 more dummy statements for the logged in user
        for i in range(2):
            Statement.objects.create(year=2018,
                                     fiscal_position_id=randint(1, 5),
                                     activity_id=randint(1, 5),
                                     owner=self.user)

        response = self.client.get(reverse('statements:list'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'statement/list.html')
        self.assertEquals(response.context['statements'].count(), 2)


class StatementNewTest(TestCase):
    def setUp(self):
        preload_dummy_objects()
        self.user = get_user_model().objects.create_user(username='Ted', password='a-super-secret-password')
        self.client.login(username='Ted', password='a-super-secret-password')

    def test_get(self):
        response = self.client.get(reverse('statements:new'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'standard_form.html')
        self.assertIsInstance(response.context['form'], StatementForm)
        self.assertIsInstance(response.context['formset'], AttachmentFormSet)
        self.assertIsInstance(response.context['formset_helper'], AttachmentFormSetHelper)

    def test_post(self):
        with open(os.path.join(SCRIPT_DIR, 'attachments/dummy_attachment.txt')) as fp:
            response = self.client.post(reverse('statements:new'), data={'year': 2018,
                                                                         'fiscal_position': ['1'],
                                                                         'activity': ['1'],
                                                                         'attachments-0-DELETE': [''],
                                                                         'attachments-0-attachment': fp,
                                                                         'attachments-0-id': [''],
                                                                         'attachments-0-statement': [''],
                                                                         'attachments-INITIAL_FORMS': ['0'],
                                                                         'attachments-MAX_NUM_FORMS': ['1000'],
                                                                         'attachments-MIN_NUM_FORMS': ['0'],
                                                                         'attachments-TOTAL_FORMS': ['1'],
                                                                         })

        new_statement = Statement.objects.filter(owner=self.user).select_related('fiscal_position', 'activity').last()
        self.assertEquals(new_statement.year, 2018)
        self.assertEquals(new_statement.fiscal_position.name, 'Fiscal Position 1')
        self.assertEquals(new_statement.activity.name, 'Activity 1')

        attachment = new_statement.attachments.all().first()
        self.assertIn('dummy_attachment', attachment.attachment.name)

        self.assertRedirects(response, reverse('statements:detail', kwargs={'pk': new_statement.pk}))


class StatementDetailTest(TestCase):
    def setUp(self):
        preload_dummy_objects()
        self.client.login(username='Dummy 1', password='a-dummy-password')

    def test_url(self):
        other_owner_statement = Statement.objects.filter(owner__username='Dummy 2').first().pk
        response = self.client.get(reverse('statements:detail', kwargs={'pk': other_owner_statement}))
        self.assertEquals(response.status_code, 403)
