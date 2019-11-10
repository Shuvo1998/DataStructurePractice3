class Queue:
    def __init__(self):
        self.items = []

    def insert(self):
        item = input()
        self.items.append(item)

    def delete(self):
        return self.items.pop(0)

    def is__empty(self):
        if self.items == []:
            return True
        return False


if __name__ == "__main__":
    q = Queue()
    for i in range(5):
        q.insert()

    while not q.is_empty():
        deleted  = q.delete()
        print(deleted)

