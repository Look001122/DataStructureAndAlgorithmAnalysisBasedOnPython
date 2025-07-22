# @Time:2025/7/22 15:58
# @Author:卢科
# @Description:3.设计一个实验，针对列表和字典比较del操作的性能

import timeit
#import matplotlib.pyplot as plt


def create_setup(n):
    """为 timeit 创建 setup 环境"""
    list_setup = f"""
from __main__ import n
my_list = list(range(n))
index = n // 2  # 删除中间元素
"""
    dict_setup = f"""
from __main__ import n
my_dict = {{i: i for i in range(n)}}
key = n // 2
"""
    return list_setup, dict_setup


# 定义要测试的数据规模
sizes = [10000, 20000, 100000, 200000]
list_times = []
dict_times = []

# 待执行的 del 操作语句
list_stmt = "del my_list[index]"
dict_stmt = "del my_dict[key]; my_dict[key] = key"

number_of_deletions = 1000  # 每个规模重复执行次数

for n in sizes:
    list_setup, dict_setup = create_setup(n)

    # 测量列表 del 性能
    list_time = timeit.timeit(stmt=list_stmt, setup=list_setup, number=number_of_deletions)
    list_times.append(list_time / number_of_deletions)  # 平均每次时间

    # 测量字典 del 性能
    dict_time = timeit.timeit(stmt=dict_stmt, setup=dict_setup, number=number_of_deletions)
    dict_times.append(dict_time / number_of_deletions)

# 输出结果
print(f"{'Size':<8} {'List (s)':<12} {'Dict (s)':<12} {'Ratio (L/D)':<12}")
print("-" * 45)
for i, n in enumerate(sizes):
    ratio = list_times[i] / dict_times[i] if dict_times[i] > 0 else float('inf')
    print(f"{n:<8} {list_times[i]:<12.2e} {dict_times[i]:<12.2e} {ratio:<12.2f}")
"""
# 可视化结果
plt.figure(figsize=(10, 6))
plt.plot(sizes, list_times, label='List del (middle)', marker='o')
plt.plot(sizes, dict_times, label='Dict del (key)', marker='s')
plt.xlabel('Data Size (n)')
plt.ylabel('Average Time per del (seconds)')
plt.title('Performance Comparison: del operation on List vs Dict')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
"""

