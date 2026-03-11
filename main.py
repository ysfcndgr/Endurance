#!/usr/bin/env python
# -*- coding: utf-8 -*-
import argparse
from sherlock import Sherlock
from whois import Whois

def main():
    parser = argparse.ArgumentParser(description="Welcome to interface. Search for username or whois info.")
    parser.add_argument("--sherlock", help="Search someone's username (e.g., 'python main.py --sherlock username')")
    parser.add_argument("--whois", help="Retrieve whois info for a site (e.g., 'python main.py --whois sitename')")

    args = parser.parse_args()

    if args.sherlock:
        objeyiuret = Sherlock()
        objeyiuret.sherlock(args.sherlock)
    elif args.whois:
        objeyiuret = Whois()
        objeyiuret.aranacaksite(args.whois)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
