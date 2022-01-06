# https://www.linkedin.com/pulse/scraping-therapists-python-selenium-beautifulsoup-scott-edenbaum/


# import libraries
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random
import numpy as np
import lxml
import pandas as pd
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

provider_type = "psychiatrists"
insurance = "unitedhealthcare"
location = "ca/oakland"  # "94619"


def main():
    url = f"https://www.psychologytoday.com/us/{provider_type}/{insurance}/{location}"
    print(url)
    # url = "https://therapists.psychologytoday.com/rms/state/New+Jersey.html"
    scrape_me(url)


def name_from_component(comp):
    try:
        name = (
            comp.contents[3]
            .contents[1]
            .contents[3]
            .contents[1]
            .contents[1]
            .contents[1]
            .contents[1]
            .contents[1]
            .text
        )
        formatted_name = " ".join(name.split())
        return formatted_name
    except:
        return


def phone_number_from_component(comp):
    try:
        return comp.find("div", {"class", "result-phone"}).text.strip()
    except:
        return


def scrape_me(url):  # input parameter = string url to pyschologytoday's website
    # driver = webdriver.Chrome()  # select selenium web driver
    docs = []  # generating empty list
    page = 0
    while True:
        try:
            driver.get(url)  # open the url in selenium
        except:
            print("bad url!")
        soup = BeautifulSoup(
            driver.page_source, "html5lib"
        )  # grab the content with beautifulsoup for parsing
        # print(soup)

        page += 1
        print("\n Page ", page, "\n")
        # print(soup.find("div", {"class": "row results-content"}).contents[1].contents)
        for result in (
            soup.find("div", {"class": "row results-content"}).contents[1].contents
        ):
            if result.name == "div":
                # print(result.name)
                print(phone_number_from_component(result))

        next_button = soup.find("a", {"class", "btn-next"})
        if (
            next_button and next_button.text.strip() == "Next"
        ):  # if a 'next page' exists...
            url = next_button[
                "href"
            ]  # set url = next page url to prepare for next page of scraping
            print(url)
            time.sleep(1)  # added a 1 second sleep to limit bot detection
        else:
            break  # scraping complete!
            print("Scraping Complete!")
    return docs  # returns scrapped data as list of dictionaries


if __name__ == "__main__":
    main()
