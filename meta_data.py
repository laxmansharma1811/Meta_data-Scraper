from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import random

# data moduels
import pandas as pd


meta_attributes = ['name', 'content', 'property']


def return_driver(url):
    driver =  webdriver.Chrome()
    driver.get(url)
    return driver

def get_meta_data(driver):
    metadata = []
    meta_tags = driver.find_elements(By.TAG_NAME, 'meta')

    for meta in meta_tags:
        temp_value = {}
        for att in meta_attributes:
            val = meta.get_attribute(att)
            if val == '':
                val = None
            temp_value[att] = val

        metadata.append(temp_value)

    return metadata

def parser(data):
    df = pd.DataFrame(data)
    df.dropna(axis=0, how='all', inplace=True)
    df.fillna("No Data", inplace=True)
    return df


def parse_url(url):
    url = url.replace("://", "")
    url = url.replace("https", "")
    url = url.replace("http", "")
    url = url.replace("www.", "")
    url = url.replace('.com', '')
    return url


def main(url = "https://techpana.com/"):
    driver = return_driver(url) 
    
    time.sleep(random.randint(2, 5))
    data = get_meta_data(driver)

    df = parser(data)
    file_name = parse_url(url)
    df.to_csv(file_name+ '_metadata.csv', index=False)



main(url='https://fast.com')
