# python3
from math import ceil

class Block():
    def __init__(self,a=[]) -> None:
        self.items = []
        self.max = []
        if a:
            for ele in a:
                self.add(ele)

    def add(self,a):
        if len(self.items)==0:
            self.max.append(a)
            self.items.append(a)
        else:
            self.items.append(a)
            temp = max(self.max[-1],a)
            self.max.append(temp)       

def max_sliding_window(sequence, m):
    l = len(sequence)
    max_nums = []
    suffix_blocks =[]
    prefix_blocks = []

    for i in range(0,l,m):
        start = i
        end = min(i+m,l)
        suffix_blocks.append(Block(sequence[start:end]))
        prefix_blocks.append(Block(sequence[start:end][::-1]))

    pblock = sblock = 0
    pele = sele = m-1

    for j in range(l-m+1):
        prefix = prefix_blocks[pblock].max[pele]
        suffix = suffix_blocks[sblock].max[sele]

        max_nums.append(max(prefix,suffix))

        if pele == 0: pblock+=1
        if sele == m-1: sblock+=1

        pele = (pele - 1)%m
        sele = (sele + 1)%m

    return max_nums


def max_sliding_window_naive(sequence, m):
    maximums = []
    for i in range(len(sequence) - m + 1):
        maximums.append(max(sequence[i:i + m]))

    return maximums

if __name__ == '__main__':
    n = int(input())
    input_sequence = [int(i) for i in input().split()]
    assert len(input_sequence) == n
    window_size = int(input())

    print(*max_sliding_window(input_sequence, window_size))