# Write your test here
from challenge01 import MyQueue

# push test
def test_push():
    q = MyQueue()
    q.push(1)
    q.push(2)
    q.push(3)
    assert q.get_queue()==[1,2,3]    
    q.push(7)
    q.push(8)
    q.push(9)
    assert q.get_queue()==[1,2,3,7,8,9]
#  pop test
def test_pop():
    q = MyQueue()
    q.push(1)
    q.push(2)
    q.push(3)
    q.pop()
    assert q.get_queue()==[2,3]    
    q.push(7)
    q.push(8)
    q.push(9)
    q.pop()
    assert q.get_queue()==[3,7,8,9]

#  peek test
def test_peek():
    q = MyQueue()
    q.push(1)
    q.push(2)
    q.peek()
    assert q.get_queue()==[1,2]

# is empty test
def test_is_empty():
    q = MyQueue()
    assert q.is_empty()==True
    q.push(1)
    assert q.is_empty()==False


