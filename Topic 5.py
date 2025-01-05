class Node:
    def __init__(self, house_id, water_usage):
        self.house_id = house_id
        self.water_usage = water_usage
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, house_id, water_usage):
        """Insert a new house with its water usage into the BST."""
        new_node = Node(house_id, water_usage)
        if self.root is None:
            self.root = new_node
        else:
            self._insert(self.root, new_node)

    def _insert(self, root, new_node):
        """Helper method to insert a node recursively."""
        if new_node.house_id < root.house_id:
            if root.left is None:
                root.left = new_node
            else:
                self._insert(root.left, new_node)
        else:
            if root.right is None:
                root.right = new_node
            else:
                self._insert(root.right, new_node)

    def search(self, house_id):
        """Search for a house by its ID."""
        return self._search(self.root, house_id)

    def _search(self, root, house_id):
        """Helper method to search for a house recursively."""
        if root is None or root.house_id == house_id:
            return root
        elif house_id < root.house_id:
            return self._search(root.left, house_id)
        else:
            return self._search(root.right, house_id)

    def update_usage(self, house_id, new_water_usage):
        """Update the water usage for a specific house."""
        house = self.search(house_id)
        if house:
            house.water_usage = new_water_usage
            print(f"Updated water usage for House {house_id} to {new_water_usage} Liters.")
        else:
            print(f"House {house_id} not found!")

    def delete(self, house_id):
        """Delete a house from the tree."""
        self.root = self._delete(self.root, house_id)

    def _delete(self, root, house_id):
        """Helper method to delete a node from the tree."""
        if root is None:
            return root
        if house_id < root.house_id:
            root.left = self._delete(root.left, house_id)
        elif house_id > root.house_id:
            root.right = self._delete(root.right, house_id)
        else:

            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            root.house_id, root.water_usage = self._min_value_node(root.right)
            root.right = self._delete(root.right, root.house_id)
        return root

    def _min_value_node(self, root):
        """Find the node with the minimum value."""
        current = root
        while current.left is not None:
            current = current.left
        return current.house_id, current.water_usage

    def inorder_traversal(self):
        """In-order traversal to display house water usage data in sorted order."""
        self._inorder_traversal(self.root)

    def _inorder_traversal(self, root):
        """Helper method to perform in-order traversal."""
        if root:
            self._inorder_traversal(root.left)
            print(f"House {root.house_id} - Water Usage: {root.water_usage} Liters")
            self._inorder_traversal(root.right)

# Example Usage:

bst = BinarySearchTree()

bst.insert(3, 200)
bst.insert(1, 150)
bst.insert(5, 180)
bst.insert(4, 220)
bst.insert(2, 170)

print("Displaying all houses with water usage data (In-order traversal):")
bst.inorder_traversal

bst.update_usage(3, 210)

print("\nDisplaying updated water usage data:")
bst.inorder_traversal()

bst.delete(1)

print("\nDisplaying water usage data after deleting House 1:")
bst.inorder_traversal()

bst.delete(5)

print("\nDisplaying water usage data after deleting House 5:")
bst.inorder_traversal()
