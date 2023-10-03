## Prerequisites 
**For installing Requests module**
```sh
 python -m pip install requests
  ```

**For installing BeautifulSoup module**
```sh
pip install bs4
```

**For running the python file**
```sh
python .\script.py 
  ```
### About This Project:
This project aimed to develop a web scraping tool to extract essential product information from Amazon's e-commerce platform. The primary focus is to monitor product prices and availability, but as well it is also extended for other purposes as well. The scraper collects data such as product names, prices, ratings, customer reviews and associated link for a list of specified categories.
<br /><br />
We send an HTTP request to the URL we want (in our case to _amazon site_) dt we created, i.e. tree traversal. For this task, we will be using another third-party python library, **Beautiful Soup**. It is a Python library for pulling data out of HTML and XML files.
 <br /><br />
We also used the library _time_ to get a delay between our next request otherwise amazon coould have blocked our server,also a user agent in attibute because we just can't import the html file from the amazon (ps they dont want automated bot to access there files). <br /><br />
 All data are extracted is in the form of _csv fie_ encodes as _UTF-8_ which could easily viewed in the form of _excel sheet_ and can be used for further data analysis.
 <br /><br />
 Also i have attached _AmazonScrappedData.csv, AmazonWebscarppeddata.xlsx_ if you wanna view how the output look like.
 <br /><br />This project provide  _NAME OF THE PRODUCT , PRICE , RATING , NUMBER OR REVIEWS , LINK_ of the product viewd on that particular site , also it provides result for all the pages.
