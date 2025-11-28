from traversal import BinarySearchTree, Node

my_tree = BinarySearchTree()
my_tree.insert(47)
my_tree.insert(21)
my_tree.insert(76)
my_tree.insert(18)
my_tree.insert(27)
my_tree.insert(52)
my_tree.insert(82)

print("BFS Traversal:", my_tree.bfs())
print("DFS Pre-order Traversal:", my_tree.dfs_pre())
print("DFS Post-order Traversal:", my_tree.dfs_post())
print("DFS In-order Traversal:", my_tree.dfs_in())