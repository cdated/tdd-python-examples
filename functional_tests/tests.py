#!/usr/bin/env python
# -*- coding: utf-8 -*-

# built-in
import unittest
import time

# selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

# django
from django.test import LiveServerTestCase

caps = DesiredCapabilities.FIREFOX

# Tell the Python bindings to use Marionette.
caps["marionette"] = True

# Path to Firefox DevEdition or Nightly.
caps["binary"] = "/Applications/FirefoxDeveloperEdition.app/Contents/MacOS/firefox"

class NewVisitorTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox(capabilities=caps)
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        table = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.ID, "id_list_table")))
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Edith heard about an online to-do app, she goes to the site
        self.browser.get(self.live_server_url)

        # She notices the pages title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # She is invited to enter a to-do item straight away
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
                inputbox.get_attribute('placeholder'),
                'Enter a to-do item'
        )

        # She types "Buy peacock feathers" into a text box
        inputbox.send_keys('Buy peacock feathers')

        # When she hits enter, the page updates, and now the page lists
        # "1: Buy peacock feathers" as an item in a to-do list
        inputbox.send_keys(Keys.ENTER)
        # Pause for redirect
        time.sleep(1)


        # There is still a text box invitingher to add another item.
        # She enters "Use peacock feathers to make a fly"
        inputbox2 = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.ID, "id_new_item")))
        inputbox2.send_keys('Use peacock feathers to make a fly')
        inputbox2.send_keys(Keys.ENTER)
        # Pause for redirect
        time.sleep(1)

        self.check_for_row_in_list_table('1: Buy peacock feathers')
        self.check_for_row_in_list_table('2: Use peacock feathers to make a fly')

        self.fail('Finish the test!')

        # The page updates again, and now shows both items on her list

        # Edith wonders whether the site will remember her list.
        # then she sees that the site has generated a unique URL for her
        # there is some explanatory text to that effect

        # She visits that URL - her to-do list is still there.

        # Satisfied, she goes back to sleep

if __name__ == '__main__':
    unittest.main(warnings='ignore')
