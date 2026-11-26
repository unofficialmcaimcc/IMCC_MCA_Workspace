# circular queue

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
     
        if self.rear:
            # assigning rear node's next to point to new node
            self.rear.next = node
            # re-assigning rear node to be new node so now previous rear node's next is this new rear node
            self.rear = node
        else:
            self.front = self.rear = node
        self.rear.next = self.front # this line creates a link between last node and first node


    def dequeue(self):
        # check if self.front exists 
        if self.front:
            if self.front is self.rear:
                self.front = self.rear = None
                print("now queue empty")
                return
            self.front = self.front.next
            self.rear.next = self.front

            
        else:
            print("queue empty")

    def traverse(self):
        curr = self.front
        if curr is None:
            print("queue empty")
        else:
            while True:
                print(curr.data, end = " -> ")
                curr = curr.next
                if curr is self.front:
                    break
            print("None")

q = linear_queue()

q.enqueue(node(0))
q.enqueue(node(1))
q.enqueue(node(2))
q.enqueue(node(3))
q.enqueue(node(4))

q.traverse()
q.dequeue()
q.traverse()
q.dequeue()
q.traverse()
q.dequeue()
q.traverse()
q.dequeue()