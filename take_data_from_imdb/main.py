import requests
from bs4 import BeautifulSoup

# Demands:
# 1. Pull movie title
# 2. Pull movie year
# 3. Pull movie rating
# 4. Print them

print("--- TOP MOVIES ---")
try:
    url = requests.get("https://www.imdb.com/chart/top/")
    soup = BeautifulSoup(url.content, "html.parser")

    for i in soup.find("tbody", {"class":"lister-list"}).find_all("tr"):
        movie_name = i.find("td", {"class":"titleColumn"}).a.text
        movie_year = i.find("span",{"class", "secondaryInfo"}).text.strip("()")
        movie_rating = i.find("td", {"class","ratingColumn"}).strong.text

        print("\n" + "*" * 50)
        print(f"Movie Name : {movie_name} - Movie Year : {movie_year} - Movie Rating : {movie_rating}")
except:
    print("Error!!!")