# Write here the code challenge solution
from stack import Stack

class MyQueue:
    
    def __init__(self):
        self.front = Stack()
        self.rear = Stack()
        self.q=[]
        
    # push function
    def push(self, x):
        if self.rear.get_size() != 0:
            for item in range(self.rear.get_size()):
                self.front.push(self.rear.pop())
        self.q.append(x)
        self.front.push(x)
        for item in range(self.front.get_size()):
            self.rear.push(self.front.pop())
    # pop function
    def pop(self):

        if not self.rear:
            return self.rear 
        self.q.pop(0)
        return self.rear.pop()
    # peek function
    def peek(self):
        return self.rear.peek()
    # empty function
    def is_empty(self):
        return self.rear.is_empty()
    # get queue function
    def get_queue(self):
        return self.q
        
# test for me
if __name__ == '__main__':

 
    myQueue = MyQueue()
    myQueue.push(1) # queue is: [1]
    myQueue.push(2) # queue is: [1, 2] (leftmost is front of the queue)
    myQueue.get_queue() # return 1
    print(myQueue.pop()) # return 1, queue is [2]

  
   