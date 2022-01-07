# psychology-today

Basic webscraper to retrieve and parse a query on Psychology Today. Currently running `get-info.py` should give meaningful results with the default parameters (therapists in nyc who accept united healthcare). These parameters can be set at the top of that file. You may need to try running the query on the website to see how your insurance/city is encoded in the url (ex: "New York" becomes "new-york"). The program will also need to open a new browser window as it scans through the search results. Closing this window before completion will cause the program to crash. 

Currently `send-message.py` has a some functions that are non-working attempts at actually messaging the therapists who appear in the query. I tried two things: 

1. Emailing them directly through the email modal. Provider's emails aren't listed directly - you have to go through a modal, and this modal makes you submit a captcha. Idk if it's possible to crack their level of captcha. 
2. Texting them directly. Most providers have a phone number listed and are open to receiving calls/texts. This means we could automate sending out texts, maybe even with the provider's name to make it look like we're DEFINITELY NOT ROBOTS, or pre-record a voice message and use an auto-dialer. I was reading into Google Voice, which didn't seem promising, but I'm sure there are other ways of doing this.
