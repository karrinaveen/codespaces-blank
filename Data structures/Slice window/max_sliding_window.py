# python3
from collections import deque
import itertools

def max_sliding_window_approach3(sequence,m):
    #using double ended queues
    if m==1: 
        return sequence

    slider = deque(sequence[:m])
    maximums = [max(slider)]

    for i in range(m,len(sequence)):
        slider.popleft()
        right_ele = sequence[i]
        left_ele = slider[0]
        if right_ele >=maximums[-1]:
            slider = deque([slider[0],right_ele])
            maximums.append(right_ele)
        else:
            new_slider = deque([left_ele])
            for ele in itertools.islice(slider,1,len(slider)):
                if ele>sequence[i]:
                    new_slider.append(ele)
            new_slider.append(right_ele)
            slider = new_slider.copy()
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

    print(*max_sliding_window_approach3(input_sequence, window_size))

