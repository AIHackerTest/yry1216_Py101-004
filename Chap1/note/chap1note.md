# Chap1 笔记

这周感觉还是有不少收获的，这里主要记录一下自己这周思考和解决问题的大致过程吧。

## 项目启动

按照ch1的任务演示思考了下需要得到的功能以及可能可以实现功能的相关代码，接着利用卡包里开发计划的模板，形成了自己第一个[开发计划](https://github.com/yry1216/Py101-005/blob/master/Chap1/note/ch1%E5%BC%80%E5%8F%91%E8%AE%A1%E5%88%92.md)。

我觉得形成开发计划，比较重要的方面是——**关注核心功能** 。

其实现在回头看，开发计划还是很粗糙的，不过我认为开发计划不用太细致，只要考虑好程序关键的功能，以及其它需要的功能，有个大致思路能够开始上手写代码就足够了（至少在ch1这个项目的难易程度上来说，是足够的）。

## 实施阶段及难点

这个阶段感觉就是遇到各种难点，以及各种尝试解决方案。

1. 难点一：解决打开中文文件编码报错的问题

   一开始打开文件时发生了报错

```python
>>> with open("weather_info.txt",'r') as f:
...     print(f.readline())
...
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
UnicodeDecodeError: 'gbk' codec can't decode byte 0xb4 in position 9: illegal multibyte sequence
```

这里的报错信息显示是Unicode解码错误，随机google了下解决方案，在[知乎一个页面](https://www.zhihu.com/question/22699590)上发现了一个解决办法，顺便也去看了看廖雪峰python教程里相关的[字符串与编码](https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431664106267f12e9bef7ee14cf6a8776a479bdec9b9000)的章节。不过这里我并没有太深入了解编码的问题，只是有个模糊的了解，就是目前有很多不同的编码方式，如UTF-8，ACSII，而Unicode则是计算机内存统一使用的编码，python3是用Unicode进行解码的，如果所读的文件不是Unicode进行编码的话，解码时会出现问题。而文件存在硬盘里会以UTF-8进行编码，所以解码时需要按照UTF-8来进行解码，这里按照知乎上学到的方式进行解码，不过那个知乎里用到的import codec好像不太需要，删去尝试之后可以正常打开。

```python
>>> # -*- coding:utf8 -*-
...
>>> with open("weather_info.txt",'r',encoding="utf8") as f:
...     print(f.readline())
...
北京,晴
```

2. 难点二：将weather_info.txt里每行的城市与天气转换成相应的dictionary

   一开始思考完成查询城市和相应天气这个功能就会想到用字典dict。那关键的问题是怎么把每行的数据转换成dict。这里有几个点：

   1. 怎么读取每行数据

   - readlines()

   2. 读取完数据是string,怎么变成dict

   - 可以先通过split()把数据将每行变成list——['城市', '天气\n']
   - 因为split之后发现天气后面有分行的formatter \n, 需要去掉，这里可以用strip()先将提取出来的string里strip('\n')来去掉，再用split()形成list
   - 形成list了之后，需要转变成dict，做法可以是先创建一个空dict，如```weather_dict = {}```然后用for循环一个一个把list[0]作为key，list[1]作为value，直到读完这个txt文件。

3.  难点三：调用查询历史的history功能的实现

   这里一开始的想法是用到dict把用户输入过的城市与天气情况进行保存。但是有两点不太清晰：

   - 怎么只保存用户有效的输入而忽略无效输入？
     - 反过来想，如果只有输入正确时，才进行保存，那在打印用户正确的输出时，同时保存就可。那就是逻辑上，要先判断用户的输入是否正确有效，有效并打印了结果再保存，无效不保存。
   - 在程序的什么地方保存？怎么优雅的读取？
     - 这里用到dict的一个method, ```.items()```，可以将key和value按照(key, value)来进行匹配读取。

   其他地方的难度不大，将剩余各功能用专门的函数封装，然后在主程序中调用即可，需要注意的大概是程序运行的逻辑吧，我采用的逻辑是先判断用户是否输入了除了城市外的其它有效指令，如history等，当都不是的时候，再判断用户是否输入正确城市名并决定是否给出相应的值。



## 程序优化

受到@sunwenbo 同学的代码的启发，发现了自己之前写chap1作业时没发现的问题，那就是当用户输入“北京市”，“海淀区”这类从平时语言习惯上合适，但因为加入了像“市”、“区”这种辖区划分的后缀之后程序无法识别的问题。

@sunwenbo同学的代码里，我理解是加入了判断用户输入是否字符在城市的列表里，如果在就print信息提醒用户把后缀去掉。这里我的想法是，有没有什么办法实现当用户输入像“北京市”或“海淀区”城市名时仍然能够被程序识别。

- 我期待实现的效果/欲达成的目的是：识别带有辖区划分后缀的城市名
- 我的系统、版本等环境配置是：python 3.6.2

今天琢磨了挺久的，不过最后还是顺利解决了，这里分享一下我的解决方案和思路吧，顺便也想看看大家在这个问题上有没有更优雅的解法。

## 思路

诸如这种情况，一般是城市名字是天气库中有的，只是因为多了个后缀而不能被识别。那如果用户输入的城市，去掉后缀，还能在天气库里找到，那就直接去掉用户输入的字符里的最后一个字，再将更正后的输入放入程序中就好了。

所以在生成用来查询天气的dictionary之后，按照在@sunwenbo 同学的代码里学到的方式，通过```list()```和```dict.keys()```来把所有天气库里的城市制作成list。

接着我考虑了一下后缀的问题，辖区划分，固定就那么多，像“市”，“区”，“镇”，“乡”等，把这些固定的后缀的字，统一放到一个list里，如果用户输入去掉最后一个字，在城市list中能找到，而且最后一个字在固定后缀字的list中（避免出现”北京事“这样的情况），那就把最后一个字去掉当做输入，从天气库中读取。代码如下：
```python
# -*- coding:utf8 -*-
with open("weather_info.txt", 'r', encoding="utf8") as f:
    weather_dict = {}
    hist = {}
    for line in f:
        b = line.strip('\n').split(',')
        weather_dict[b[0]] = b[1]

city_list = list(weather_dict.keys())

def rem_redn(ini_input):
    """If the city input is valid but has redundant letter, 
    remove the letter and return revised input"""
    redu_letter = ['市','县','镇','村','乡','区']
    if ini_input[:-1] in city_list and ini_input[-1] in redu_letter: # make sure the input is valid for revision
        revi_input = ini_input[:-1] # delete the redundant letter at the end of the string
        return revi_input # return the revised version
    else:
        return ini_input # if not found in weather_dict after the removal, keep the initial one
```
