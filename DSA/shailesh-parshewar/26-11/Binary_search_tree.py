# BST: Binary Search Tree is a data structure where each root node has zero to at most 2 child nodes and the left node is always less than root node, right node is always greater than root node.\


# example BST:

#            10
#      4              27
#   2     7      14      30
# 1   3 6   8  11  17  29   31
# 

# traversal in BST:
# 1. InOrder : leftNode - Root - RightNode
#       gives you list in ascending order since it visits left-most node first
#       sample output: 1, 2, 3, 4, 6, 7, 8, 10, 11, 14, 17, 27, 29, 30, 31
# 
# 2. PreOrder : Root - leftNode - RightNode
#       gives you a list of descending order in chunks (not fully descending ordered list) depending on BST structure.
#       sample output: 27, 4, 
# 
# 3. PostOrder : leftNode - RightNode - Root


# example exercise :
#  75, 34, 45, 62, 22, 96, 82, 105, 98, 25
# output BST:

#                              75
#            34                                 96
#      22           45                  82              105
#           25            62                          98
#   

# in order: 
#       output: 22, 25, 34, 45, 62, 75, 82, 96, 98, 105
# pre order:
#       output: 75, 34, 22, 25, 45, 62, 96, 82, 105, 98
# post order:
#       output: 25, 22, 62, 45, 34, 82, 98, 105, 96, 75


# example 2:
# in order: 3, 5, 8, 15, 20, 24, 37, 50, 58, 60, 62, 91
# post order: 3, 8, 5, 24, 37, 20, 15, 60, 58, 91, 62, 50 
# output BST: 
#                                   50
#             (3,5,8,15,20,24,37)           (58,60,62,91)
#                     15                         62
#           (3,5,8)      (20,24,37)     (60,58)          91
#              5             20          58
#           3    8              (24,37)         60
#                                  37
#                               24
# ---------------------------------------------------------------------------------

# BST code
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def addLeft(self, data):
        self.left = node(data)
    def addRight(self, data):
        self.right = node(data)



class BST:
    def __init__(self):
        self.root = None
    cnt = 0

    def empty(self):
        return self.root == None
    
    def addNodeUsingRecursion(self, data):
        # check if the BST is empty and assigns the current data as a node to it if so
        if self.empty():
            self.root = node(data)
        else:
            
            self.checkForSpot(self.root, data)

    def addNodeUsingLoop(self, data):
        if self.empty():
            self.root = node(data)
        else:
            temp = self.root
            while True:
                if data < temp.data:
                    if temp.left is None:
                        temp.left = node(data)
                        return
                    else:
                        temp = temp.left
                else:
                    if temp.right is None:
                        temp.right = node(data)
                        return
                    else:
                        temp = temp.right

    
    def checkForSpot(self, curr_node: node, data):
        # checking if the new data is larger than current node's data
        if curr_node.data < data:
            if curr_node.right: # check if right node exists, if yes we want to perform the same check starting from right node as current node
                self.checkForSpot(curr_node.right, data)
            else: # since right node doesn't exist I can just assign new data to it as a new node
                curr_node.addRight(data)
        else: # data here is less than current node's data
            if curr_node.left: # check if left node exists. if yes we want to perform the same check starting from left node as current node
                self.checkForSpot(curr_node.left, data)
            else: # since left node doesn't exist I can just assign new data to it as a new node
                curr_node.addLeft(data)

    def inorder(self, curr_node: node, level = 0):
            
            if curr_node is None:
                return
            else:
                level += 1
                self.inorder(curr_node.left, level)
                level -= 1
                print(f"data : {curr_node.data}, level : {level}")
                level +=1
                self.inorder(curr_node.right, level)
                level -=1

    def count(self, curr_node):
        if self.empty():
            return
        else:
            if curr_node is None:
                return
            else:
                self.count(curr_node.left)
                self.node_count +=1
                self.count()
            

    def count_leaf_nodes(self, curr_node):
        if curr_node is None:
            return 0
        if curr_node.left is None and curr_node.right is None:
            return 1
        return self.count_leaf_nodes(curr_node.left) + self.count_leaf_nodes(curr_node.right)


    # this implementation is wrong
    def count_nonLeaf_nodes(self, curr_node): 
        if curr_node is None:
            return 0
        if curr_node.left is not None or curr_node.right is not None:
            return self.count_nonLeaf_nodes(curr_node.left) + self.count_nonLeaf_nodes(curr_node.right)
        return 1



    def traverse_inorder(self):
        if self.empty():
            print("bst empty")
        else:
           
            print(self.inorder(self.root, 0))

    def preorder(self, curr_node, level = 0):
        if curr_node is None:
                return
        else:
            print(f"data : {curr_node.data}, level : {level}")
            level += 1
            self.preorder(curr_node.left, level)
            level -= 1
            level +=1
            self.preorder(curr_node.right, level)
            level -=1

    def traverse_preorder(self):
        if self.empty():
                print("bst empty")
        else:                   
            self.preorder(self.root)

    def postorder(self, curr_node, level = 0):
        if curr_node is None:
                return
        else:
            level += 1
            self.postorder(curr_node.left, level)
            level -= 1
            level +=1
            self.postorder(curr_node.right, level)
            level -=1
            print(f"data : {curr_node.data}, level : {level}")
    def traverse_postorder(self):
        if self.empty():
                print("bst empty")
        else:                   
            self.postorder(self.root)

    def minimum_node(self, curr_node: node):
        if curr_node.left is None:
            print("minimum node value : ", curr_node.data)
        else:
            self.minimum_node(curr_node.left)

    def maximum_node(self, curr_node: node):
        if curr_node.right is None:
            print("maximum node value : ", curr_node.data)
        else:
            self.maximum_node(curr_node.right)


    def delete_node(self, curr_node, data):
        # this if elif will run as long as node value is not found while making appropriate nudges along the next path 
        if curr_node.data > data:
            curr_node.left = self.delete_node(curr_node.left, data)
        elif curr_node.data < data:
            curr_node.right = self.delete_node(curr_node.right, data)
        else:
            # here we have found the right node in this block
            if curr_node.left is None:  # if node has no left child we return right child
                return curr_node.right
            elif curr_node.right is None: # if node has no right child we return left child
                return curr_node.left


        successor = self.get_succesor(curr_node)
        curr_node.data = successor.data
        curr_node.right = self.delete_node(curr_node.right, successor.data)
        return curr_node


    def get_succesor(self, curr_node):
       
        while curr_node is not None and curr_node.left is not None:
            curr_node = curr_node.left

        return curr_node

    # this method could also be called as 'exists' since it checks if node exists
    def search(self, key):
        temp = self.root

        while temp:
            if temp.data == key:
                return True
            elif temp.data > key:
                temp = temp.left
            else:
                temp = temp.right
        return False

    def level_order_traversal(self):
        if self.empty():
            print("BST is empty")
            return

        # traversal array will keep track of all node visited in loop iterations
        traversal_array = []
        # adding root node as a starting point
        traversal_array.append(self.root)

        # count will keep track of which node to process as it fills
        # acts as the index for traversal_array in loop body
        count  = 0
        # while count is less than arr length, which means we still have some elements left to visit
        while count < len(traversal_array):
            # getting a temp node from traversal_array using count as index
            temp =  traversal_array[count]
            # since we can treat this node as visited, we can increase count by one to get next node in next iteration
            count +=1
            # if the node exists we want to print its data and add its direct child node as next element
            if temp:
                print(temp.data, end = " ")
                if temp.left:
                    traversal_array.append(temp.left)
                if temp.right:
                    traversal_array.append(temp.right)

            # if temp node is None just print it and move on
            else:
                print(None, end= " ")

  


bt = BST()

bt.addNodeUsingRecursion(0)
bt.addNodeUsingRecursion(1)
bt.addNodeUsingRecursion(2)
bt.addNodeUsingRecursion(-1)
bt.addNodeUsingRecursion(-3)
bt.addNodeUsingRecursion(-6)
bt.addNodeUsingRecursion(-7)
bt.addNodeUsingRecursion(-2)

bt.traverse_inorder()
print("count : ", bt.count_leaf_nodes(bt.root))

bt.level_order_traversal()

