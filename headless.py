#!/usr/bin/env python
# -*- coding: utf-8 -*-

from  selenium import webdriver
import time,sys
from selenium.webdriver.firefox.options import Options
class headlessopen():
    def headlessopenwith(self):
        options = Options()
        options.headless = True
        self.browser_yakala = webdriver.Firefox(options=options)
        return self.browser_yakala
