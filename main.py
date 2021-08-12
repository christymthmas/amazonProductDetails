import requests
from bs4 import BeautifulSoup
import amazonDetails as details
import amazonRating as rating
import amazonReviews as reviews
from time import sleep

if __name__=="__main__":
    headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.115 Safari/537.36"}
    while True:
        url = input("Paste the Amazon 🇮🇳 URL of the product : ")
        # url = "https://www.amazon.in/Redmi-9A-2GB-32GB-Storage/dp/B08696XB4B/ref=sr_1_3?dchild=1&keywords=mobile&qid=1628157865&sr=8-3"
        baseurl ="https://www.amazon.in/"
        serachURL ="https://www.amazon.in/s?"
        if not url:
            print("\n\nURL can't be empty!\n\n")
            sleep(2)
        elif url.find(baseurl) == -1:
            print("\n\nInvalid URL!\n\nPlease provide an Amazon India URL which starts with '{}...'\n\n".format(baseurl))
            sleep(2)
        elif url.find(serachURL) != -1:
            print("\n\nInvalid URL!\n\nPlease provide a product URL!\n\n".format(baseurl))
            sleep(2)
        else:
            break

    resp = requests.get(url, headers=headers)

    soup = BeautifulSoup(resp.content,"lxml")

    
    details.printDetails(soup)
    sleep(2)
    rating.printRating(soup)
    sleep(2)
    reviews.printTopReviews(soup)

