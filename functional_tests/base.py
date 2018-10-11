import time

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.urls import reverse
from selenium import webdriver
from selenium.common.exceptions import WebDriverException

MAX_WAIT = 10


def wait(fn):
    def modified_fn(*args, **kwargs):
        start_time = time.time()
        while True:
            try:
                return fn(*args, **kwargs)
            except (AssertionError, WebDriverException) as e:
                if time.time() - start_time > MAX_WAIT:
                    raise e
                time.sleep(0.5)

    return modified_fn


class FunctionalTest(StaticLiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()

    def login(self, username, password, url):
        url = reverse(url)
        self.browser.get(self.live_server_url + url)
        self.wait_for(lambda: self.assertIn('Login', self.browser.find_element_by_tag_name('body').text))

        self.browser.find_element_by_name('username').send_keys(username)
        self.browser.find_element_by_name('password').send_keys(password)
        self.browser.find_element_by_class_name('btn').click()

        self.wait_for(lambda: self.assertIn(url, self.browser.current_url))

    @wait
    def wait_for(self, fn):
        return fn()
