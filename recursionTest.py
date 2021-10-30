# coding: utf-8

# <算法图解>练习4.1, test
def sum(arr):
    if len(arr) < 2:  # 基线条件
        return arr[0]
    else:  # 递归条件
        s = arr.pop(0)
        return s + sum(arr)


# <图解算法>快排4.2
def quicksort(arr):
    if len(arr) < 2:
        return arr  # 基线条件, 为空或者只有一个元素的数组都是"有序的"
    else:
        middle_item = arr[0]  # 递归条件
        less = [i for i in arr[1:] if i <= middle_item]  # 所有小于基准值的元素组成的数组
        greater = [i for i in arr[1:] if i > middle_item]  # 所有大于及基准值的元素组成的数组
        return quicksort(less) + [middle_item] + quicksort(greater)


if __name__ == '__main__':
    print(sum([2, 4, 6]))

