import timeit
import matplotlib.pyplot as plt

# 数据收集
list_sizes = range(1000000, 100000001, 1000000)
popzero_times = []
popend_times = []

for size in list_sizes:
    # 测量pop(0)时间
    x = list(range(size))
    timer = timeit.Timer("x.pop(0)", "from __main__ import x")
    time_zero = timer.timeit(number=1000) * 1000  # 毫秒
    popzero_times.append(time_zero)

    # 测量pop()时间
    x = list(range(size))
    timer = timeit.Timer("x.pop()", "from __main__ import x")
    time_end = timer.timeit(number=1000) * 1000  # 毫秒
    popend_times.append(time_end)

# 可视化
plt.figure(figsize=(12, 8))
plt.scatter(list_sizes, popzero_times, label='pop(0)', alpha=0.6)
plt.scatter(list_sizes, popend_times, label='pop()', alpha=0.6)

plt.xscale('log')  # 使用对数刻度
plt.xlabel('列表长度')
plt.ylabel('执行时间 (毫秒)')
plt.title('pop(0) vs pop() Performance Comparison')
plt.legend()
plt.grid(True, which="both", ls="--")
plt.savefig('pop_performance.png', dpi=300)
plt.show()