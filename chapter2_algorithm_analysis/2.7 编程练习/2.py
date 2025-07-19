# @Time:2025/7/18 21:10
# @Author:
# @Description:设计一个实验，证明字典的取值操作和赋值操作的时间复杂度为常数阶

import time
import random
import matplotlib.pyplot as plt

def measure_dict_operations(dict_size,num_trials):
    """
    测量字典取值和赋值操作的时间

    :param dict_size:字典的大小
    :param num_trials: 每个字典大小下重复试验的次数
    :return: 取值操作的平均时间，赋值操作的平均时间(秒)
    """

    #创建一个大小为dict_size的字典
    data={i:i for i in range(dict_size)}

    #初始化时间变量
    total_get_time=0
    total_set_time=0

    for _ in range(num_trials):
        # 随机选择一个键
        key=random.randint(0,dict_size-1)

        #开始计时：取值操作
        start_time=time.time()
        _=data[key]
        end_time=time.time()
        total_get_time += (end_time-start_time)

        #开始计时：赋值操作
        new_key=dict_size+random.randint(0,1000)
        new_value=random.randint(0,1000)
        start_time=time.time()
        data[new_key]=new_value
        end_time=time.time()
        total_set_time += (end_time-start_time)

    #计算平均时间
    avg_get_time=total_get_time/num_trials
    avg_set_time=total_set_time/num_trials

    return avg_get_time,avg_set_time

#设置实验参数
sizes=[10**3, 10**4, 10**5, 10**6]
num_trials=1000

#测量不同大小字典的取值和赋值操作时间
results=[]
for size in sizes:
    avg_get_time,avg_set_time=measure_dict_operations(size,num_trials)
    results.append((size,avg_get_time,avg_set_time))

#输出结果
print("\nExperiment Results:")
for size,avg_get_time,avg_set_time in results:
    print(f"Dict size:{size}, Average get time:{avg_get_time:.6f} seconds, Average set time :{avg_set_time:.6f} seconds")

# 提取结果数据
sizes, get_times, set_times = zip(*results)

# 绘制图表
plt.figure(figsize=(10, 6))

# 绘制取值操作时间
plt.plot(sizes, get_times, marker='o', linestyle='-', color='b', label='Get Time')

# 绘制赋值操作时间
plt.plot(sizes, set_times, marker='s', linestyle='--', color='r', label='Set Time')

# 使用对数刻度显示字典大小
plt.xscale('log')
plt.xlabel('Dictionary Size (log scale)')
plt.ylabel('Average Operation Time (seconds)')
plt.title('Operation Time vs. Dictionary Size')
plt.legend()
plt.grid(True)
plt.show()