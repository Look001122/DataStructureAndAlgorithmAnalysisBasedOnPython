# @Time:2025/7/6 16:58
# @Author:卢科
# @Description:代码清单2-12 比较列表和字典的包含操作
import timeit
import random
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']  # 或者 'SimSun', 'PingFang SC', 'WenQuanYi Zen Hei' 等
plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题

# 数据收集
list_sizes = range(10000, 1000001, 20000)
lst_times = []
d_times = []

for i in list_sizes:
    t = timeit.Timer('random.randrange(%d) in x' % i, 'from __main__ import random,x')

    # 测量列表的时间
    x = list(range(i))
    lst_time = t.timeit(number=1000)

    # 测量字典的时间
    x = {j: None for j in range(i)}
    d_time = t.timeit(number=1000)

    lst_times.append(lst_time)
    d_times.append(d_time)

# 可视化
plt.figure(figsize=(12, 8))
plt.plot(list_sizes, lst_times, label='列表 (in)', marker='o', linestyle='-', alpha=0.6)
plt.plot(list_sizes, d_times, label='字典 (in)', marker='s', linestyle='-', alpha=0.6)

plt.xscale('log')  # 使用对数刻度
plt.yscale('log')  # 使用对数刻度
plt.xlabel('数据结构大小')
plt.ylabel('执行时间 (秒)')
plt.title('列表 vs 字典 包含操作性能比较')
plt.legend()
plt.grid(True, which="both", ls="--")
plt.savefig('list_vs_dict_performance.png', dpi=300)
plt.show()