import requests
from bs4 import BeautifulSoup
import json

def scrape_bikes(url,l1):
    response = requests.get(url)
    if response.status_code !=200 :
        print("Scrapping Failed....")
        return
    soup = BeautifulSoup(response.text,"html.parser")
    bikes = soup.find_all("div", class_="p-3 md:py-6 md:px-4")
    for bike in bikes:
        bike_full_name = bike.find("h4",class_="text-gray-800 text-lg font-medium md:text-xl").text
        bike_model_year = bike_full_name[:4]
        bike_name = bike_full_name[4:]
        bike_price_text = bike.find("p",class_="text-xl font-medium my-2 md:mt-2 md:mb-4 md:text-2xl").text
        bike_price = float(bike_price_text[4:].replace(",",""))
        currency = bike_price_text[:4]
        bike_type =bike.find("li",class_="text-sm text-gray-600").text
        bike_cc_container= bike.find_all("ul",class_="list-disc list-inside")
        bike_power_cc=""
        bike_power_watt=""
        for bike in bike_cc_container:
                bike_cc =bike.find_next('li',class_="text-sm text-gray-600").text
                if "watt" in bike_cc:
                      bike_power_watt = bike_cc.strip().strip("watt")
                elif "cc" in bike_cc:
                      bike_power_cc = bike_cc.strip().strip("cc")

        


              
              
        print(bike_name,"|",currency,"|",bike_price,"|",bike_model_year,"|",bike_type,"|",bike_power_cc,"|",bike_power_watt)
        dict = {
                "Bike Name": bike_name,
                "Bike Year" : bike_model_year,
                "Bike Price":bike_price,
                "Bike Currency" : currency,
                "Bike Power CC":bike_power_cc,
                "Bike Power Watt":bike_power_watt,
                "Type Of Bike":bike_type
                    }
        
        l1.append(dict)
    return l1
l1 = [] #global variable
for i in range(1, 85):
    URL = f"https://www.bikebazarnepal.com/bikes?page={i}&sortBy=price"
    scrape_bikes(URL,l1)
    with open("bikes.json", "w") as f:
                json.dump(l1, f, indent=4)
    
print(f"{len(l1)} bikes were scraped")



