#!/usr/bin/env python
# -*- coding: utf-8 -*-
from  selenium import webdriver
import time,sys
from sherlock import*
from headless import headlessopen

class whoisClass(sherlockClass):
    def aranacaksite(self,aranacaksiteyial):
        print("[*] Estimated time 10 seconds")
        self.browser_yakala=headlessopen().headlessopenwith()
        self.browser_yakala.get("https://www.isimtescil.net/Whois")
        self.veriyial = self.browser_yakala.find_element_by_css_selector('#TxtWhois')
        self.veriyial.click()
        self.veriyial.send_keys(aranacaksiteyial)
        self.tikla = self.browser_yakala.find_element_by_xpath('//*[@id="IsimTescilNET-2012"]/div/div[1]/div[2]/div')
        self.tikla.click()
        time.sleep(5)
        self.elements = self.browser_yakala.find_elements_by_css_selector('#WhoQueryreturn')
        self.liste = list()
        self.ekranayazdir()
        self.ciktilariyazdir()
        self.browser_yakala.quit() 

