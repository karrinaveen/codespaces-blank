#python3
import sys

class StackWithMax():
    def __init__(self):
        self.__stack = []
        self.maximum= [float('-inf')]

    def Push(self, a):
        self.__stack.append(a)
        if a >= self.maximum:
            self.maximum.append(a)

    def Pop(self):
        assert(len(self.__stack))
        x = self.__stack.pop()
        if x == self.maximum[-1]:
            self.maximum.pop()

    def Max_naive(self):
        assert(len(self.__stack))
        return max(self.__stack)

    def Max(self):
        assert(len(self.__stack))
        return self.maximum[-1]


if __name__ == '__main__':
    stack = StackWithMax()

    num_queries = int(sys.stdin.readline())
    for _ in range(num_queries):
        query = sys.stdin.readline().split()

        if query[0] == "push":
            stack.Push(int(query[1]))
        elif query[0] == "pop":
            stack.Pop()
        elif query[0] == "max":
            print(stack.Max())
        else:
            assert(0)
