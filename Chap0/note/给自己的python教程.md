
# 给自己的python教程

## 搭建python环境

### 安装python

要学习python，首先，电脑要先安装上python。安装方式有多种，推荐直接通过科学数据分析专用的Anaconda套件进行安装，还自带jupyter notebook，方便省事。

[Continuum&copy; Anaconda](https://www.continuum.io/downloads)

根据需要可以选择基于python 3还是python 2版本的anaconda。因为目前工程界是往python 3的方向发展的，所以推荐基于python 3的版本。安装成功后，在Mac里的终端Termial/ITerm2或者Windows下的Powershell/Cmder里输入 ```python --version``` 可以查询目前python的版本。

```
~|⇒ python --version
Python 3.6.2 :: Anaconda custom (x86_64)
```
如上方代码显示，目前python版本为Python 3.6.2。

如希望升级Python版本，很简单，anaconda套件可以很方便的完成这个任务，只需要在终端打入 ```conda update python``` 即可。

### python多版本问题

虽然python 3是业界发展的方向，但因为是在新旧交替的过程中，所以还是很有可能会需要用到python 2的情况，那多版本的问题怎么解决呢？

很简单，在安装了anaconda后，可以按照你的需求安装新的版本环境。同样有两种方式。比如你已经装了anaconda3，即系统自带python 3了，想要装上python 2，可以根据以下方式操作。

在终端中输入
```
conda create --name <name of the enviornment> python=2
```
其中```<name of the enviornment>```可以是你想给这个python 2环境取的名字，比如把它命名叫```snakes```，那可以这么输
```
conda create --name snakes python=2
```
然后等待安装完毕，你可以通过下面的命令查看目前anaconda已经安装的环境
```
conda info --envs
```
```
# conda environments:
#
snakes                   D:\anaconda\envs\snakes
root                  *  D:\anaconda
```
装好后，在想要转换到python2的环境，很简单，命令激活即可
**Linus/MacOS:** ```source activate snakes```
**Windows:** ```activate snakes```

然后可以再通过```python --version```查询目前是不是已经成功切换到python2版本。

如果需要用回python3呢？反激活即可回到root的python版本
**Linus/MacOS:** ```source deactivate snakes```
**Windows:** ```deactivate snakes```

更多细节参考：[Managing Python](https://conda.io/docs/py2or3.html)

## 数据结构及变量

### 数据结构
Python中有许多数据类型，类型分类及相关特性见下表：

数据类型 | 描述 | 例子
--------|--------|--------
布尔值 boolean value | 布尔逻辑值，只有True和False | True, False
字符串 string | 以单引号```' '```或双引号```" "```包括在之中的文本为字符串 | “Today”, 'tomorrow'
整数 integers | 即数学中的整数，包括正整数和负整数 | 1, 0, -1等
浮点数 floating number | 即数学中带小数位的数字，之所以称为浮点数，是因为科学计数法中，小数点的位置是可以浮动的，如1.12 \* 10<sup>10</sup> 和 11.2 \* 10<sup>9</sup> 是一样的 | 3.2、0.5、 2.33等
列表 list | 是一种有序集合，用```[ ]```所包含, 集合里可以有数字或字符或布尔值，也可以是有一个单独列表作为其中一个元素。序列从0开始 | [‘python’, 1, 'd', 'apple', True, ['This','is','a single list']]
字典 dict | 其它语言中也成为map，使用键-值(key-value)的配对形式储存数据，能够根据key快速查找对应value，用```{ }```组成字典 | {'Mike': 'A', 'Peter': 'B', 'Candy': 95}
空值 None | 一种特殊的空值，表达为None | None

**列表list与元祖tuple**
列表list和元祖tuple的共同点是两者都是有序集合，即其中元素可按先后顺序索引来找到。

list是用```[ ]```来包括，如```[1, 2, 3]```
tuple则是用```( )```来包括，如```(1, 2, 3)```

两者序列都以**0**开始。
```
>>> a = (1, 2, 3)
>>> b = [1, 2, 3]
>>> a[0]
1
>>> b[0]
1
```
用```len()```可以显示list和tuple的元素数量。
```
>>> a = (1, 2, 3)
>>> b = [1, 2, 3]
>>> len(a)
3
>>> len(b)
3
```

但两者不同在于list可以修改，即mutable。而tuple一旦确定元素，不能被修改，即immutable。

因为可被修改的属性，list可用```append()```来在列表最后加入元素

```
>>> b = [1, 2, 3]
>>> b.append(4)
>>> b
[1, 2, 3, 4]
```

list还可以通过```insert()```在指定位置插入元素，如在索引1，插入字符"s"。
```
>>> b.insert(1, "s")
>>> b
[1, 's', 2, 3, 4]
```
还可以通过```pop()```来删除最后一个元素，或者指定位置的元素，如删除索引1的元素。用```pop()```时，会返回被删除的元素的值。

```
[1, 's', 2, 3, 4]
>>> b.pop()
4
>>> b
[1, 's', 2, 3]
>>> b.pop(1)
's'
>>> b
[1, 2, 3]
```

**还需要对dict和set进行学习并补充相关知识点，先挖个坑立个flag**


### 变量
Python里变量(variable)与一般数学里理解的变量没有什么不同，在编程领域，变量不仅可以是数字，也可以是任意数据类型。

```
a = 1
b = 'ABC'
c = [1, 'ABC']
```

#### 静态语言 vs. 动态语言
Python中，变量可以被赋予任何数据类型的值，而且可以反复被赋值，被赋值的类型也可以不同。
```
a = 1 // a 赋值为整数 1
a = 'ABC' // 重新为a赋值，新的赋值为字符串'ABC'
```
这种变量本身类型不固定的语言，称为**动态语言**，相对应的**静态语言**则在定义变量时，就要定义变量的数据类型，如果赋值不匹配，就会报错，如下

```
int a = 123; // a是整数类型变量
a = "ABC"; // 错误：不能把字符串赋给整型变量
```

根据阳老和王垠博客提供的，编程基本的关键概念，列在下面，后续当做之后学习的map，慢慢突破。
- 变量定义
- 算数运算
- for循环与while循环
- 函数定义与函数调用
- 递归
- 静态与动态类型
- 类型推导
- lambda 函数
- 面向对象
- 垃圾回收
- 指针算数
- goto 语句

## Reference
[廖雪峰的python教程](https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/00143167793538255adf33371774853a0ef943280573f4d000)
