
# coding: utf-8

# In[1]:




# In[2]:

with open("weather_info.txt", 'r', encoding="utf8") as f: 
    weather_dict = {} # use to store all cities and weather info
    hist = {} # use to store search history
    for line in f: # read one line at a time
        b = line.strip('\n').split(',') # split the string to a list between ',' and strip the \n at the end
        weather_dict[b[0]] = b[1] # put the first item of the list as key and second as value

city_list = list(weather_dict.keys()) # make a list of all cities available


# In[3]:

def rem_redn(ini_input):
    """If the city input is valid but has redundant letter, 
    remove the letter and return revised input"""
    redu_letter = ['市','县','镇','村','乡','区']
    if ini_input[:-1] in city_list and ini_input[-1] in redu_letter: # make sure the input is valid for revision
        revi_input = ini_input[:-1] # delete the redundant letter at the end of the string
        return revi_input # return the revised version
    else:
        return ini_input # if not found in weather_dict after the removal, keep the initial one


# In[4]:

def app_help():
    """This will print out the help readme file when called."""
    print("-" * 60)
    print("\n" * 2)
    print("""使用说明\n\n
    输入城市名称, 查询对应城市天气情况\n
    输入'h'或'help', 查询程序使用说明\n
    输入'history', 查询城市搜索记录\n
    输入'q'或'quit', 退出程序""")
    print("\n" * 2)
    print("-" * 60)


# In[5]:

def app_history():
    """This function is to print all valid cities inquired."""
    if hist == {}:
        print("城市天气查询记录为空。")
    else:
        print("城市查询历史：")
        for k, v in hist.items():
            print(k, ":", v)


# In[6]:

def show_weather():
    """To ask user for input of the name of the city and return the pertinent weather info of the city"""
    print("请输入中国地区城市名称查询天气情况，如需帮助，请输入'h'或'help‘获取程序使用说明。")
    while True:
        user_input = input("请输入指令或城市名称：")
        if user_input in ["help", "h"]:
            app_help()
        elif user_input == "history":
            app_history()
        elif user_input in ["quit","q"]:
            break
            exit()
        else:
            rem_redn(user_input) # check first if the revised input can be found in the list
            try:
                output = weather_dict[rem_redn(user_input)]
            except KeyError:
                print("无法找到相关城市信息，请重新输入。如需帮助，请输入'h'或'help'获取使用指南。")
            else:
                print("%s的天气状况是%s。" % (user_input, output))
                hist[user_input] = output   


# In[7]:

show_weather()


# In[ ]:



