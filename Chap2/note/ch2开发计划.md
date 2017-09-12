# ch2开发计划

## 确定MVP(Minimum Viable Product)

需要实现哪些功能：

- 利用request模块调用天气api，查询实时城市天气信息
- 输入history记录天气查询记录
- 输入help显示程序使用指南
- 输入quit退出程序

其中，核心功能是：

- 利用request模块调用天气api实时查询城市天气信息

## 开发计划

大体解决思路

1. 了解request模块的使用
   - Get和Post的区别
   - 怎样输入特定的key和url信息
   - 怎样处理返回的数据
     - json文件的读取
2. 建立获取天气信息函数，weather_get()
3. 与ch1已完成的函数进行拼接

## 实现MVP

实现核心功能，需要哪些步骤？



其中涉及哪些知识点？

1. request包的安装与使用
2. get和post的使用与区别
3. api调用url与request如何搭配使用？
4. 返回的json数据的读取​