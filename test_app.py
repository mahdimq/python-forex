from unittest import TestCase
from flask import Flask, render_template, request, redirect
from app import app

# Make Flask errors be real errors, not HTML pages with error info
app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar']


class CurrencyTest(TestCase):
    def setUp(self):
        """Stuff to do before every test"""
        app.config['TESTING'] = True

    def tearDown(self):
        """Stuff to do after every test"""

    def test_homepage(self):
        """Test homepage template and status code of 200"""
        with app.test_client() as client:
            res = client.get("/")
            """extract html from route"""
            html = res.get_data(as_text=True)
            """test html from test to page"""
            self.assertEqual(res.status_code, 200)
            self.assertIn('<p class="title">Forex Python</p>', html)
            self.assertIn(
                '<label class="label" for="from">Converting From</label>', html)
            self.assertIn(
                '<label class="label" for="to">Converting To</label>', html)
            self.assertIn(
                '<label class="label" for="amount">Amount</label>', html)

    def test_currency_pass(self):
        """Test Currency conversion route and status code of 200"""
        with app.test_client() as client:
            """confirming pass if US$ 1.0 == US$ 1.0"""
            res = client.get("/currency?from=USD&to=USD&amount=1")
            """extract html from route"""
            html = res.get_data(as_text=True)
            """test html from test to page"""
            self.assertEqual(res.status_code, 200)
            self.assertIn(
                '<p class="is-medium mb-2">Converting From: <strong>USD (United States dollar)</strong></p>', html)
            self.assertIn(
                '<p class="is-medium mb-2">Amount to Change: <strong>1.0</strong></p>', html)
            self.assertIn(
                '<p class="is-medium mb-2">Amount to Receive: <strong>US$ 1.0</strong></p>', html)

    def test_currency_redirect(self):
        """Test redirect and failed route and status code of 302"""
        with app.test_client() as client:
            """test wrong codes and get error then redirect"""
            res = client.get("/currency?from=XYZ&to=ABC&amount=1")
            self.assertEqual(res.status_code, 302)
            self.assertEqual(res.location, 'http://localhost/')

    def test_currency_fail(self):
        """Test Currency conversion failed route and follow redirects"""
        with app.test_client() as client:
            """after error, we follow the redirect route to index page"""
            res = client.get(
                "/currency?from=XYZ&to=ABC&amount=1", follow_redirects=True)
            """extract html from route and status code of 200"""
            html = res.get_data(as_text=True)
            self.assertEqual(res.status_code, 200)
            """confirm html from route to homepage html"""
            self.assertIn('<p class="title">Forex Python</p>', html)
            self.assertIn(
                '<label class="label" for="from">Converting From</label>', html)
            self.assertIn(
                '<label class="label" for="amount">Amount</label>', html)
