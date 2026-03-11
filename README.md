# What is used for

Data collection, discovery


# Installation

1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

2. Make sure you have Firefox installed. With Selenium 4, geckodriver is automatically managed, so you don't necessarily need to manually download it if Selenium Manager handles it, but if you do:
   - Download the geckodriver from https://github.com/mozilla/geckodriver/releases
   - Extract it and add it to your system PATH.

# Usage 

To see available options:
```
python main.py --help
```

Search for a username:
```
python main.py --sherlock <username>
```

Retrieve whois information for a site:
```
python main.py --whois <sitename>
```

# Youtube Video

https://www.youtube.com/watch?v=X9GfMbX2b0I
