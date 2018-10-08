from .base import FunctionalTest


class TestDjango(FunctionalTest):

    def test_django_is_installed(self):
        self.browser.get('http://localhost:8000')
        self.assertIn('Django', self.browser.title)
