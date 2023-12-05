import random
from ctypes import cdll, c_bool, c_float, c_int, pointer, POINTER, Structure


class CTreeNode(Structure):
    pass


CTreeNode._fields_ = [("key", c_int),
                      ("value", c_float),
                      ("left", POINTER(CTreeNode)),
                      ("right", POINTER(CTreeNode))]


class CTree:

    code = None

    def __init__(self):
        if CTree.code is None:
            CTree.code = cdll.LoadLibrary("libtree.dll")
            CTree.code.insert.argtypes = [POINTER(CTreeNode), c_int, c_float]
            CTree.code.insert.restype = POINTER(CTreeNode)
            CTree.code.search.argtypes = [POINTER(CTreeNode),
                                          c_int, POINTER(c_float)]
            CTree.code.search.restype = c_bool
            CTree.code.destroy.argtypes = [POINTER(CTreeNode)]
        self.root = POINTER(CTreeNode)()

    def search(self, key):
        pass

    def insert(self, key, value):
        pass

    def __str__(self):
        pass

    def __del__(self):
        CTree.code.destroy(self.root)


class Node:

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.right = None
        self.left = None

    def search(self, key):
        if self.key == key:
            return self.value
        elif (self.key < key) and (not self.right == None):
            return self.right.search(key)
        elif (self.key > key) and (not self.left == None):
            return self.left.search(key)
        
        return None

    def insert(self, key, value):
        if self.key == key:
            self.value = value
        elif (self.key < key) and (self.right == None):
            self.right = Node(key, value)
        elif (self.key > key) and (self.left == None):
            self.left = Node(key, value)
        elif (self.key < key) and (not self.right == None):
            self.right.insert(key, value)
        elif (self.key > key) and (not self.left == None):
            self.left.insert(key, value)

    def __str__(self):
        return f"({self.key} {self.left} {self.right})"


class BinarySearchTree:

    def __init__(self):
        self.root = None

    def search(self, key):
        if not self.root is None:
            return self.root.search(key)
        
        return None

    def insert(self, key, value):
        if not self.root is None:
            self.root.insert(key, value)
        else:
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
    # cbst = CTree()
    # for i in range(0, 20):
    #     cbst.insert(random.randint(0, 30), random.random())
    # for i in range(0, 10):
    #     k = random.randint(0, 30)
    #     print(f"Searching for {k}: {cbst.search(k)}")
    # print(cbst)
