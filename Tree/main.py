from tree import BinarySearchTree
from tree import Node

myTree = BinarySearchTree()
myTree.insert(2)
myTree.insert(3)
myTree.insert(1)

print("Left: ", myTree.root.left.value)
print("Right: ", myTree.root.right.value)
print("Root: ", myTree.root.value)

print("Tree contains 2: ",myTree.contain(2))
print("Tree contains 5: ", myTree.contain(5))
