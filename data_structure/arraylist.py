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