# @Time:2025/7/18 16:22
# @Author:卢科
# @Description:设计一个实验，证明列表的索引操作为常数阶

import time
import random
import matplotlib.pyplot as plt

def measure_indexing_time(list_size,num_trials):
    """
    测量列表索引操作的时间

    :param list_size: 列表的大小
    :param num_trials: 每个列表大小下重复试验的次数
    :return: 平均索引操作时间(秒)
    """

    #创建一个大小为list_size的列表
    data=list(range(list_size))

    total_time=0

    for _ in range(num_trials):
        #随机选择一个索引
        index=random.randint(0,list_size-1)

        #开始计时
        start_time=time.time()

        #执行索引操作
        _ =data[index]

        #结束计时
        end_time=time.time()

        #累加时间
        total_time += (end_time-start_time)

    #返回平均时间
    return total_time/num_trials

#设置实验参数
sizes=[10**3,10**4,10**5,10**6]
num_trials=1000

#测量不同大小列表的索引操作时间
results=[]
for size in sizes:
    avg_time=measure_indexing_time(size,num_trials)
    results.append((size,avg_time))
    print(f"List size:{size}, Average indexing time:{avg_time:.6f} seconds")

#输出结果
print("\nExperiment Results:")
for size,avg_time in results:
    print(f"List size:{size}, Average indexing time:{avg_time:.6f} seconds")

#提取结果数据
sizes,times=zip(*results)

#绘制图表
plt.figure(figsize=(10, 6))
plt.plot(sizes, times, marker='o', linestyle='-', color='b')
plt.xscale('log')  # 使用对数刻度显示列表大小
plt.xlabel('List Size (log scale)')
plt.ylabel('Average Indexing Time (seconds)')
plt.title('Indexing Time vs. List Size')
plt.grid(True)
plt.show()

