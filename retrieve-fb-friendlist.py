#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
retrieve via Webdriver + Scraping the Facebook's Friend List and print it in a text file
'''

from selenium import webdriver
import getpass
from time import sleep
from bs4 import BeautifulSoup as bs

friends_url = 'https://www.facebook.com/me/friends'
output_file = 'fb_friends.txt'

b = webdriver.Chrome()
b.get('https://www.facebook.com')
sleep(2)
user_form = b.find_element_by_id('email')
pwd_form = b.find_element_by_id('pass')
login_button = b.find_element_by_id('loginbutton')
username = input('user? ')
user_form.send_keys(username)
pw = getpass.getpass('password? ')
pwd_form.send_keys(pw)
login_button.click()
sleep(2)

b.get(friends_url)
sleep(2)

lastHeight = b.execute_script("return document.body.scrollHeight")
while True:
    b.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    sleep(2)
    newHeight = b.execute_script("return document.body.scrollHeight")
    if newHeight == lastHeight or '<div class="mbm _5vf sectionHeader _4khu">' in b.page_source:
        break
    lastHeight = newHeight

soup = bs(b.page_source, 'html5lib')
b.quit()

with open(output_file, 'w') as f:

    #friends = []
    for friend in soup.find_all('div', {'class':'fsl fwb fcb'}):
        #friends.append(friend.text)
        f.write(friend.text)
