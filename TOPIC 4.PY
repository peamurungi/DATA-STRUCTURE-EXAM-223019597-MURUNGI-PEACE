from datetime import datetime

class Node:
    def __init__(self, house_id, water_usage, timestamp):
        self.house_id = house_id
        self.water_usage = water_usage
        self.timestamp = timestamp
        self.next = None

class SinglyLinkedList:
    def __init__(self, max_orders):
        self.head = None  
        self.max_orders = max_orders  
        self.size = 0 

    def is_full(self):
        """Check if the list is full."""
        return self.size == self.max_orders

    def is_empty(self):
        """Check if the list is empty."""
        return self.size == 0

    def add_order(self, house_id, water_usage):
        """Add a new order to the linked list."""

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        new_node = Node(house_id, water_usage, timestamp)

        if self.is_full():
            self.remove_oldest_order()  
        
        if self.is_empty():
            self.head = new_node  
        else:
            current = self.head
            while current.next: 
                current = current.next
            current.next = new_node  

        self.size += 1
        print(f"Order added: House {house_id} used {water_usage} Liters at {timestamp}.")

    def remove_oldest_order(self):
        """Remove the oldest order from the list (the head node)."""
        if self.is_empty():
            print("List is empty, no order to remove.")
            return
        
        print(f"Removing oldest order: House {self.head.house_id} used {self.head.water_usage} Liters.")
        self.head = self.head.next  
        self.size -= 1

    def update_order(self, house_id, new_water_usage):
        """Update the water usage for a specific house in the order list."""
        if self.is_empty():
            print("List is empty!")
            return
        
        current = self.head
        while current:
            if current.house_id == house_id:
                current.water_usage = new_water_usage
                print(f"Updated order: House {house_id} now uses {new_water_usage} Liters.")
                return
            current = current.next
        print(f"House {house_id} not found!")

    def display_orders(self):
        """Display all orders in the list."""
        if self.is_empty():
            print("List is empty!")
            return

        current = self.head
        while current:
            print(f"House {current.house_id} - Water Usage: {current.water_usage} Liters - Order Time: {current.timestamp}")
            current = current.next

# Example Usage:

order_system = SinglyLinkedList(max_orders=3)

order_system.add_order(1, 200)
order_system.add_order(2, 150)
order_system.add_order(3, 180)

print("\nDisplaying all orders:")
order_system.display_orders()

order_system.add_order(4, 220)

print("\nDisplaying all orders after adding a new order:")
order_system.display_orders()

order_system.update_order(2, 175)

print("\nDisplaying all orders after updating House 2's order:")
order_system.display_orders()

order_system.add_order(5, 190)

print("\nDisplaying all orders after adding a new order (House 5):")
order_system.display_orders()
