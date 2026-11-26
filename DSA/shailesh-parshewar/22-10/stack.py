

class node:
    def __init__(self, value):
        self.data = value
        self.next = None


class stack:
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top is None

    def push(self, node):
        # node.next points to previous self.top which holds address of previous top node
        # like a reversed linked list where the first node is top node
        node.next = self.top
        self.top = node

    def pop(self):
        if self.is_empty():
            print("empty stack")

        else:
            self.top = self.top.next


    def peek(self):
        if self.is_empty():
            print("stack empty")
        else:
            print("top node data : ", self.top.data)
    def reverse_stack(self):
        stk = stack()
        temp = self.top
        while temp:
            stk.push(node(temp.data))
            temp = temp.next
        return  stk

stk = stack()

stk.push(node(0))
stk.push(node(1))
stk.push(node(2))
stk.push(node(3))
stk.push(node(4))
stk.push(node(5))
stk.push(node(6))
stk.push(node(7))

stk.peek()

st1 = stk.reverse_stack()

st1.peek()