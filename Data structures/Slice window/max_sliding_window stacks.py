# python3

class StackWithMax():
    def __init__(self):
        self.__stack = []
        self.maximum= None
    
    def __len__(self):
        return len(self.__stack)

    def Push(self, a):
        if len(self)==0: self.maximum =a
        if a > self.maximum:
            temp = 2*a - self.maximum
            self.__stack.append(temp)
            self.maximum = a
        else:
            self.__stack.append(a)

    def Pop(self):
        assert(len(self.__stack))
        x = self.__stack.pop()
        if x > self.maximum:
            self.maximum = 2*self.maximum - x
        return x

    def Max_naive(self):
        assert(len(self.__stack))
        return max(self.__stack)

    def Max(self):
        if len(self.__stack)==0: 
            return float('-inf')
        return self.maximum 
    
class QueueWithStack():
    def __init__(self):
        self.inbox = StackWithMax()
        self.outbox = StackWithMax()
    
    def enqueue(self,a):
        self.inbox.Push(a)

    def dequeue(self,a):
        if len(self.outbox)==0:
            while(len(self.inbox)):
                temp = self.inbox.Pop()
                self.outbox.Push(temp)
        self.outbox.Pop()
    
    def Max(self):
        return max(self.inbox.Max(),self.outbox.Max())
    

def max_sliding_window(sequence, m):
    dq = QueueWithStack()
    max_nums = []
    l = len(sequence)

    for x in range(l):
        dq.enqueue(sequence[x])
        if (x>=m):
            dq.dequeue(sequence[x-m+1])
        if (x>=m-1):
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

