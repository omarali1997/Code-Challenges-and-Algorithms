# Write here the code challenge solution

class MyQueue:

    def __init__(self):
        self.front = []
        self.rear = []

    def push(self, x):
        self.front.append(x)
        
    def pop(self):
        self.peek()
        return self.rear.pop()

    def peek(self):
        if len(self.rear) == 0:
            while self.front:
                self.rear.append(self.front.pop())
        return self.rear[-1]

    def empty(self):
        return len(self.rear) + len(self.front) == 0

        

if __name__ == '__main__':


    myQueue = MyQueue()
    myQueue.push(1) # queue is: [1]
    myQueue.push(2) # queue is: [1, 2] (leftmost is front of the queue)
    print(myQueue.peek()) # return 1
    print(myQueue.pop()) # return 1, queue is [2]
    print(myQueue.empty()) # return false
    myQueue.push(3) 
    print(myQueue.peek()) 
    print(myQueue.pop()) 
    print(myQueue.pop()) 
    print(myQueue.empty())
   