import os
import platform
import sys
import re
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options


def pandA_thread(username, password):
    print ("start")
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--head')

    driver = webdriver.Chrome(options=chrome_options)
    url = 'https://panda.ecs.kyoto-u.ac.jp/portal/login'
    driver.get(url)
    driver.find_element_by_id('username').send_keys(username)
    driver.find_element_by_id('password').send_keys(password)
    driver.find_element_by_name('submit').send_keys(Keys.ENTER)

    while True:
        driver.get(url)
        driver.get(get_subsites(driver)[1][0]) # Go to membership from Home, get list of courses

        href_sites = []
        sites = driver.find_element_by_xpath("/html/body/div[3]/div[9]/div[2]/main/div/div/div/div/form/div").get_attribute("innerHTML")
        sites = BeautifulSoup(sites, "html.parser")
        
        for tr in sites.find_all("tr"):  
            if tr.a:
                 href_sites.append( (tr.a.get('href'), tr.a.getText().strip("\n").strip("\t") ) )
        print(href_sites)
        
        # Go to each courses and check assignments/quizzes
        for site in href_sites:
            print(site[1])
            driver.get(site[0])
            for subsite in get_subsites(driver):
                if subsite[1] == 'Assignments':
                    driver.get(subsite[0])
                    check_assignments()

        time.sleep(3600)

def get_subsites(driver):
    href_subsites = []
    subsites = driver.find_element_by_xpath("/html/body/div[3]/div[9]/div[2]/div").get_attribute("innerHTML")
#     toolSubsitesContainer
    subsites = BeautifulSoup(subsites, "html.parser")
    for li in subsites.find_all("li"):  
        if li.a:
             href_subsites.append( (li.a.get('href'), li.a.getText().strip("\n") ) )
    return href_subsites

def check_assignments():
    print("finshed!!!")
