import requests
from bs4 import BeautifulSoup
import amazonDetails as details
import amazonRating as rating
import amazonReviews as reviews
from time import sleep

if __name__=="__main__":
    headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.115 Safari/537.36"}

    url = input("Paste the Amazon URL of the product : ")
    # url = "https://www.amazon.in/Redmi-9A-2GB-32GB-Storage/dp/B08696XB4B/ref=sr_1_3?dchild=1&keywords=mobile&qid=1628157865&sr=8-3"
    resp = requests.get(url, headers=headers)

    soup=BeautifulSoup(resp.content,"lxml")

    
    details.printDetails(soup)
    sleep(2)
    rating.printRating(soup)
    sleep(2)
    reviews.printTopReviews(soup)

