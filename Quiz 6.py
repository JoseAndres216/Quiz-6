class Node:
    data = None
    left = None
    right = None

    def __init__(self, data):
        self.right = None
        self.left = None
        self.data = data
        return

    def setLeft(self, left):
        self.left = left
        return

    def setRight(self, right):
        self.right = right
        return

    def setdata(self, data):
        self.data = data
        return

    def getLeft(self):
        return self.left

    def getRight(self):
        return self.right

    def getData(self):
        return self.data

    def insertNode(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insertNode(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insertNode(data)
        else:
            self.data = data

    def findMin(self):
        if self.left is not None:
            self.left.findMin()
        else:
            return self.data

    def findMax(self):
        if self.right is not None:
            self.right.findMax()
        else:
            return self.data

    # def deleteNode(self, data):
    #   if self.data:
    #      if data < self.data and self.left!=None:
    #         self.left.deleteNode(data)
    #    elif data > self.data and self.right!=None:
    #       self.right.deleteNode(data)
    #  elif data == self.data:
    #     if self.right != None and self.left != None:
    #        self.data = self.findMin(self.right)
    #       self.
    #
    #
    #
    #       else:
    #          print("Empty tree")

    def printTree(self):
        if self.left:
            self.left.printTree()
        print(self.data),
        if self.right:
            self.right.printTree()


root = Node(12)
root.insertNode(6)
root.insertNode(14)
root.insertNode(3)
root.printTree()

print(root.findMax())
print(root.findMin())
