import unittest

from morelia import run
from splinter import Browser

from app import app, auth


class StepsMixin:
    def step_authentication_system(self):
        r"authentication system"
        pass

    def step_existing_user_foo_with_password_bar(self, foo, bar):
        r'existing user "([^"]+)" with password "([^"]+)"'
        pass

    def step_I_enter_login_into_the_login_input(self, login):
        r"I enter (.+) into the login input"
        self.step_I_enter_value_into_input(login, "login")

    def step_I_enter_password_into_the_password_input(self, password):
        r"I enter (.+) into the password input"
        self.step_I_enter_value_into_input(password, "password")

    def step_I_should_see_result(self, expected):
        r"I should see (.+)"
        self.step_I_should_see_expected_result(expected)


class BackendAcceptanceTests(StepsMixin, unittest.TestCase):
    def setUp(self):
        app.config["TESTING"] = True
        app.config["DEBUG"] = True
        self.c = app.test_client()

    def test_authentication_feature(self):
        """Authentiaction feature."""
        run("tests/authentiaction.feature", self, verbose=True)

    def step_I_visit_login_page(self):
        r"I visit login page"
        pass

    def step_I_enter_value_into_input(self, value, attr):
        r'I enter "([^"]+)" into the "([^"]+)" input'
        setattr(self, attr, value)

    def step_I_click_submit_button(self):
        r"I click submit button"
        pass

    def step_I_should_see_expected_result(self, expected):
        r'I should see "([^"]+)"'
        result = auth(self.login, self.password)
        expected = True if expected == "Logged in" else False

        self.assertEqual(result, expected)


class FrontendAcceptanceTests(StepsMixin, unittest.TestCase):
    def setUp(self):
        app.config["TESTING"] = True
        app.config["DEBUG"] = True
        self.browser = Browser("flask", app=app)

    def test_authenticaton_feature(self):
        """Authentiaction feature."""
        run("tests/authentiaction.feature", self, verbose=True)

    def step_I_visit_login_page(self):
        r"I visit login page"
        self.browser.visit("/")

    def step_I_enter_value_into_input(self, value, attr):
        r'I enter "([^"]+)" into the "([^"]+)" input'
        self.browser.fill(attr, value)

    def step_I_click_submit_button(self):
        r"I click submit button"
        self.browser.find_by_text("Submit").first.click()

    def step_I_should_see_expected_result(self, expected):
        r'I should see "([^"]+)"'
        self.assertIn(expected, self.browser.html)
