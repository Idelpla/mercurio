from random import randint

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from tax.models import FiscalPosition, Activity
from ..models import Statement

from django.db.models import Max

from ..forms import AttachmentFormSet, AttachmentFormSetHelper, StatementForm


def preload_dummy_objects():
    """Creates dummy objects so the tests can have some base data to work with."""

    # 5 dummy objects for FiscalPosition, Activity
    for i in range(5):
        FiscalPosition.objects.create(name='Fiscal Position ' + str(i + 1))
        Activity.objects.create(name='Activity' + str(i + 1))

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

    def test_url(self):
        response = self.client.get(reverse('statements:list'))
        self.assertEquals(response.status_code, 200)

    def test_get_queryset(self):
        # 2 more dummy statements for the logged in user
        for i in range(2):
            Statement.objects.create(year=2018,
                                     fiscal_position_id=randint(1, 5),
                                     activity_id=randint(1, 5),
                                     owner=self.user)

        response = self.client.get(reverse('statements:list'))
        self.assertEquals(response.context['statements'].count(), 2)


class StatementNewTest(TestCase):
    def setUp(self):
        preload_dummy_objects()
        self.user = get_user_model().objects.create_user(username='Ted', password='a-super-secret-password')
        self.client.login(username='Ted', password='a-super-secret-password')

    def test_url(self):
        response = self.client.get(reverse('statements:new'))
        self.assertEquals(response.status_code, 200)

    def test_get_context_data(self):
        response = self.client.get(reverse('statements:new'))
        self.assertIsInstance(response.context['formset'], AttachmentFormSet)
        self.assertIsInstance(response.context['formset_helper'], AttachmentFormSetHelper)

    def test_post(self):
        self.fail('Write me')

    def test_form_valid(self):
        response = self.client.post(reverse('statements:new'), data={'year': 2018,
                                                                     'fiscal_position': ['1'],
                                                                     'activity': ['1'], })

        # self.assertIsInstance(response.context['form'], StatementForm)
        self.assertEquals(Statement.objects.filter(owner=self.user).exists(), True)

    def test_get_success_url(self):
        response = self.client.post(reverse('statements:new'), data={'year': 2018,
                                                                     'fiscal_position': ['1'],
                                                                     'activity': ['1'], })

        new_statement_id = Statement.objects.aggregate(id=Max('id'))['id']
        self.assertRedirects(response, reverse('statements:detail', kwargs={'pk': new_statement_id}))


class StatementDetailTest(TestCase):
    def setUp(self):
        preload_dummy_objects()
        self.client.login(username='Dummy 1', password='a-dummy-password')

    def test_url(self):
        response = self.client.get(reverse('statements:detail', kwargs={'pk': 1}))
        self.assertEquals(response.status_code, 200)
