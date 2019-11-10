class Queue:
    def __init__(self):
        self.items = []

    def insert(self,item):
        self.items.append(item)

    def __delete__(self):
        return self.items.pop(0)