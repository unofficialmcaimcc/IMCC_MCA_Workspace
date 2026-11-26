
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class Linked_list:
    def __init__(self):
        self.head = None
    def empty(self):
        self.head = None

    def append(self, node):
        # check if linked list is empty
        if not self.head:
            self.head = node

        # linked list is not empty here
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
                
            # appending node to last by adding temp.next to be node  and node.prev to be temp
            temp.next = node
            node.prev = temp

    def traverse(self):
        # first check if the linked list is empty
        if not self.head:
            print("Empty linked list")
        temp = self.head
        # linked list is not empty and we have assigned temp to be self.head
        while temp:
            print("node : ", temp.data)
            temp = temp.next
            
        print("traversal complete")

    def insert(self, node, pos):    
        # 0 position will be treated as invalid
        if pos == 0:
            print("invalid address: list indexing not allowed, posistion has to be at least 1")
            return
        elif pos == 1:
            node.next = self.head
            self.head.prev = node
            self.head = node
        else:
            p = 1
            temp = self.head
            while p != pos -1 and temp.next:
                temp = temp.next
                p+=1
            if temp.next:
                temp.next.prev = node
            node.prev = temp
            node.next = temp.next
            temp.next = node

    def delete_node(self, value):

        temp = self.head
        if temp.data == value:
            self.head = self.head.next
            self.head.prev = None
        else:
            # iterate while temp exists and temp.data is not equal to value

            while temp.data != value and temp:
                # move temp to its next node
                temp = temp.next
                # if the next node is None then that means we are at end of list
                if not temp:
                    print("value is not present in linked list")
                    return
                
            # we found our node, so we assign its previous node's next to be temp's next skipping temp 
            temp.prev.next = temp.next

            if temp.next: # not last node
                # we will assign temp's next node's prev to be temp's prev skipping temp again
                temp.next.prev = temp.prev

            temp = None

        pass

    def traverse_in_reverse(self):
        temp = self.head
        while temp.next:
            temp = temp.next
        
        while temp:
            print("node: ", temp.data)
            temp = temp.prev

    def count_occurance_of_value(self, value):
        temp = self.head
        count = 0
        while temp.next:
            if temp.data == value:
                count +=1
            temp = temp.next
        print("value: ", value, "appears ", count)
li = Linked_list()

li.append(Node(1))
li.append(Node(2))
li.append(Node(3))
li.append(Node(4))
li.append(Node(5))
li.append(Node(6))
li.append(Node(7))
li.append(Node(8))

li.insert(Node(99), 1)
li.insert(Node(98), 1)
li.insert(Node(99), 6)
li.insert(Node(990), 56)
li.count_occurance_of_value(99)

li.traverse_in_reverse()