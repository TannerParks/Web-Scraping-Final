import requests
from bs4 import BeautifulSoup
from csv import writer
import re


def is_url(address):
    address = address.lower()
    if re.search("http[s]?://", address) is not None:  # If we find http(s):// at the start it is a URL.
        return True
    else:
        return False


def get_url():
    while True:
        address = input("Please enter a PC Part Picker URL here: ")
        if is_url(address):
            return address
            break
        else:
            print("Invalid URL, please try again: ")
            continue


def get_website(url_input):
    website = re.search(r"\w+\.(com|org|net|us)", url_input)
    # Matches a series of alpha-numeric chars followed by . com/org/net/us
    if website is not None:
        return website[0]
    else:
        return "Could not find website"


def get_pcpartpicker_website(input_url):
    matches = re.search(r"mr/\w+/", input_url)
    website = matches[0]
    return website[3:len(website) - 1]

# url = requests.get('https://pcpartpicker.com/product/9nm323/amd-ryzen-5-3600-36-thz-6-core-processor-100-100000031box')


url = get_url()
print(get_website(url))
url = requests.get(url)

soup = BeautifulSoup(url.text, 'html.parser')

Price_Location = soup.findAll(class_='td__finalPrice')

with open('CPU_Scraping_V1', 'w') as csv_file:
    csv_writer = writer(csv_file)
    headers = ['Website', 'Price', 'Store_link']  # availability?
    csv_writer.writerow(headers)

    for element in Price_Location:
        Price = element.find(target='_blank').get_text()
        Store_link = 'https://pcpartpicker.com' + element.find('a')['href']
        Website = get_pcpartpicker_website(Store_link)
        csv_writer.writerow([Website, Price, Store_link])
