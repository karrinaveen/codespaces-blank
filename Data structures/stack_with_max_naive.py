#python3
import sys

class StackWithMax():
    def __init__(self):
        self.__stack = []
        self.__max= [float('-inf')]

    def Push(self, a):
        self.__stack.append(a)
        new_max = max(a,self.__max[-1])
        self.__max.append(new_max)

    def Pop(self):
        assert(len(self.__stack))
        self.__stack.pop()
        self.__max.pop()

    def Max_naive(self):
        assert(len(self.__stack))
        return max(self.__stack)

    def Max(self):
        assert(len(self.__stack))
        return self.__max[-1]


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
