

@author: Aditya
"""

import requests
import csv
import json
from bs4 import BeautifulSoup
import urllib.request
import smtplib
import time

url = 'https://www.amazon.de/Sony-DigitalKamera-Touch-Display-Vollformatsensor-Kartenslots/dp/B07B4L1PQ8/ref=sr_1_3?keywords=sony+a7&qid=1561393494&s=gateway&sr=8-3'

h = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'}

def check_price():
    page = requests.get(url, headers=h)
    
    soup = BeautifulSoup(page.text, 'html.parser')
    
    title = soup.find(id='productTitle').text.strip()
    
    price = soup.find(id='priceblock_ourprice').text
    converted_price = float(price[0:5])
    
    if converted_price > 1.700 :
        send_mail()


def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    
    server.login('youremail@gmail.com', 'rpweaxfcvyojpirm')
    
    subject = "Hey ! The price of the product you are looking for fell down!"
    
    body = 'Check the Amazon Link https://www.amazon.de/Sony-DigitalKamera-Touch-Display-Vollformatsensor-Kartenslots/dp/B07B4L1PQ8/ref=sr_1_3?keywords=sony+a7&qid=1561393494&s=gateway&sr=8-3'
    
    msg = f"Subject: {subject}\n\n{body}"
    
    server.sendmail(
            'youremail@gmail.com',
            'youremail@gmail.com',
            msg)
    
    print('Hey email has been sent')
    server.quit()
    

if __name__ == "__main__":
    while(True):
        check_price()
        time.sleep(3600)
    
