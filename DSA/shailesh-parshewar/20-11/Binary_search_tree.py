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
                
    def traverse_inorder(self):
        if self.empty():
            print("bst empty")
        else:
           
            self.inorder(self.root)

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

bt = BST()


bt.addNodeUsingRecursion(10)
bt.addNodeUsingRecursion(15)
bt.addNodeUsingRecursion(13)
bt.addNodeUsingRecursion(9)
bt.addNodeUsingRecursion(8)
bt.addNodeUsingRecursion(5)
bt.addNodeUsingRecursion(2)
bt.addNodeUsingRecursion(300)

# bt.traverse_inorder()
# print("-"*24)
# bt.traverse_preorder()
# print("-"*24)
# bt.traverse_postorder()

bt.minimum_node(bt.root)
bt.maximum_node(bt.root)