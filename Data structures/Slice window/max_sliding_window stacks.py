# python3

class StackWithMax():
    def __init__(self):
        self.__stack = []
        self.max_value = [float('-inf')]
    
    def __len__(self):
        return len(self.__stack)

    def Push(self, a):
        if not self.max_value:
            self.max_value.append(a)
        elif a >= self.max_value[-1]:
            self.max_value.append(a)
        self.__stack.append(a)

    def Pop(self):
        assert(len(self.__stack))
        if self.__stack[-1] == self.max_value[-1]:
            self.max_value.pop()
        return self.__stack.pop()

    def Max(self):
        return self.max_value[-1] 
    
class QueueWithStack():
    def __init__(self):
        self.inbox = StackWithMax()
        self.outbox = StackWithMax()
    
    def enqueue(self,a):
        self.inbox.Push(a)

    def dequeue(self):
        if len(self.outbox)==0:
            while(len(self.inbox)):
                temp = self.inbox.Pop()
                self.outbox.Push(temp)
        self.outbox.Pop()
    
    def Max(self):
        # if self.inbox.Max() == []:
        #     return max(self.outbox.Max())
        # if self.outbox.Max() == []:
        #     return max(self.inbox.Max())
        return max(self.inbox.Max(),self.outbox.Max())
    

def max_sliding_window(sequence, m):
    dq = QueueWithStack()
    max_nums = []
    l = len(sequence)

    for x in range(l):
        dq.enqueue(sequence[x])
        if (x>=m):
            dq.dequeue()
        if (x>=m-1):
            # print(dq.inbox.Max())
            # print(dq.outbox.Max())
            max_nums.append(dq.Max())
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

