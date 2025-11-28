class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
       
class BinarySearchTree:
    def __init__(self):
        self.root = None

    def invert_tree(self):  
        self.root = self.__invert_tree(self.root)
    def __invert_tree(self, node):
        if node is None:
            return None
        l = node.left
        r = node.right
        node.left = self.__invert_tree(r)
        node.right = self.__invert_tree(l)
        return node
my_node = TreeNode(4,
        TreeNode(2, TreeNode(1), TreeNode(3)),
        TreeNode(7, TreeNode(6), TreeNode(9)))
tree = BinarySearchTree()
tree.root = my_node
print(tree.invert_tree())