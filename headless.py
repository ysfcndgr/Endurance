#!/usr/bin/env python
# -*- coding: utf-8 -*-

from  selenium import webdriver
import time,sys
from selenium.webdriver.firefox.options import Options
class HeadlessBrowser():
    def headlessopenwith(self):
        options = Options()
        options.add_argument("--headless")
        self.browser_yakala = webdriver.Firefox(options=options)
        return self.browser_yakala
