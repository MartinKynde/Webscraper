import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import time

while True:
    URL = 'https://discimport.com/product/grip-eq-ax5-sand/'


    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    price = soup.find('p', class_ = 'price').text
    price = int(price[13:18].replace('.',''))


    URL2 = 'https://www.gbasesport.dk/grip-eq-ax5-series-backpack-disc-golf-taske.html'

    page = requests.get(URL2)
    soup = BeautifulSoup(page.content, 'html.parser')
    try:
        price2 = soup.find('p', class_ = 'special-price').text
        price2 = int(price.replace('.',''))
    except:
        pass


    URL3 = 'https://discs.dk/products/ax5'
    page = requests.get(URL3)
    soup = BeautifulSoup(page.content, 'html.parser')
    price3 = soup.find('span', class_ = 'product__price').text
    price3 = price3.replace(' ','').replace('.', '').replace('kr','')
    print(price3)
    #except:
     #   pass



    if price < 1600:
        mail_content = '''Hello,
        Prisen på grip tasken er nu nede på {} kr på {}.'''.format(price, URL)
        smt = smtplib.SMTP('smtp.gmail.com',587)
        smt.ehlo()
        smt.starttls()
        smt.login('kyndemartin@gmail.com','usmqnyjdkgmtifbr')
        message = MIMEMultipart()
        message['From'] = 'kyndemartin@gmail.com'
        message['To'] = 'kyndemartin@gmail.com'
        message['Subject'] = 'Taske Pris Notifier'  # The subject line
        message.attach(MIMEText(mail_content, 'plain'))

        session = smtplib.SMTP('smtp.gmail.com', 587)  # use gmail with port
        session.starttls()  # enable security
        session.login('kyndemartin@gmail.com', 'usmqnyjdkgmtifbr')  # login with mail_id and password
        text = message.as_string()
        session.sendmail('kyndemartin@gmail.com', 'kyndemartin@gmail.com', text)
        session.quit()

    if price2 < 1600:
        mail_content = '''Hello,
        Prisen på grip tasken er nu nede på {} kr på {}.'''.format(price2, URL2)
        smt = smtplib.SMTP('smtp.gmail.com',587)
        smt.ehlo()
        smt.starttls()
        smt.login('kyndemartin@gmail.com','usmqnyjdkgmtifbr')
        message = MIMEMultipart()
        message['From'] = 'kyndemartin@gmail.com'
        message['To'] = 'kyndemartin@gmail.com'
        message['Subject'] = 'Taske Pris Notifier'  # The subject line
        message.attach(MIMEText(mail_content, 'plain'))

        session = smtplib.SMTP('smtp.gmail.com', 587)  # use gmail with port
        session.starttls()  # enable security
        session.login('kyndemartin@gmail.com', 'usmqnyjdkgmtifbr')  # login with mail_id and password
        text = message.as_string()
        session.sendmail('kyndemartin@gmail.com', 'kyndemartin@gmail.com', text)
        session.quit()

    if price3 < 1600:
        mail_content = '''Hello,
        Prisen på grip tasken er nu nede på {} kr på {}.'''.format(price3, URL3)
        smt = smtplib.SMTP('smtp.gmail.com',587)
        smt.ehlo()
        smt.starttls()
        smt.login('kyndemartin@gmail.com','usmqnyjdkgmtifbr')
        message = MIMEMultipart()
        message['From'] = 'kyndemartin@gmail.com'
        message['To'] = 'kyndemartin@gmail.com'
        message['Subject'] = 'Taske Pris Notifier'  # The subject line
        message.attach(MIMEText(mail_content, 'plain'))

        session = smtplib.SMTP('smtp.gmail.com', 587)  # use gmail with port
        session.starttls()  # enable security
        session.login('kyndemartin@gmail.com', 'usmqnyjdkgmtifbr')  # login with mail_id and password
        text = message.as_string()
        session.sendmail('kyndemartin@gmail.com', 'kyndemartin@gmail.com', text)
        session.quit()
    time.sleep(24*60*3)
