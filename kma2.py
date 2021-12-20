from urllib import request
from bs4 import BeautifulSoup

# 우리집 예보
target = request.urlopen("https://www.kma.go.kr/wid/queryDFSRSS.jsp?zone=2626057000")


soup = BeautifulSoup(target, "html.parser")
with open(file="myhome-weather.xml", mode="a") as urlPage:
    urlPage.write("{}".format(soup))

tm = soup.select_one("tm")
print("도시:", soup.select_one("category").string)
for data in soup.select("data"):
    print("날씨:", data.select_one("wfKor").string)
    print("최저기온:", data.select_one("tmn").string)
    print("최고기온:", data.select_one("tmx").string)
    print("예상기온:", data.select_one("temp").string)
    print("날짜:", data.select_one("day").string)
    print("시간:", data.select_one("hour").string, ": 00")
    print()