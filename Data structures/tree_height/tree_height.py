# python3

import sys
import threading
import time
from collections import defaultdict

class node():
    def __init__(self,value):
        self.value = value
        self.child = []

    def add_child(self,child):
        self.child.append(child)


def compute_height_naive(n, parents):
    # Replace this code with a faster implementation
    max_height = 0
    for vertex in range(n):
        height = 0
        current = vertex
        while current != -1:
            height += 1
            current = parents[current]
        max_height = max(max_height, height)
    return max_height

def compute_height_recursion(n,parents):
    nodes = [node(i) for i in range(n)]
    root = 0

    for child,parent in enumerate(parents):
        if parent==-1:
            root = child
        else:
            nodes[parent].add_child(nodes[child])
            
    def max_height(node):
        if len(node.child)==0:
            return 1
        else:
            children = node.child
            height = 1 + max([max_height(child) for child in children])
            return height

    return max_height(nodes[root])

def compute_height(n,parents):
    nodes = [node(i) for i in range(n)]
    root = 0
    for child,parent in enumerate(parents):
        if parent==-1:
            root = child
        else:
            nodes[parent].add_child(nodes[child])
    
    heights = defaultdict(int)
    def height(node):
        if node.value==root:
            return 1
        else:
            pnode = nodes[parents[node.value]]
            if heights[pnode.value]!=0:
                heights[node.value] = 1+ heights[pnode.value]
            else:
                heights[node.value] = 1+ height(pnode)
        return heights[node.value]
    
    max_height = 1
    for n in nodes:
        if len(n.child)==0:
            max_height = max(max_height,height(n))
    
    return max_height


def main():
    n = int(input())
    parents = list(map(int, input().split()))
    print(compute_height(n, parents))



# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
