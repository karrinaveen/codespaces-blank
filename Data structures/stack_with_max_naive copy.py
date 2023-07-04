#python3
import sys

# Class to make a Node
class Node:
    #Constructor which assign argument to nade's value
    def __init__(self, value):
        self.value = value
        self.next = None
   
    # This method returns the string representation of the object.
    def __str__(self):
        return "Node({})".format(self.value)
     
    #  __repr__ is same as __str__
    __repr__ = __str__

class Stack:
    # Stack Constructor initialise top of stack and counter.
    def __init__(self):
        self.top = None
        self.count = 0
        self.maximum = None
     
    #This method is used to get minimum element of stack
    def getMax(self):
        if self.top is None:
            return "Stack is empty"
        else:
            return self.maximum

 
    # Method to check if Stack is Empty or not
    def isEmpty(self):
        # If top equals to None then stack is empty
        if self.top == None:
            return True
        else:
        # If top not equal to None then stack is empty
            return False
 
    # This method returns length of stack      
    def __len__(self):
        self.count = 0
        tempNode = self.top
        while tempNode:
            tempNode = tempNode.next
            self.count+=1
        return self.count 
 
    #This method is used to add node to stack
    def push(self,value):
        if self.top is None:
            self.top = Node(value)
            self.maximum = value
             
        elif value > self.maximum :
            temp = (2 * value) - self.maximum
            new_node = Node(temp)
            new_node.next = self.top
            self.top = new_node
            self.maximum = value
        else:
            new_node = Node(value)
            new_node.next = self.top
            self.top = new_node
   
    #This method is used to pop top of stack
    def pop(self):
        if self.top is None:
            print( "Stack is empty")
        else:
            removedNode = self.top.value
            self.top = self.top.next
            if removedNode > self.maximum:
                self.maximum = ( ( 2 * self.maximum ) - removedNode )
    

if __name__ == '__main__':
    stack = Stack()

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
