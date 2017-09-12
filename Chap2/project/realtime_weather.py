
# coding: utf-8

# In[3]:

import requests
import json
import sys


# In[4]:

def app_help():
    """This will print out the help readme file when called."""
    print("-" * 60)
    print("""使用说明\n\n
    输入城市名称, 查询对应城市天气情况\n
    输入'h'或'help', 查询程序使用说明\n
    输入'history', 查询城市搜索记录\n
    输入'q'或'quit', 退出程序""")
    print("-" * 60)


# In[5]:

def app_history():
    """This function is to print all valid cities inquired."""
    if hist == []:
        print("城市天气查询记录为空。")
    else:
        print("城市查询历史：")
        for item in hist:
            print(item)


# In[6]:

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
    app_result = "%s的天气是%s, 气温为%s摄氏度, 更新时间: %s %s" % (city_name, weather, temp, year_now, time_now)
    return app_result


# In[7]:

print("欢迎使用天气查询系统")
app_help()

while True:
    user_input = input("请输入想查询的城市名或指令 >>> ")
    if user_input == "h" or user_input == "help":
        app_help()
    elif user_input == "q" or user_input == "quit":
        print("感谢你使用天气查询软件！再见！")
        break
    elif user_input == "history":
        app_history()
    else:
        try:
            output = get_weather(user_input)
        except KeyError:
            print("无法找到相关指令或城市名的信息，请重新输入。如需帮助，请输入'h'或'help'获得使用指南。")
        else:
            print(output)
            hist.append(output)
       
    
        

        

