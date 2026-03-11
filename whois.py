#!/usr/bin/env python
# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
import time,sys
from sherlock import*
from headless import HeadlessBrowser

class Whois(Sherlock):
    def aranacaksite(self,aranacaksiteyial):
        print("[*] Estimated time 10 seconds")
        self.browser_yakala=HeadlessBrowser().headlessopenwith()
        try:
            self.browser_yakala.get("https://www.isimtescil.net/Whois")
            self.veriyial = self.browser_yakala.find_element(By.CSS_SELECTOR, '#TxtWhois')
            self.veriyial.click()
            self.veriyial.send_keys(aranacaksiteyial)
            self.tikla = self.browser_yakala.find_element(By.XPATH, '//*[@id="IsimTescilNET-2012"]/div/div[1]/div[2]/div')
            self.tikla.click()
            time.sleep(5)
            self.elements = self.browser_yakala.find_elements(By.CSS_SELECTOR, '#WhoQueryreturn')
            self.liste = list()
            self.ekranayazdir()
            self.ciktilariyazdir()
        finally:
            self.browser_yakala.quit()

