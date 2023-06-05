import requests
from bs4 import BeautifulSoup


def sendMsg(codeSrc):
    data = {
        "token": "8906471ad908426db7f4e17d229bf46a",
        "title": "通行码",
        "content": codeSrc,
    }
    requests.post(url="http://www.pushplus.plus/send/", data=data)


if __name__ == "__main__":
  sendMsg("886")
