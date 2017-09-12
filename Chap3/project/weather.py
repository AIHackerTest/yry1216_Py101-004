# -*- coding: utf-8 -*-
from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)

hist = []

def get_weather(city):
    appkey = "jjeovqorokdmdoey"
    api = "https://api.seniverse.com/v3/weather/now.json"
    value = {
        "key": appkey,
        "location": city,
        "language": "zh-Hans",
        "unit": "c"}
    r = requests.get(api, params=value, timeout=60)
    data = json.loads(r.text)["results"][0]
    city_name = data["location"]["name"]
    weather = data["now"]["text"]
    temp = data["now"]["temperature"]
    updatetime = data["last_update"]

    t1 = updatetime.find("T")
    t2 = updatetime.find("+")
    year_now = updatetime[:t1]
    time_now = updatetime[t1+1:t2]
    result_in_dict = {"city": city_name, "weather": weather,"temp": temp,
    "year_now": year_now, "time_now": time_now}
    weather_str = "%s, %s, %s摄氏度, 更新时间：%s %s" % (city_name, weather, temp, year_now, time_now)
    return weather_str

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/requesting', methods=["GET"])
def data_process():
    city = request.args.get('city')
    try:
        weather_str = get_weather(city)
        hist.append(weather_str)
        return render_template('query.html', weather_str=weather_str)
    except KeyError:
        if request.args.get('history') == '历史':
            return render_template('history.html', hist=hist)
        elif request.args.get('help') == '帮助':
            return render_template('help.html')
        else:
            return render_template('404.html')



if __name__ == '__main__':
    app.run(debug=True)
