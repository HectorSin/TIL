# 리스트
class ArrayList:
    def __init__(self):
        self.items = []

    def insert(self, pos, elem):
        self.items.insert(pos, elem)
    
    def delete(self, pos):
        return self.items.pop(pos)

    def isEmpty(self):
        return self.size()==0
    
    def getEntry(self,pos):
        return self.items[pos]
    
    def size(self):
        return len(self.items)
    
    def clear(self):
        self.items = []

    def find(self, item):
        return self.items.index(item)
    
    def replace(self, pos, elem):
        self.items[pos] = elem

    def sort(self):
        self.items.sort()

    def merge(self, lst):
        self.items.extend(lst)

    def display(self, msg="ArrayList: "):
        print(msg, '')

# 원형 큐
class CircularQueue:
    def __init__(self, SIZE):
        self.front = 0
        self.rear = 0
        self.items = [None] * SIZE
    def isEmpty(self): return self.front == self.rear
    def isFull(self, SIZE): return self.front == (self.rear+1)%SIZE
    def clear(self): self.front = self.rear

    def enqueue(self,item,SIZE):
        if not self.isFull():
            self.rear = (self.rear+1)%SIZE
            self.items[self.rear] = item

    def dequeue(self,SIZE):
        if not self.isEmpty():
            self.front = (self.front+1)%SIZE
            return self.items[self.front]
        
    def peek(self,SIZE):
        if not self.isEmpty():
            self.front = (self.front+1)%SIZE
            return self.items[self.front]
        
    def peek(self,SIZE):
        if not self.isEmpty():
            return self.items[(self.front +1) % SIZE]
        
    def size(self,SIZE):
        return(self.rear - self.front + SIZE) % SIZE
    
    def display(self,SIZE):
        out = []
        if self.front < self.rear:
            out = self.items[self.front+1:self.rear+1]
        else:
            out = self.items[self.front+1:SIZE] + self.items[0:self.rear+1]
        print("[f=%s,r=%d] ==> "%(self.front, self.rear), out)

# 리스트를 활용한 우선순위 큐 구현
class PriorityQueue:
    def __init__(self):
        self.queue = []
        
    def push(self, item, priority):
        # 삽입할 아이템과 우선순위를 함께 저장한다.
        # 우선순위가 높을수록 먼저 처리된다.
        self.queue.append((item, priority))
        
    def pop(self):
        if len(self.queue) == 0:
            return None
        
        # 우선순위가 가장 높은 아이템을 찾는다.
        max_index = 0
        for i in range(1, len(self.queue)):
            if self.queue[i][1] > self.queue[max_index][1]:
                max_index = i
                
        # 우선순위가 가장 높은 아이템을 반환하고, 큐에서 제거한다.
        item = self.queue[max_index][0]
        del self.queue[max_index]
        return item

# 힙을 활용해 우선순위 큐 구현
import heapq

class PriorityQueue:
    def __init__(self):
        self.queue = []
        self.index = 0
        
    def push(self, item, priority):
        # 삽입할 아이템과 우선순위를 함께 저장한다.
        # 우선순위가 높을수록 먼저 처리된다.
        heapq.heappush(self.queue, (-priority, self.index, item))
        self.index += 1
        
    def pop(self):
        if len(self.queue) == 0:
            return None
        
        # 우선순위가 가장 높은 아이템을 반환하고, 큐에서 제거한다.
        priority, index, item = heapq.heappop(self.queue)
        return item
