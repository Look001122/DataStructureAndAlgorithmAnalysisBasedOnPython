构造函数（Constructor）是面向对象编程中一个非常重要的概念，它用于初始化一个类的实例 。在 Python 中，`__init__` 方法就是我们通常所说的“构造函数”。
### 一、什么是构造函数？
定义：构造函数是一个特殊的类方法，在创建类的新实例时自动调用，用来为新对象设置初始状态。  
在 Python 中，这个构造函数叫做：`__init__`
### 二、构造函数的基本写法
```python
class 类名:
    def __init__(self, 参数1, 参数2, ...):
        # 初始化代码
        self.属性1 = 参数1
        self.属性2 = 参数2
```
- `self`是第一个参数，代表当前对象自己。
- 构造函数可以接受多个参数，用于初始化对象的属性。
### 三、你写的 Stack 类中的构造函数
```python
class Stack:
    def __init__(self):
        self.items = []
```
#### 解释:
- 当你执行 s = Stack() 时，Python 会自动调用 `__init__` 方法。
- 这个构造函数的作用是：
    - 创建一个新的栈对象；
    - 并初始化一个空列表 `self.items`，用来保存栈中的元素。

所以每个 Stack 实例都会有自己的 items 属性，彼此之间互不干扰。
### 四、构造函数的作用总结
| 作用 | 描述 |
|----|----|
| 初始化属性   |  在创建对象时设置一些默认值或初始状态  |
|  自动调用  |  不需要手动调用，创建实例时自动运行  |
|  支持参数  |  可以带参数，用来定制对象的初始状态  |
### 五、构造函数带参数的例子
比如我们想让栈在创建时就有一些初始元素：  
```python
class Stack:
    def __init__(self, initial_items=None):
        if initial_items is None:
            self.items = []
        else:
            self.items = list(initial_items)
```
使用示例：
```python
s1 = Stack()
print(s1.items)  # []

s2 = Stack([1, 2, 3])
print(s2.items)  # [1, 2, 3]
```
### 总结一句话：
构造函数 `__init__ `就是用来给新创建的对象设置初始状态的方法。它是类的实例化过程中不可或缺的一部分。