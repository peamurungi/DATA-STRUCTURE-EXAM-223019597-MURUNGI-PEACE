class Node:
    def __init__(self, name, water_usage=None):
        self.name = name  
        self.water_usage = water_usage  
        self.children = []  

class Tree:
    def __init__(self):
        self.root = None

    def set_root(self, name):
        """Set the root node of the tree (region level)."""
        if self.root is None:
            self.root = Node(name)
        else:
            print("Root already set!")

    def add_neighborhood(self, parent_name, neighborhood_name):
        """Add a neighborhood (subregion) to a given region."""
        parent_node = self.find_node(self.root, parent_name)
        if parent_node:
            new_neighborhood = Node(neighborhood_name)
            parent_node.children.append(new_neighborhood)
            print(f"Neighborhood {neighborhood_name} added to {parent_name}.")
        else:
            print(f"Region {parent_name} not found!")

    def add_house(self, neighborhood_name, house_id, water_usage):
        """Add a house to a given neighborhood."""
        neighborhood_node = self.find_node(self.root, neighborhood_name)
        if neighborhood_node:
            new_house = Node(house_id, water_usage)
            neighborhood_node.children.append(new_house)
            print(f"House {house_id} with water usage {water_usage} added to {neighborhood_name}.")
        else:
            print(f"Neighborhood {neighborhood_name} not found!")

    def find_node(self, node, name):
        """Find a node by its name (region, neighborhood, or house)."""
        if node is None:
            return None
        if node.name == name:
            return node
        for child in node.children:
            found = self.find_node(child, name)
            if found:
                return found
        return None

    def display_tree(self, node=None, level=0):
        """Display the hierarchical data of the tree."""
        if node is None:
            node = self.root
        print("  " * level + f"{node.name} - Water Usage: {node.water_usage if node.water_usage else 'N/A'}")
        for child in node.children:
            self.display_tree(child, level + 1)

# Example Usage:

water_tree = Tree()

water_tree.set_root("Main Region")

water_tree.add_neighborhood("Main Region", "Neighborhood 1")
water_tree.add_neighborhood("Main Region", "Neighborhood 2")

water_tree.add_house("Neighborhood 1", "House 101", 200)
water_tree.add_house("Neighborhood 1", "House 102", 150)

water_tree.add_house("Neighborhood 2", "House 201", 180)
water_tree.add_house("Neighborhood 2", "House 202", 220)

print("\nDisplaying water usage data in the hierarchical structure:")
water_tree.display_tree()
