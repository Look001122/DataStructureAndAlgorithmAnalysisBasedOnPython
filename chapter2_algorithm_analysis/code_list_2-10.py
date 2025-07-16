import timeit

popzero=timeit.Timer("x.pop(0)", "from __main__ import x")
popend=timeit.Timer("x.pop()", "from __main__ import x")

x=list(range(2000000))
print(popzero.timeit(number=1000)*1000,"ms")

x=list(range(2000000))
print(popend.timeit(number=1000)*1000,'ms')

"""
为什么创建计时器对象可以写在前面，此时还没有初始化列表x啊！
在代码中，popzero和popend计时器对象的创建确实是在列表 `x` 初始化之前进行的。这看起来似乎有些不合逻辑，因为 `x` 在创建计时器对象时尚未定义。但实际上，`timeit.Timer` 的工作方式使得这种写法是可行的。

timeit.Timer的构造函数接受两个参数：
1. stmt：要测量的代码段（例如 `"x.pop(0)"`）。
2. setup：在执行 `stmt` 之前运行的设置代码（例如 `"from __main__ import x"`）。
关键在于 `setup` 参数。`setup` 代码会在每次执行 `stmt` 之前运行，确保 `x` 已经被正确初始化。

为什么可以这样写?
延迟执行：`timeit.Timer` 的 `stmt` 和 `setup` 代码是在调用 `timeit` 方法时才被执行的。因此，即使 `x` 在创建计时器对象时还没有定义，只要在实际测量之前定义了 `x`，就不会有问题。
独立性：每个 `timeit` 调用都是独立的，`setup` 代码会在每次 `timeit` 调用时重新执行，确保 `x` 在每次测量前都被正确初始化。

"""


