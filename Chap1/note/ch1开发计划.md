# ch1开发计划

## 确定MVP(Minimum Viable Product)

需要实现哪些功能：

- 输入城市名，返回该城市的天气数据；
- 输入指令，打印帮助文档（一般使用 h 或 help）；
- 输入指令，退出程序的交互（一般使用 quit 或 exit）；
- 在退出程序之前，打印查询过的所有城市。

其中，核心功能是：

- 输入城市名，返回该城市的天气数据

## 开发计划

大体解决思路

1. 将个城市作为key, 天气数据作为value, 建立dict, 用input()要输入后，能够识别并print对应value
   - 怎么将txt文档中, "城市, 天气" 的格式转换成['城市': '天气'] 
   - 如果输入了文档里没有的城市，或者无效的字母或数字，怎么办？
   - 使用中文，python的utf-8怎么弄？
2. 建立帮助文档，用户通过input()输入"help"或"h"后，能够读取并返回文档内容
   - 如何实现？首先建立txt文档？
   - 用什么方式来read这个帮助文档？可能要回顾一下LPTHW读取文档的部分
3. 用户通过input()输入"quit"后，能退出程序。
   - 怎么退出程序？exit()？
4. 将input()中输入过的城市名字保存成dict，并在输入"history"之后能查询已有历史
   - 首先要建立一个空dict，然后用户输入一个城市，得到相应的天气值，之后将两者保存在dict中。
   - 用户通过input()输入"history"可以调用历史
   - 打印的方式怎么更优雅？即 “城市” “天气”

## 实现MVP

实现核心功能，需要哪些步骤？



其中涉及哪些知识点？

1. 字典数据的储存，调用，修改
   - 如何保存数据
   - 如何分开打印key 和 value (回顾一下LPTHW练习)
2. 函数的建立以及method()的使用
   - method()比如read(), readline()。
   - 怎样做退出程序的函数