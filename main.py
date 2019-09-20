#!/usr/bin/env python
# -*- coding: utf-8 -*-
from sherlock import sherlockClass
from whois import whoisClass
from  selenium import webdriver
import sys
try:
    if sys.argv[1] == "--help":
        print("""
    Welcome to interface
    How to use:
    If you want to search someone's username, you have to type and search 'python main.py --sherlock username'
    If you want to retrieve whois info you have to type and search 'python main.py  --whois sitename'
        """)
    elif sys.argv[1]=="--sherlock":
        objeyiuret = sherlockClass()
        objeyiuret.sherlock(sys.argv[2])
    elif sys.argv[1] =="--whois":
        objeyiuret = whoisClass()
        objeyiuret.aranacaksite(sys.argv[2])
    else:
        print("Incorrect entry")
except IndexError:
    print("If you do not know the parameter you can use --help command and find out")
