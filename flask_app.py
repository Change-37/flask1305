from flask import Flask, render_template
import sys
from urllib import request
from bs4 import BeautifulSoup
 
app = Flask(__name__)
 
@app.route("/")
def home():
    return render_template('index.html', subject="박창은입니다, 반갑습니다.")
 
#1-1
@app.route('/<user>')
def hello(user):
    return '<h1> hello ' + user
 
@app.route("/about")
def about():
    return render_template('busan1.html', subject="부산중위연령시각화")
 
@app.route("/show1")
def show1():
    return render_template('img_test1.html', image_file='img/1.jpg')
 
@app.route("/kma")
def kma():
  target = request.urlopen("http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stdId=108")
 
  soup = BeautifulSoup(target, "html.parser")
 
  output = ""  
  for item in soup.select("item"):
    output += "<h2>{}</h2><hr/>".format(item.select_one("title").string)
 
  for location in soup.select("location"):
    output += "<h3>{}</h3>".format(location.select_one("city").string)
    output += "날씨: {}</br>".format(location.select_one("wf").string)
    output += "최저/최고 기온: {}/{}".format(location.select_one("tmn").string, location.select_one("tmx").string)
    output += "<hr/>"  
 
  output += "{}</br>".format(soup.select_one("title").string)
  output += "날짜: {}</br>".format(location.select_one("tmEf").string)  
  output += "지역: {}</br>".format(soup.select_one("province").string)
 
  return output
 
@app.route("/kma1")
def kma1():
  target = request.urlopen("https://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=109")
 
  soup = BeautifulSoup(target, "html.parser")
 
  output = ""
 
  for item in soup.select("item"):
    output += "<h2>{}</h2><hr/>".format(item.select_one("title").string)
   
  for location in soup.select("location"):
    output += "<h3>{}</h3>".format(location.select_one("city").string)
    output += "날짜: {}</br>".format(location.select_one("tmEf").string)
    output += "날씨: {}</br>".format(location.select_one("wf").string)
    output += "최저/최고 기온: {}/{}".format(location.select_one("tmn").string, location.select_one("tmx").string)
    output += "<hr/>"
 
  output += "{}</br>".format(soup.select_one("title").string)
  output += "날짜: {}</br>".format(location.select_one("tmEf").string)  
  output += "지역: {}</br>".format(soup.select_one("province").string)
 
  return output

  
@app.route("/kma2")
def kma1():
  target = request.urlopen("https://www.kma.go.kr/wid/queryDFSRSS.jsp?zone=2626057000")
 
  soup = BeautifulSoup(target, "html.parser")
 
  output = ""
  tm = ""
 
  for item in soup.select("item"):
    output += "<h2>{}</h2><hr/>".format(item.select_one("title").string)

  for item in soup.select("head"):
    tm += item.select_one("tm").string
   
  for data in soup.select("data"):
    output += "<h3>{}</h3>".format(data.select_one("city").string)
    output += "날짜: {}</br>".format(data.select_one("day").string)
    output += "시간: {}:00</br>".format(data.select_one("hour").string)
    output += "날씨: {}</br>".format(data.select_one("wfKor").string)
    output += "예상 기온: {}</br>".format(data.select_one("temp").string)
    output += "최저/최고 기온: {}/{}".format(data.select_one("tmn").string, data.select_one("tmx").string)
    output += "<hr/>"
 
  output += "{}</br>".format(soup.select_one("title").string)
  output += "지역: {}</br>".format(item.select_one("category").string)
 
  return output
if __name__ == '__main__':
    app.run(host='127.0.0.1', port='5000', debug=True)
