#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

caps = DesiredCapabilities.FIREFOX

# Tell the Python bindings to use Marionette.
caps["marionette"] = True

# Path to Firefox DevEdition or Nightly.
caps["binary"] = "/Applications/FirefoxDeveloperEdition.app/Contents/MacOS/firefox"

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox(capabilities=caps)
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Edith heard about an online to-do app, she goes to the site
        self.browser.get('http://localhost:8000')

        # She notices the pages title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title)

        self.fail('Finish the test!')

        # She is invited to enter a to-do item straight away

        # She types "Buy peacock feathers" into a text box

        # When she hits enter, the page updates, and now the page lists
        # "1: Buy peacock feathers" as an item in a to-do list

        # There is still a text box invitingher to add another item.
        # She enters "Use peacock feathers to make a fly"

        # The page updates again, and now shows both items on her list

        # Edith wonders whether the site will remember her list.
        # then she sees that the site has generated a unique URL for her
        # there is some explanatory text to that effect

        # She visits that URL - her to-do list is still there.

        # Satisfied, she goes back to sleep

if __name__ == '__main__':
    unittest.main(warnings='ignore')
