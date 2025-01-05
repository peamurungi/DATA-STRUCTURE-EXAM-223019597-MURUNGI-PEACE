class WaterUsageRecord:
    def __init__(self, timestamp, usage, household_id):
        self.timestamp = timestamp
        self.usage = usage  
        self.household_id = household_id

class DynamicArray:
    def __init__(self):
        self.array = []
        self.size = 0
    
    def append(self, record):
        self.array.append(record)
        self.size += 1
    
    def get_household_usage(self, household_id):
        usage_records = []
        for record in self.array:
            if record.household_id == household_id:
                usage_records.append(record)
        return usage_records
    
    def get_total_usage(self, household_id):
        total = 0
        for record in self.array:
            if record.household_id == household_id:
                total += record.usage
        return total

class AVLNode:
    def __init__(self, household_id, address):
        self.household_id = household_id
        self.address = address
        self.usage_records = DynamicArray()
        self.height = 1
        self.left = None
        self.right = None

class AVLTree:
    def __init__(self):
        self.root = None
    
    def height(self, node):
        if not node:
            return 0
        return node.height
    
    def balance_factor(self, node):
        if not node:
            return 0
        return self.height(node.left) - self.height(node.right)
    
    def update_height(self, node):
        if not node:
            return
        node.height = max(self.height(node.left), self.height(node.right)) + 1
    
    def right_rotate(self, y):
        x = y.left
        T2 = x.right
        
        x.right = y
        y.left = T2
        
        self.update_height(y)
        self.update_height(x)
        
        return x
    
    def left_rotate(self, x):
        y = x.right
        T2 = y.left
        
        y.left = x
        x.right = T2
        
        self.update_height(x)
        self.update_height(y)
        
        return y
    
    def insert(self, household_id, address):
        def _insert(node, household_id, address):
            if not node:
                return AVLNode(household_id, address)
            
            if household_id < node.household_id:
                node.left = _insert(node.left, household_id, address)
            elif household_id > node.household_id:
                node.right = _insert(node.right, household_id, address)
            else:
                return node
            
            self.update_height(node)
            
            balance = self.balance_factor(node)
            
            if balance > 1 and household_id < node.left.household_id:
                return self.right_rotate(node)
            
            if balance < -1 and household_id > node.right.household_id:
                return self.left_rotate(node)

            if balance > 1 and household_id > node.left.household_id:
                node.left = self.left_rotate(node.left)
                return self.right_rotate(node)
            
            if balance < -1 and household_id < node.right.household_id:
                node.right = self.right_rotate(node.right)
                return self.left_rotate(node)
            
            return node
        
        self.root = _insert(self.root, household_id, address)
    
    def find_household(self, household_id):
        def _find(node, household_id):
            if not node:
                return None
            if node.household_id == household_id:
                return node
            if household_id < node.household_id:
                return _find(node.left, household_id)
            return _find(node.right, household_id)
        
        return _find(self.root, household_id)
    
    def add_usage_record(self, household_id, timestamp, usage):
        household = self.find_household(household_id)
        if household:
            record = WaterUsageRecord(timestamp, usage, household_id)
            household.usage_records.append(record)
            return True
        return False

# Example usage
def main():
    monitoring_system = AVLTree()
    
    monitoring_system.insert(1001, "123 Main St")
    monitoring_system.insert(1002, "456 Oak Ave")
    monitoring_system.insert(1003, "789 Pine Rd")
    
    monitoring_system.add_usage_record(1001, "2024-01-04 10:00", 150)  
    monitoring_system.add_usage_record(1001, "2024-01-04 11:00", 100)
    monitoring_system.add_usage_record(1002, "2024-01-04 10:00", 200)
    
    household = monitoring_system.find_household(1001)
    if household:
        total_usage = household.usage_records.get_total_usage(1001)
        print(f"Total usage for household 1001: {total_usage} liters")
        
        records = household.usage_records.get_household_usage(1001)
        print("\nUsage records for household 1001:")
        for record in records:
            print(f"Time: {record.timestamp}, Usage: {record.usage} liters")

if __name__ == "__main__":
    main()