import unittest

from morelia import run
from splinter import Browser

from app import app, auth


class BackendAcceptanceTests(unittest.TestCase):

    def setUp(self):
        app.config["TESTING"] = True
        app.config["DEBUG"] = True
        self.c = app.test_client()

    def test_authentication_feature(self):
        """Authentiaction feature."""
        run("tests/authentiaction.feature", self, verbose=True)

    def step_I_visit_login_page(self):
        r'I visit login page'
        pass

    def step_existing_user_foo_with_password_bar(self, foo, bar):
        r'existing user "([^"]+)" with password "([^"]+)"'
        pass

    def step_I_enter_bar_into_the_password_input(self, value, attr):
        r'I enter "([^"]+)" into the "([^"]+)" input'
        setattr(self, attr, value)

    def step_I_click_submit_button(self):
        r'I click submit button'
        pass

    def step_I_should_see_Logged_in(self, expected):
        r'I should see "([^"]+)"'
        result = auth(self.login, self.password)
        expected = True if expected == "Logged in" else False

        self.assertEqual(result, expected)


class FrontendAcceptanceTests(unittest.TestCase):

    def setUp(self):
        app.config["TESTING"] = True
        app.config["DEBUG"] = True
        self.browser = Browser("flask", app=app)

    def test_authenticaton_feature(self):
        """Authentiaction feature."""
        run("tests/authentiaction.feature", self, verbose=True)

    def step_existing_user_foo_with_password_bar(self, foo, bar):
        r'existing user "([^"]+)" with password "([^"]+)"'
        pass

    def step_I_visit_login_page(self):
        r'I visit login page'
        self.browser.visit("/")

    def step_I_enter_foo_into_the_login_input(self, value, attr):
        r'I enter "([^"]+)" into the "([^"]+)" input'
        self.browser.fill(attr, value)

    def step_I_click_submit_button(self):
        r'I click submit button'
        self.browser.find_by_text("Submit").first.click()

    def step_I_should_see_Logged_in(self, expected):
        r'I should see "([^"]+)"'
        self.assertIn(expected, self.browser.html)
