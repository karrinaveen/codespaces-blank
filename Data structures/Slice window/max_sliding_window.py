# python3
from collections import deque
import itertools

def max_sliding_window(sequence, m):
    dq = deque()
    max_nums = []
    length = len(sequence)
    for i in range(length):
        # print(dq)
        while dq and sequence[i] >= sequence[dq[-1]]:
            dq.pop()
        dq.append(i)
        if i >= m and dq and dq[0] == i - m:
            dq.popleft()
        if i >= m - 1:
            max_nums.append(sequence[dq[0]])
    return max_nums

def max_sliding_window_approach3(sequence,m):
    #using double ended queues
    if m==1: 
        return sequence

    slider = deque(sequence[:m])
    maximums = [max(slider)]

    for i in range(m,len(sequence)):
        print(slider)
        slider.popleft()
        left_ele = sequence[i-m+1]
        right_ele = sequence[i]
        if right_ele>=maximums[-1]:
            slider.append(right_ele)
            maximums.append(right_ele)
        else:
            newslider = deque()
            for ele in slider:
                if ele >= right_ele:
                    newslider.append(ele)
            if len(newslider)==0 or newslider[0]!=left_ele:
                newslider.appendleft(left_ele)
            newslider.append(right_ele)
            slider = newslider.copy()
            maximums.append(max(slider))
    return maximums


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

