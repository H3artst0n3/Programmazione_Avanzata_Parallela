class Queue:

    def __init__(self):
        self.data = []

    def add(self, x):
        self.data.append(x)

    def remove(self):
        x = self.data[0]
        self.data = self.data[1:]
        return x

    def empty(self):
        return self.data == []

class Stack():

    def __init__(self):
        self.data = []

    def inserisci(self, x):
        # self.data = [x] + self.data
        self.data.append(x)
        return x

    def rimuovi(self):
        # x = self.data[0]
        # self.data = self.data[1:]
        x = self.data[-1]
        self.data = self.data[:-1]
        return x

    def isempty(self):
        return self.data == []

q1 = Queue()
q2 = Queue()

# q1.add(3)
# q1.add(4)

# q2.add(1)

# print(q2.remove())

# while (not q1.empty()):
#     print(q1.remove())

s1 = Stack()

for i in range(10):
    print(f"inserisco: {s1.inserisci(i)}")

while (not s1.isempty()):
    print(f"rimuovo: {s1.rimuovi()}")