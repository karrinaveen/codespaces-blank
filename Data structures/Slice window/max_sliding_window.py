# python3
from collections import deque

def max_sliding_window_approach3(sequence,m):
    #using double ended queues
    slider = deque(sequence[:m])
    maximums = [max(slider)]

    for i in range(m,len(sequence)):
        temp = sequence[i]
        if temp >=maximums[-1]:
            slider = deque([maximums[-1],temp])
            maximums.append(temp)
        else:
            slider.popleft()
            new_slider = []
            for ele in slider:
                if ele>sequence[i]:
                    new_slider.append(ele)
            new_slider.append(temp)
            slider = deque(new_slider)
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

