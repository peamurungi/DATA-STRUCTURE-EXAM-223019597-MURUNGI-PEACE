class Node:
    def __init__(self, house_id, water_usage):
        self.house_id = house_id
        self.water_usage = water_usage
        self.next = None  

class CircularLinkedList:
    def __init__(self):
        self.head = None  

    def is_empty(self):
        """Check if the list is empty."""
        return self.head is None

    def add_house(self, house_id, water_usage):
        """Add a new house to the circular linked list."""
        new_node = Node(house_id, water_usage)
        
        if self.is_empty():
            self.head = new_node
            new_node.next = self.head  
        else:
            current = self.head
            while current.next != self.head:  
                current = current.next
            current.next = new_node  
            new_node.next = self.head  

    def update_usage(self, house_id, new_water_usage):
        """Update the water usage for a specific house."""
        if self.is_empty():
            print("List is empty!")
            return
        
        current = self.head
        while True:
            if current.house_id == house_id:
                current.water_usage = new_water_usage
                print(f"Updated water usage for House {house_id} to {new_water_usage} Liters.")
                return
            current = current.next
            if current == self.head:  
                break
        print(f"House {house_id} not found!")

    def display_all_usages(self):
        """Display water usage for all houses in the circular list."""
        if self.is_empty():
            print("List is empty!")
            return

        current = self.head
        while True:
            print(f"House {current.house_id} - Water Usage: {current.water_usage} Liters")
            current = current.next
            if current == self.head: 
                break

    def delete_house(self, house_id):
        """Delete a house from the circular linked list."""
        if self.is_empty():
            print("List is empty!")
            return

        current = self.head
        prev = None
        while True:
            if current.house_id == house_id:
                if prev is None:  
                
                    if current.next == self.head:
                        self.head = None
                    else:

                        last_node = self.head
                        while last_node.next != self.head:
                            last_node = last_node.next
                        self.head = current.next
                        last_node.next = self.head
                else:
                    prev.next = current.next
                print(f"House {house_id} deleted.")
                return
            prev = current
            current = current.next
            if current == self.head:
                break
        print(f"House {house_id} not found!")

# Example Usage:

cll = CircularLinkedList()

cll.add_house(1, 200)
cll.add_house(2, 150)
cll.add_house(3, 180)
cll.add_house(4, 220)
cll.add_house(5, 170)

print("Displaying all water usages:")
cll.display_all_usages()

cll.update_usage(3, 200)

print("\nDisplaying updated water usages:")
cll.display_all_usages()

cll.delete_house(2)

print("\nDisplaying water usages after deleting House 2:")
cll.display_all_usages()
