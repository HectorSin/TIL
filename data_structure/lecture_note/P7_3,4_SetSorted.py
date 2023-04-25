# Set.
class Set:
    def __init__( self ):
        self.items = []

    def size( self ):
       return len(self.items)

    def contains(self, item) :      # O(n)
       return item in self.items

    def insert(self, elem) :        # O(n)  --> 수정 --> 여전히 O(n)
        if elem in self.items : return      # 이미 있음
        for idx in range(len(self.items)) : # loop: n번
            if elem < self.items[idx] :     # idx위치에 삽입
                self.items.insert(idx, elem)
                return;
        self.items.append(elem)             # 맨 뒤에 삽입

    def delete(self, elem) :        # O(n)
       self.items.remove(elem)

    def __eq__( self, setB ):       # O(mn) ---> O(n+m)
        if self.size() != setB.size() :
            return False
        for idx in range(len(self.items)) : # loop: n번
            if self.items[idx] != setB.items[idx] :
                return False
        return True

    def union( self, setB ):        # O(mn) ---> O(n+m)
        newSet = Set()
        a = 0
        b = 0
        while a < len( self.items ) and b < len( setB.items ) :
            valueA = self.items[a]
            valueB = setB.items[b]
            if valueA < valueB :
                newSet.items.append( valueA )
                a += 1
            elif valueA > valueB :
                newSet.items.append( valueB )
                b += 1
            else : # Only one of the two duplicates are appended.
                newSet.items.append( valueA )
                a += 1
                b += 1

        while a < len( self.items ) :
             newSet.items.append( self.items[a] )
             a += 1
        while b < len( setB.items) :
             newSet.items.append( setB.items[b] )
             b += 1

        return newSet

#P7_3 -------------------
    def intersect( self, setB ):        # O(mn) ---> O(n+m)
        newSet = Set()
        a = 0
        b = 0
        while a < len( self.items ) and b < len( setB.items ) :
            valueA = self.items[a]
            valueB = setB.items[b]
            if valueA < valueB :
                a += 1
            elif valueA > valueB :
                b += 1
            else : # Only one of the two duplicates are appended.
                newSet.items.append( valueA )
                a += 1
                b += 1

        return newSet

#P7_4 -------------------
    def difference( self, setB ):        # O(mn) ---> O(n+m)
        newSet = Set()
        a = 0
        b = 0
        while a < len( self.items ) and b < len( setB.items ) :
            valueA = self.items[a]
            valueB = setB.items[b]
            if valueA < valueB :
                newSet.items.append( valueA )
                a += 1
            elif valueA > valueB :
                b += 1
            else : # Only one of the two duplicates are appended.
                a += 1
                b += 1

        while a < len( self.items ) :
             newSet.items.append( self.items[a] )
             a += 1

        return newSet
#------------------------

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
setA.display('Set A:')
setB.display('Set B:')

setA.union(setB).display('A U B:')
setA.intersect(setB).display('A ^ B:')
setA.difference(setB).display('A - B:')
