#!/usr/bin/env python
# -*- coding: utf-8 -*-

from  selenium import webdriver
import time,sys
from selenium.webdriver.firefox.options import Options
from headless import headlessopen

class sherlockClass():
    def sherlock(self,aranacakisi):
        print("[*] 23 platformdan aynı anda veri çekiliyor bu yüzden sherlock yavaş çalışır...")
        print("[*] Tahmini tamamlanma süresi : 2 dakika olarak belirlendi...")
        self.browser_yakala=headlessopen().headlessopenwith()
        #time.sleep(10)
        """
        selenium eski sürümlerinde kod satırı tamamlanmasa bile diğer işlemlere geçiyordu
        bu yüzden kod hata veriyordu ancak yeni sürümünlerinde: Benim kullandığım (3.141.0) böyle bir 
        davranışta bulunmuyor eğer program işlerken hata alıyorsanız time.sleep(10) fonksiyonunu ve
        aşağıdaki time.sleep(5) fonksiyonunu yorum satırından çıkarın.
        """
        self.browser_yakala.get("http://www.usersherlock.com/")
       
        self.veriyial = self.browser_yakala.find_element_by_css_selector('#content > div.search > form > input[type=text]:nth-child(1)')
        self.veriyial.click()
        self.veriyial.send_keys(aranacakisi)
        print("[*] Sabret az kaldı...")
        self.tikla = self.browser_yakala.find_element_by_xpath('//*[@id="content"]/div[2]/form/input[2]')
        self.tikla.click()
        #time.sleep(5)
        self.elements = self.browser_yakala.find_elements_by_css_selector('#results')
        self.liste = list()
        self.ekranayazdir()
        self.ciktilariyazdir()
        self.browser_yakala.quit()    
    def ciktilariyazdir(self):  
        self.yazdirmakistiyormusun = input("Verileri dosyaya yazdırmak istiyor musunuz? E/H ")
        if self.yazdirmakistiyormusun.upper() == "E":
            self.dosya_ismi = input("Dosya ismini girmelisin: ")
            with open("veriler/"+self.dosya_ismi+".txt","w",encoding="UTF-8") as file:
                for bilgi in self.liste:
                    file.write(bilgi)
                    file.write("**************************")
            print("[*] Bilgiler başarıyla yazıldı...")
        elif self.yazdirmakistiyormusun.upper() == "H":
            print("[*] Dosyaya veri yazılmadı programdan çıkılıyor...")
        else:
            print("Yanlış giriş")
    
    def ekranayazdir(self):
        for element in self.elements:
            print("---------------Sonuçlar Aşağıda Listelenecek---------------")
            self.liste.append(element.text)
            print(element.text)
    def __str__(self):
        return self.ekranayazdir()        
    def __len__(self):
        pass
