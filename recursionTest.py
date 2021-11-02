# coding: utf-8

# <算法图解>练习4.1, test
from collections import deque


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


# <算法图解>练习题6.1
def findend(node_name='start'):
    """
    从起点开始, 先搜寻一度关系, 再搜寻二度关系, 以此类推, 直到找到目标并找到最短的路径抵达;
    0. 画图建立问题模型(题中已给出图), 图由节点和边组成; 代码中可以使用散列表来实现图
    1. 假设起点为start, 终点目标为f; 一度关系为[a,b]; 二度关系a为[c, f]; 二度关系b为[c, d], 三度关系d为[f];
    2. 从节点s出发, 是否有通往f的路径? 通往f的路径中, 哪条路径最短? (广度优先搜索可回答这两个问题)
    3. 需要从离节点s最近的节点开始搜索(可使用队列进行)
    :return:
    """
    graph = {}
    graph['start'] = ['a', 'b']
    graph['a'] = ['c', 'f']
    graph['b'] = ['c', 'd']
    graph['c'] = []
    graph['d'] = ['f']

    search_path = deque()
    search_path += graph['start']
    searched = []

    while search_path:
        node = search_path.popleft()  # 取出第一个节点
        if node not in searched:
            if is_end(node):  # 判断是否为终点
                print("已找到终点")
                return True
            else:
                search_path += graph[node]  # 不是终点, 则将该节点所能走到的节点(也就是该节点的关系节点)加入搜索队列
                searched.append(node)
    return False


def is_end(node):
    if node == 'f':
        return True


def person_is_seller(name):
    return name[-1] == 'm'


if __name__ == '__main__':
    findend()
    # print(sum([2, 4, 6]))
