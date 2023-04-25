# Linked Queue.
class Node:
    def __init__ (self, elem, next):
        self.data = elem 
        self.link = next

class LinkedQueue:
    def __init__( self ):
        self.front = None
        self.rear = None

    def isEmpty( self ): return self.front == None

    def enqueue( self, item ):
        if( self.isEmpty()):
            self.front = self.rear = Node(item, None)
        else :
            self.rear.link = Node(item, None)
            self.rear = self.rear.link

    def peek( self ):
        if not self.isEmpty():
            return self.front.data

    def dequeue( self ):
        if not self.isEmpty():
            data = self.front.data
            self.front = self.front.link
            return data

    def print( self, msg='LinkedQueue:' ):
        print(msg, end='')
        node = self.front
        while not node == None :
            print(node.data, end=' ')
            node = node.link
        print()

#======================================================================
def testLinkedQueue() :
    print('연결된 구조의 큐 구현\n')
    queue = LinkedQueue()
    for i in range(10):
        queue.enqueue(i)
    queue.print('큐 enqueue 9회:')
    print('\tdequeue() --> ', queue.dequeue())
    print('\tdequeue() --> ', queue.dequeue())
    print('\tdequeue() --> ', queue.dequeue())
    queue.print('큐 dequeue 3회:')

    queue.enqueue('홍길동')
    queue.enqueue('이순신')
    queue.enqueue('김연아')
    queue.enqueue('황희')
    queue.print('큐 enqueue 4회:')
    print('\tdequeue() --> ', queue.dequeue())
    queue.print('큐 dequeue 1회:')
    print('\tpeek()--> ', queue.peek())

testLinkedQueue()
