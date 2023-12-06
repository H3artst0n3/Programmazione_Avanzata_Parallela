import random
from ctypes import cdll, c_bool, c_float, c_int, pointer, POINTER, Structure


class CTreeNode(Structure):
    # this must be empty
    pass


CTreeNode._fields_ = [("key", c_int),
                      ("value", c_float),
                      ("left", POINTER(CTreeNode)),
                      ("right", POINTER(CTreeNode))]


class CTree:

    code = None

    def __init__(self):
        # if we don't have a tree then initialize it
        if CTree.code is None:
            # import the C library
            CTree.code = cdll.LoadLibrary("./libtree.dll")
            # we have to define the types of the parameters of insert
            CTree.code.insert.argtypes = [POINTER(CTreeNode), c_int, c_float]
            # we have to define the type of the value returned by insert
            CTree.code.insert.restype = POINTER(CTreeNode)
            # we have to define the types of the parameters of search
            CTree.code.search.argtypes = [POINTER(CTreeNode), c_int, POINTER(c_float)]
            # we have to define the type of the value returned by search
            CTree.code.search.restype = c_bool
            # we have to define the types of the parameters of destroy
            CTree.code.destroy.argtypes = [POINTER(CTreeNode)]
        # if we have a root set it like a pointer
        self.root = POINTER(CTreeNode)()

    def search(self, key):
        # ??
        res = c_float()
        # ??
        found = CTree.code.search(self.root, c_int(key), pointer(res))
        # if found = True
        if found: 
            # return the value
            return res.value
        
        # if we didn't find the key return None
        return None
    
    def insert(self, key, value):
        # insert the value and the key in the right subtree
        self.root = CTree.code.insert(self.root, c_int(key), c_float(value))

    def __str__(self):
        def print_node(node):
            if not node:
                return "None"
            s = f"{node.contents.key}"
            if node.contents.left or node.contents.right:
                left = print_node(node.contents.left)
                right = print_node(node.contents.right)
                s = f"({s} {left} {right})"
            return s
        
        return print_node(self.root)
    
    def __del__(self):
        CTree.code.destroy(self.root)


class Node:

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.right = None
        self.left = None

    def search(self, key):
        # check if the key is in the current node
        if self.key == key:
            return self.value # return the value of the key
        
        # go right and check if we have a child or a None value
        if (self.key < key) and (self.right is not None):
            return self.right.search(key)
        
        # go left and check if we have a child or a None value
        if (self.key > key) and (self.left is not None):
            return self.left.search(key)
        
        return None

    def insert(self, key, value):
        # if the key is already in the current node
        if self.key == key:
            self.value = value # assign the new value
        
        # go right
        if self.key < key:
            # if there is no child initialize a new node
            if self.right is None:
                self.right = Node(key, value)
            else: # call insert on the right child
                self.right.insert(key, value) 
        
        # go left
        if self.key > key:
            # if there is no child initialize a new node
            if self.left is None:
                self.left = Node(key, value)
            else: # call insert on the left child
                self.left.insert(key, value)

    def __str__(self):
        s = f"{self.key}"
        if self.right is not None or self.left is not None:
            s = f"({s} {str(self.left)} {str(self.right)})"
        return s


class BinarySearchTree:

    def __init__(self):
        self.root = None

    def search(self, key):
        # if we have a root do the search
        if self.root is not None:
            return self.root.search(key)
        
        return None

    def insert(self, key, value):
        # if we have a root do the insert
        if self.root is not None:
            self.root.insert(key, value)
        else: # if we don't have a root initialize it like a Node with the key and value of the insert function
            self.root = Node(key, value)

    def __str__(self):
        return str(self.root)


if __name__ == "__main__":
    bst = BinarySearchTree()
    for i in range(0, 20):
        bst.insert(random.randint(0, 30), random.random())
    for i in range(0, 10):
        k = random.randint(0, 30)
        print(f"Searching for {k}: {bst.search(k)}")
    print(bst)

    # Decommentare per la parte extra
    cbst = CTree()
    for i in range(0, 20):
        cbst.insert(random.randint(0, 30), random.random())
    for i in range(0, 10):
        k = random.randint(0, 30)
        print(f"Searching for {k}: {cbst.search(k)}")
    print(cbst)
