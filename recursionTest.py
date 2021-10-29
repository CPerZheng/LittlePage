# coding: utf-8

# <算法图解>练习4.1, test
def sum(arr):
    if len(arr) < 2:  # 基线条件
        return arr[0]
    else:  # 递归条件
        s = arr.pop(0)
        return s + sum(arr)


if __name__ == '__main__':
    print(sum([2, 4, 6]))

