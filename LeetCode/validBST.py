from Tree_Traversal.traversal import BinarySearchTree
def is_valid_bst(self):
    values = self.dfs_in()
    for i in range(1,len(values)):
        if values[i]<=values[i-1]:
            return False
    return True

my_tree = BinarySearchTree()
my_tree.insert(47)
my_tree.insert(21)
my_tree.insert(76)
my_tree.insert(18)
my_tree.insert(27)
my_tree.insert(52)
my_tree.insert(82)
print(is_valid_bst(my_tree))  # Expected output: True