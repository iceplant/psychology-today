# psychology-today

Basic webscraper to retrieve and parse a query on Psychology Today. Currently running `get-info.py` should give meaningful results with the default parameters (therapists in nyc who accept united healthcare). These parameters can be set at the top of that file. You may need to try running the query on the website to see how your insurance/city is encoded in the url (ex: "New York" becomes "new-york"). The program will also need to open a new browser window as it scans through the search results. Closing this window before completion will cause the program to crash. 
