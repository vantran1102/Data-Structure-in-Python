class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
class BinarySearchTree:
    def __init__(self):
        self.root = None
        
    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        while (True):
            if new_node.value == temp.value:
                return False
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else: 
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right
    
    def bfs(self):
        result = []
        queue = []
        current_node = self.root
        queue.append(self.root)
        while len(queue) > 0:
            current_node = queue.pop(0)
            result.append(current_node.value)
            if current_node.left is not None:
                queue.append(current_node.left)
            if current_node.right is not None:
                queue.append(current_node.right)
        return result

    def dfs_pre(self):
        result = []
        def traversal(current_node):
            result.append(current_node.value)
            if current_node.left is not None:
                traversal(current_node.left)
            if current_node.right is not None:
                traversal(current_node.right)
        traversal(self.root)
        return result
    
    def dfs_post(self):
        result = []
        def traversal(current_node):
            if current_node.left is not None:
                traversal(current_node.left)
            if current_node.right is not None:
                traversal(current_node.right)
            result.append(current_node.value)
        traversal(self.root)
        return result

    def dfs_in(self):
        result = []
        def traversal(current_node):
            if current_node.left is not None:
                traversal(current_node.left)
            result.append(current_node.value)
            if current_node.right is not None:
                traversal(current_node.right)
        traversal(self.root)
        return result