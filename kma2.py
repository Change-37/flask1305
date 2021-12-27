from urllib import request
from bs4 import BeautifulSoup

# 서울 예보
target = request.urlopen("https://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=159")


soup = BeautifulSoup(target, "html.parser")
with open(file="bnk-weather.xml", mode="a") as urlPage:
    urlPage.write("{}".format(soup))


for location in soup.select("location"):
    print("도시:", location.select_one("city").string)
    print("날씨:", location.select_one("wf").string)
    print("최저기온:", location.select_one("tmn").string)
    print("최고기온:", location.select_one("tmx").string)
    print("날짜:", location.select_one("tmEf").string)
    print()