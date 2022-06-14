# tree can be build with with a form of LinkedList

# Terminologies
# Full tree: every node point to 0 or 2 nodes
# perfect tree: in every level in the tree is filled
# complete tree: filling the tree from left to right without gap


# build a binary tree
# bst = divide and conquere
# number of nodes = 2^n - 1 where n is level
# lookup, insert, remove: O(log n)
# technically the worst case is O(n); n is # of nodes 
# when adding 80 to a bst: (10)-(20)-(30)-(40)-(insert)
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def print_bst(self):
        temp = self.root
        while temp is not None:
            print(temp.left.value)
            temp = temp.left

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        while True:
            if value == temp.value:
                return False
            if value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right

    def contains(self, value):
        # not neccessary
        # if self.root is None:
        #     return False
        temp = self.root
        while temp is not None:
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True
        return False

    def minimum_value(self, current_node):
        while current_node.left is not None:
            current_node = current_node.left
        return current_node

    # Tree Traversal: different ways to visit every node in a tree
    # BFS
    # DFS: pre-order
    # DFS: post-order
    # DFS: in-order


    def BFS(self):
        queue = []
        visit = []
        queue.append(self.root)
        while len(queue) > 0:
            current_node = queue.pop(0)
            visit.append(current_node.value)
            if current_node.left is not None:
                queue.append(current_node.left)
            if current_node.right is not None:
                queue.append(current_node.right)
        return visit        

    def dfs_pre_order(self):
        visit = []
        def traverse(current_node):
            visit.append(current_node.value)       
            if current_node.left is not None:
                traverse(current_node.left)
            if current_node.right is not None:
                traverse(current_node.right)
        traverse(self.root)
        return visit

    def dfs_post_order(self):
        visit = []
        def traverse(current_node):
            if current_node.left is not None:
                traverse(current_node.left)
            if current_node.right is not None:
                traverse(current_node.right)
            visit.append(current_node.value)       
        traverse(self.root)
        return visit

    def dfs_in_order(self):
        visit = []
        def traverse(current_node):
            if current_node.left is not None:
                traverse(current_node.left)
            visit.append(current_node.value)           
            if current_node.right is not None:
                traverse(current_node.right)
        traverse(self.root)
        return visit
  
# test 
# bst = BinarySearchTree()
# bst.insert(47)
# bst.insert(21)
# bst.insert(76)
# bst.insert(18)
# bst.insert(27)
# bst.insert(52)
# bst.insert(82)

# print(bst.root.value)
# print(bst.root.left.value)
# print(bst.root.right.value)
# print(bst.contains(21))
# print(bst.contains(20))
# print(bst.minimum_value(bst.root.left))

# tree traversal
# print(bst.BFS())
# print(bst.dfs_pre_order())
# print(bst.dfs_post_order())
# print(bst.dfs_in_order())


