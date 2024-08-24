class Node:
    def __init__(self, data):
        self.value = data
        self.right = None
        self.left = None


class BinaryTree:
    def __init__(self):
        print("Initialising the Binary Tree")
        self.root = None
        print("Binary Tree Initialized")

    def insert(self, val):
        def insert_recursive(current_node, val):
            if current_node is None:
                current_node = Node(data=val)
                print(f"{val} inserted successfully in BST.")
                return current_node
            elif current_node.value == val:
                return current_node
            elif current_node.value > val:
                current_node.left = insert_recursive(current_node.left, val)
            else:
                current_node.right = insert_recursive(current_node.right, val)
        if self.root is None:
            self.root = Node(data=val)
            print(f"{val} inserted as root successfully in BST.")
        else:
            insert_recursive(self.root, val)

    def in_order_traversal(self):
        def _in_order_recursive(current_node):
            if current_node is None:
                return
            else:
                _in_order_recursive(current_node.left)
                result.append(current_node.value)
                _in_order_recursive(current_node.right)
        if self.root is None:
            print("Tree is Empty!!")
            return
        else:
            result = []
            _in_order_recursive(self.root)
            return result


if __name__ == "__main__":
    bst = BinaryTree()
    while True:
        print("**********************************")
        print("1. Insert the node")
        print("2. Delete the node")
        print("3. Search the node")
        print("4. Pre-Order Traversal")
        print("5. In-Order Traversal")
        print("6. Post-Order Traversal")
        print("7. Breadth-First Search (Level-Order Traversal)")
        element = int(input("Enter your choice: "))
        if element == 1:
            value = input("Enter the value to be inserted in Binary Search Tree(BST): ")
            bst.insert(val=value)
        elif element == 5:
            in_order = bst.in_order_traversal()
            print(in_order)
        else:
            break
