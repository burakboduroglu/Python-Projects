import requests
from bs4 import BeautifulSoup

try:
    url = requests.get("https://www.worldometers.info/coronavirus/")
    soup = BeautifulSoup(url.content,"html.parser")

    all = soup.find_all("div",{"class": "maincounter-number"})
    total_case = all[0].find("span").text
    deaths = all[1].find("span").text
    recovered = all[2].find("span").text

    print(f"Coronavirus Cases: {total_case}\nDeaths: {deaths}\nRecovered: {recovered}")
except:
    print("Error!!!")
