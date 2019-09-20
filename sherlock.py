#!/usr/bin/env python
# -*- coding: utf-8 -*-

from  selenium import webdriver
import time,sys
from selenium.webdriver.firefox.options import Options
from headless import headlessopen

class sherlockClass():
    def sherlock(self,aranacakisi):
        print("[*] Sherlock retrieving data from 23 different platform that's why it may work slowly...")
        print("[*] Estimated completion time: Set to 2 minutes...")
        self.browser_yakala=headlessopen().headlessopenwith()
        #time.sleep(10)
        """
        In the old version of Selenium even if line of code does not complete, it pass the next process.
        Therefore the code was giving an error but in the new version:
        The version that i am using (3.141.0) you will not face with those kind of errors.
        If you receive any error while program is working;
        You need to remove time.sleep(10) and time.sleep(5) function from comment line.
        """
        self.browser_yakala.get("http://www.usersherlock.com/")
       
        self.veriyial = self.browser_yakala.find_element_by_css_selector('#content > div.search > form > input[type=text]:nth-child(1)')
        self.veriyial.click()
        self.veriyial.send_keys(aranacakisi)
        print("[*] Almost done...")
        self.tikla = self.browser_yakala.find_element_by_xpath('//*[@id="content"]/div[2]/form/input[2]')
        self.tikla.click()
        #time.sleep(5)
        self.elements = self.browser_yakala.find_elements_by_css_selector('#results')
        self.liste = list()
        self.ekranayazdir()
        self.ciktilariyazdir()
        self.browser_yakala.quit()    
    def ciktilariyazdir(self):  
        self.yazdirmakistiyormusun = input("Do you want to print the data to the file Y/N ? ")
        if self.yazdirmakistiyormusun.upper() == "Y":
            self.dosya_ismi = input("You have to enter the file name: ")
            with open("data/"+self.dosya_ismi+".txt","w",encoding="UTF-8") as file:
                for bilgi in self.liste:
                    file.write(bilgi)
                    file.write("**************************")
            print("[*] Information successfully written...")
        elif self.yazdirmakistiyormusun.upper() == "N":
            print("[*] Data not written to the file...Exiting the program...")
        else:
            print("incorrect entry")
    
    def ekranayazdir(self):
        for element in self.elements:
            print("---------------The results will be listed below---------------")
            self.liste.append(element.text)
            print(element.text)
    def __str__(self):
        return self.ekranayazdir()        
    def __len__(self):
        pass
