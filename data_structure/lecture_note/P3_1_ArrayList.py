# Linked List.
class ArrayList:
    def __init__( self ):
        self.items = []

#    def insert(self, pos, elem) : self.items.insert(pos, elem)
# P3.1(1)
    def insert(self, pos, elem) :
        self.items.append(elem)
        # pos 위치부터 뒤로 복사해 밀기
        for i in range(len(self.items)-2, pos-1, -1) :
            self.items[i+1] = self.items[i]
        # pos 위치에 원하는 데이터 덮어씌우기
        self.items[pos] = elem

#    def delete(self, pos) : self.items.pop(pos)
# P3.1(2)
    def delete(self, pos):
        # pos위치까지 데이터를 땡겨서 덮어 씌우기
        for i in range(pos, len(self.items)-1):
            self.items[i] = self.items[i+1]
        # 마지막 남은 데이터 삭제
        self.items.pop(-1)

    def size( self ): return len(self.items)
    def isEmpty( self ): return self.size() == 0   
    def getEntry(self, pos) : return self.items[pos]
   
    def clear( self ) : self.items = []
#    def find(self, item) : return self.items.index(item)
# P3.1(3)
    def find(self, item) :
        for i in range(self.size()):
            if item == self.items[i] : return i

    def replace(self, pos, elem) : self.items[pos] = elem
    def sort(self) : self.items.sort()
#    def merge(self, lst) : self.items.extend(lst)
# P3.1(4) 리스트 덧셈 사용
    def merge(self, lst) :
        self.items += lst
    def display(self, msg='ArrayList:' ):
        print(msg, '항목수=', self.size(), self.items)

s = ArrayList()
s.display('파이썬 리스트로 구현한 리스트 테스트')
s.insert(0, 10)
s.insert(0, 20)
s.insert(1, 30)
s.insert(s.size(), 40)
s.insert(2, 50)
s.display("파이썬 리스트로 구현한 List(삽입x5): ")
s.sort()
s.display("파이썬 리스트로 구현한 List(정렬후): ")
s.replace(2, 90)
s.display("파이썬 리스트로 구현한 List(교체x1): ")

print("find 90 pos: ", s.find(90))
print("find 15 pos: ", s.find(15))

s.delete(2);	s.delete(s.size() - 1);	s.delete(0)
s.display("파이썬 리스트로 구현한 List(삭제x3): ")
lst = [ 1, 2, 3 ]
s.merge(lst)
s.display("파이썬 리스트로 구현한 List(병합+3): ")
s.clear()
s.display("파이썬 리스트로 구현한 List(정리후): ")


