# @Time:2025/7/26 16:41
# @Author:卢科
# @Description:给定一个数字列表，其中的数字随机排列，编写一个线性阶算法，找出第k小的元素，并解释为何该算法的阶是线性的。
import random


def partition(arr, low, high):
    """
    分区函数：选择最后一个元素作为 pivot，将数组分为两部分，
    左侧小于等于 pivot，右侧大于等于 pivot，并返回 pivot 的最终位置。
    """
    pivot = arr[high]
    i = low - 1  # i 是小于等于 pivot 的元素的最后一个索引

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]  # 交换元素，确保小于等于 pivot 的元素在左侧

    # 将 pivot 放置到正确的位置
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quickselect(arr, low, high, k):
    """
    快速选择算法：在数组中找到第 k 小的元素。
    """
    if low == high:  # 基本情况：只有一个元素
        return arr[low]

    pivot_index = partition(arr, low, high)

    # 根据 pivot 的位置判断第 k 小的元素在哪一部分
    if k == pivot_index:
        return arr[k]
    elif k < pivot_index:
        return quickselect(arr, low, pivot_index - 1, k)
    else:
        return quickselect(arr, pivot_index + 1, high, k)


def find_kth_smallest(arr, k):
    """
    主函数：调用 quickselect 找到第 k 小的元素。
    """
    if k < 1 or k > len(arr):
        raise ValueError("k must be within the range of the array length")
    return quickselect(arr, 0, len(arr) - 1, k - 1)  # k-1 因为索引从 0 开始


# 测试代码
if __name__ == "__main__":
    arr = [7, 10, 4, 3, 20, 15]
    k = 3
    result = find_kth_smallest(arr, k)
    print(f"The {k}rd smallest element is: {result}")
