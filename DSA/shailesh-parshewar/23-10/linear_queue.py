# linear queue

class node:
    def __init__(self, value):
        self.data = value
        self.next = None

class linear_queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, node):
        if not self.front and not self.rear:
            self.front = self.rear = node

        else:
            # assigning rear node's next to point to new node
            self.rear.next = node
            # re-assigning rear node to be new node so now previous rear node's next is this new rear node
            self.rear = node
    def dequeue(self):
        # check if self.front exists 
        if self.front:
            temp = self.front
            self.front = self.front.next
            # we check if new self.front is none that means we have an empty queue and so we also have to update self.rear to be also None so it doesn't point to deleted node
            if self.front is None:
                self.rear = None
            temp = None
        else:
            print("queue empty")

    def traverse(self):
        temp = self.front
        if temp is None:
            print("queue empty")
        else:
            while temp:
                print(temp.data, end = " -> ")
                temp = temp.next
            print("None")

q = linear_queue()

q.enqueue(node(0))
q.enqueue(node(1))
q.enqueue(node(2))
q.enqueue(node(3))
q.enqueue(node(4))

q.traverse()
q.dequeue()
q.dequeue()
q.dequeue()
q.dequeue()
q.dequeue()
q.traverse()