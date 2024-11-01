# Step 1: Define the Node Class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Step 2: Define the LinkedList Class with all methods
class LinkedList:
    def __init__(self):
        self.head = None

# Step 3: Append method
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

# Step 4: Display method
    def display(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        print(" -> ".join(map(str, elements)))

    # Step 5: Insert method
    def insert(self, data, position):
        new_node = Node(data)
        if position == 0:
            new_node.next = self.head
            self.head = new_node
            return
        current = self.head
        for _ in range(position - 1):
            if current is None:
                raise IndexError("Position out of range")
            current = current.next
        new_node.next = current.next
        current.next = new_node

    # Step 6: Delete method
    def delete(self, data):
        if not self.head:
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next

    # Step 7: Search method
    def search(self, data):
        current = self.head
        position = 0
        while current:
            if current.data == data:
                return position
            current = current.next
            position += 1
        return -1

    # Step 8: Reverse method
    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

# Test the LinkedList class with all methods
ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.display()  # Output: 1 -> 2 -> 3

ll.insert(4, 1)
ll.display()  # Output: 1 -> 4 -> 2 -> 3

ll.delete(2)
ll.display()  # Output: 1 -> 4 -> 3

print(ll.search(4))  # Output: 1
print(ll.search(5))  # Output: -1

ll.reverse()
ll.display()  # Output: 3 -> 4 -> 1


#Exercises:
#A. Implement a method to find the middle element of the linked list.
# Step 1: Define the Node Class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Step 2: Define the LinkedList Class with methods
class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def display(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        print(" -> ".join(map(str, elements)))

    def find_middle(self):
        if not self.head:
            return None
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow.data

# Testing the find_middle method
ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)
ll.append(5)

ll.display()  # Output: 1 -> 2 -> 3 -> 4 -> 5
print("Middle element:", ll.find_middle())  # Output: 3

# Testing with even number of elements
ll.append(6)
ll.display()  # Output: 1 -> 2 -> 3 -> 4 -> 5 -> 6
print("Middle element:", ll.find_middle())  # Output: 4

# B. Create a method to detect if the linked list has a cycle.
# Step 1: Define the Node Class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Step 2: Define the LinkedList Class with methods
class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def has_cycle(self):
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

# Testing the has_cycle method
ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)
ll.append(5)

# Manually creating a cycle for testing
ll.head.next.next.next.next.next = ll.head.next  # Creating a cycle

print("Does the linked list have a cycle?", ll.has_cycle())  # Output: True

# Testing with a non-cyclic list
ll2 = LinkedList()
ll2.append(1)
ll2.append(2)
ll2.append(3)
print("Does the linked list have a cycle?", ll2.has_cycle())  # Output: False

#C. Implement a method to remove duplicates from an unsorted linked list.
# Step 1: Define the Node Class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Step 2: Define the LinkedList Class with methods
class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def display(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        print(" -> ".join(map(str, elements)))

    def remove_duplicates(self):
        if not self.head:
            return
        seen = set()  # Track unique values
        current = self.head
        seen.add(current.data)
        while current.next:
            if current.next.data in seen:
                # Remove the duplicate node
                current.next = current.next.next
            else:
                # Add to the set and move to the next node
                seen.add(current.next.data)
                current = current.next

# Testing the remove_duplicates method
ll = LinkedList()
ll.append(1)
ll.append(3)
ll.append(2)
ll.append(3)
ll.append(1)
ll.append(4)
ll.display()  # Output before removing duplicates: 1 -> 3 -> 2 -> 3 -> 1 -> 4

ll.remove_duplicates()
ll.display()  # Output after removing duplicates: 1 -> 3 -> 2 -> 4

# D:
# Add a method to merge two sorted linked lists into a single sorted linked list.
# Step 1: Define the Node Class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Step 2: Define the LinkedList Class with methods
class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def display(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        print(" -> ".join(map(str, elements)))

    @staticmethod
    def merge_sorted(list1, list2):
        # Create a dummy node to build the merged list
        dummy = Node(0)
        current = dummy
        p1, p2 = list1.head, list2.head

        # Traverse both lists, picking the smaller node each time
        while p1 and p2:
            if p1.data < p2.data:
                current.next = p1
                p1 = p1.next
            else:
                current.next = p2
                p2 = p2.next
            current = current.next

        # Append any remaining nodes from either list
        if p1:
            current.next = p1
        elif p2:
            current.next = p2

        # Create the merged linked list
        merged_list = LinkedList()
        merged_list.head = dummy.next  # Skip the dummy node
        return merged_list

# Testing the merge_sorted method
list1 = LinkedList()
list1.append(1)
list1.append(3)
list1.append(5)

list2 = LinkedList()
list2.append(2)
list2.append(4)
list2.append(6)

merged_list = LinkedList.merge_sorted(list1, list2)
merged_list.display()  # Output: 1 -> 2 -> 3 -> 4 -> 5 -> 6

