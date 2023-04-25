# Set.
class Set:
    def __init__( self ):
        self.items = []

    def size( self ):
        return len(self.items)

    def contains(self, item) :
#       return item in self.items
# P3.3(1)
        for i in range(len(self.items)) :   # len(self.items) -> self.size()
            if self.items[i] == item :
                return True
        return False

    def insert(self, elem) :
#        if elem not in self.items :
# P3.3(3)
        if self.contains(elem) == False :
           self.items.append(elem)

    def delete(self, elem) :
#        if elem in self.items :
#            self.items.remove(elem)
# P3.3(2)
        for i in range(len(self.items)) :
            if self.items[i] == elem :
                self.items.pop(i)
	        return
    
    def union( self, setB ):                # C = self U  B
        newSet = Set()
        newSet.items = list(self.items)
        for elem in setB.items :
#            if elem not in self.items :
# P3.3(3)
            if not self.contains(elem) :
                newSet.items.append(elem)
        return newSet

    def intersect( self, setB ):            # C = self ∩ B
        setC = Set()
        for elem in setB.items :
#            if elem in self.items :
# P3.3(3)
            if self.contains(elem) :
                setC.items.append(elem)
        return setC

    def difference( self, setB ):           # C = self - B
        setC = Set()
        for elem in self.items:
#            if elem not in setB.items:
# P3.3(3)
            if not setB.contains(elem) :  # not True = False
                setC.items.append(elem)
        return setC

# P3.3(4)
    def __sub__( self, setB ):           # C = self - B
        return self.difference(setB)

# P3.3(5)
    def isSubsetOf( self, setB ):
        for elem in self.items :
            if elem not in setB : return False
        return True

    def display(self, msg):
        print(msg, self.items)

#======================================================================
setA = Set()
setA.insert('휴대폰')
setA.insert('지갑')
setA.insert('손수건')
setA.display('Set A:')

setB = Set()
setB .insert('빗')
setB .insert('파이썬 자료구조')
setB .insert('야구공')
setB .insert('지갑')
setB.display('Set B:')

setB.insert('빗')
setA.delete('손수건')
setA.delete('발수건')
setA.display('Set A:')
setB.display('Set B:')

setA.union(setB).display('A U B:')
setA.intersect(setB).display('A ∩ B:')
setA.difference(setB).display('A - B:')
(setA-setB).display('A - B:')

