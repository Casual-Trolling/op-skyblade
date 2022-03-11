# url-scraper

A HTML scraper that is designed to search for a github link in a websites HTML page.
Originaly designed to check suspicious links and to monitor the means of distrobution of malware.
You can run it once or set it up to scrape the html every X ammount of time.
Info on how to install the script and how to run the script can be found below.

**setup**

```txt
pip install requests
cd <project directory>
git clone https://github.com/Casual-Trolling/url-scraper
cd url-scraper
py launcher.py
```

**running**

```txt
[--:--:--]: Enter URL >> [url to search]
[--:--:--]: Loop y/N? >> [do you want to loop. if so, see below]
[--:--:--]: Enter TPM >> [how many times you want to check the url per min]
[--:--:--]: Log  y/N? >> [do you want to log the data]
```


*this file is licensed under the [MIT license](https://mit-license.org/)*
