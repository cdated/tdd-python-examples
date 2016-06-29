#!/usr/bin/env python
# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

caps = DesiredCapabilities.FIREFOX

# Tell the Python bindings to use Marionette.
# This will not be necessary in the future,
# when Selenium will auto-detect what remote end
# it is talking to.
caps["marionette"] = True

# Path to Firefox DevEdition or Nightly.
# Firefox 47 (stable) is currently not supported,
# and may give you a suboptimal experience.
#
# On Mac OS you must point to the binary executable
# inside the application package, such as
# /Applications/FirefoxNightly.app/Contents/MacOS/firefox-bin
caps["binary"] = "/Applications/Firefox.app/Contents/MacOS/firefox-bin"

browser = webdriver.Firefox(capabilities=caps)
browser.get('http://localhost:8000')

assert 'Django' in browser.title
