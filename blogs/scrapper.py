from bs4 import BeautifulSoup
import requests


def scrap(url="https://www.onlinekhabar.com/2018/12/724699"):
    try:
        res = requests.get(url)
        # print(res.text)
        # print(res.encoding)
        res.encoding = "utf-8"
        bs = BeautifulSoup(res.text, "html.parser")

        dict = {}
        dict["title"] = bs.select(".nws__title--card > h2")[0].text
        dict["published"] = bs.select(".post__time > span")[0].text
        dict["description"] = bs.select(".main__read--content")[0].text

        return dict
    except:
        return None

if __name__ == '__main__':
    print(scrap())