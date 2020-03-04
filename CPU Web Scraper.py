import requests
from bs4 import BeautifulSoup
from csv import writer

url=input('Enter PC Part Picker URL here: ')
url=requests.get(url)

soup = BeautifulSoup(url.text, 'html.parser')

Price_Location=soup.findAll(class_='td__finalPrice')

with open('CPU_Scraping_V1', 'w') as csv_file:
    csv_writer=writer(csv_file)
    headers=['Price', 'Store_link'] #availability?
    csv_writer.writerow(headers)

    for element in Price_Location:
        Price = element.find(target='_blank').get_text()
        Store_link ='https://pcpartpicker.com' + element.find('a')['href']
        csv_writer.writerow([Price, Store_link])
