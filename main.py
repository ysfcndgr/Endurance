#!/usr/bin/env python
# -*- coding: utf-8 -*-
from sherlock import sherlockClass
from whois import whoisClass
from  selenium import webdriver
import sys
try:
    if sys.argv[1] == "--help":
        print("""
    Arayüze hoşgeldin
    Kullanım:
    Birinin kullanıcı adıyla arama yapmak istiyorsan "python main.py --sherlock kullanıcıadı" şeklinde kullanmalısın.
    Whois Bilgisi çekmek istiyorsan "python main.py --whois siteismi" şeklinde aramalısın.
        """)
    elif sys.argv[1]=="--sherlock":
        objeyiuret = sherlockClass()
        objeyiuret.sherlock(sys.argv[2])
    elif sys.argv[1] =="--whois":
        objeyiuret = whoisClass()
        objeyiuret.aranacaksite(sys.argv[2])
    else:
        print("Hatalı giriş")
except IndexError:
    print("Parametreleri bilmiyorsan --help komutunu çalıştırarak öğrenebilirsin")
