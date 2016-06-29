#!/usr/bin/env python
# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

caps = DesiredCapabilities.FIREFOX

# Tell the Python bindings to use Marionette.
caps["marionette"] = True

# Path to Firefox DevEdition or Nightly.
caps["binary"] = "/Applications/FirefoxDeveloperEdition.app/Contents/MacOS/firefox-bin"

# Edith heard about an online to-do app, she goes to the site
browser = webdriver.Firefox(capabilities=caps)
browser.get('http://localhost:8000')

# She notices the pages title and header mention to-do lists
assert 'To-Do' in browser.title
