class House:
    def __init__(self, house_id, water_usage):
        self.house_id = house_id
        self.water_usage = water_usage

    def __repr__(self):
        return f"House {self.house_id}: {self.water_usage} Liters"

def insertion_sort(houses):
    """Sort houses by water usage using Insertion Sort."""

    for i in range(1, len(houses)):
        key = houses[i]  
        j = i - 1
        
        while j >= 0 and houses[j].water_usage > key.water_usage:
            houses[j + 1] = houses[j]
            j -= 1
        houses[j + 1] = key  
    return houses

# Example Usage:

houses = [
    House(101, 250),
    House(102, 150),
    House(103, 180),
    House(104, 220),
    House(105, 175)
]

print("Before Sorting:")
print(houses)

sorted_houses = insertion_sort(houses)

print("\nAfter Sorting by Water Usage:")
print(sorted_houses)
