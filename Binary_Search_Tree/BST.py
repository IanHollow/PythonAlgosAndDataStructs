class Node:
    def __init__(self, value, parent):
        self.value = value
        self.parent = parent
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value, None)

        if self.root == None:
            self.root = new_node
            return

        parent_node = self.root
        while True:
            if value < parent_node.value:

                if parent_node.left == None:
                    parent_node.left = new_node
                    break
                parent_node = parent_node.left

            elif value > parent_node.value:

                if parent_node.right == None:
                    parent_node.right = new_node
                    break
                parent_node = parent_node.right

            else:
                return

        new_node.parent = parent_node

    def get_node_count(self):
        def traverse(node):
            if node == None:
                return 0

            left = traverse(node.left)
            right = traverse(node.right)

            return (left + right + 1)

        return traverse(self.root)

    def print_values(self):
        values = []

        def traverse(node):
            if node == None:
                return

            traverse(node.left)
            values.append(node.value)
            traverse(node.right)

        traverse(self.root)

        print(values)

    def delete_tree(self):
        self.root = None

    def is_in_tree(self, value):
        def traverse(node):
            if node == None:
                return
            if node.value == value:
                return True

            if traverse(node.left) or traverse(node.right):
                return True
            return False

        return traverse(self.root)

    def get_height(self):
        def traverse(node):
            if node == None:
                return 0

            left = traverse(node.left)
            right = traverse(node.right)

            if left > right:
                return left+1
            else:
                return right+1

        return traverse(self.root)

    def get_min(self):
        current_node = self.root

        if current_node == None:
            return None

        while current_node.left:
            current_node = current_node.left

        return current_node.value

    def get_max(self):
        current_node = self.root

        if current_node == None:
            return None

        while current_node.right:
            current_node = current_node.right

        return current_node.value

    def get_successor(self, node):
        node = node.right

        if node == None:
            return None

        while node.left:
            node = node.left

        return node

    def get_predecessor(self, node):
        node = node.left

        if node == None:
            return None

        while node.right:
            node = node.right

        return node

    def delete(self, value):
        def traverse(node):
            if node == None:
                return None
            if node.value == value:
                predecessor = self.get_predecessor(node)
                successor = self.get_successor(node)

                if predecessor:
                    temp = node.value
                    node.value = predecessor.value
                    predecessor.value = temp

                    traverse(predecessor)
                elif successor:
                    temp = node.value
                    node.value = successor.value
                    successor.value = temp

                    traverse(successor)
                else:
                    if node.parent.left == node:
                        node.parent.left = None
                    else:
                        node.parent.right = None

            traverse(node.left)
            traverse(node.right)

        traverse(self.root)


bst = BinarySearchTree()

bst.insert(10)
bst.insert(4)
bst.insert(2)
bst.insert(7)
bst.insert(3)

bst.insert(15)
bst.insert(13)
bst.insert(18)

bst.print_values()

print(bst.get_node_count())

print(bst.is_in_tree(5))
print(bst.is_in_tree(7))

print(bst.get_height())

print(bst.get_min())
print(bst.get_max())

bst.delete(10)
bst.print_values()

bst.delete(15)
bst.print_values()

bst.delete(3)
bst.print_values()

bst.delete(3)
bst.print_values()
