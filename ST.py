class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

    def __str__(self):
        return "<Node: (%s, %s), next: %s>" % (self.key, self.value, self.next != None)

    def __repr__(self):
        return str(self)


# Hash table with separate chaining
class HashTable:
    def __init__(self):
        self.capacity = 255
        self.size = 0
        self.buckets = [None] * self.capacity

    def __str__(self):
        s = ""

        s += "size is: " + str(self.size) + "\n"
        for i in self.buckets:
            if i is not None:
                s += str(i) + "\n"
                node = i.next
                while node is not None:
                    s += str(node) + "\n"
                    node = node.next
        return s

    # Generate a hash for a given key
    # Input:  key - string
    # Output: Index from 0 to self.capacity
    def hash(self, key):
        hashsum = 0
        for idx, c in enumerate(key):
            # Add (index + length of key) ^ (current char code)
            hashsum += (idx + len(key)) ** ord(c)
            # Perform modulus to keep hashsum in range [0, self.capacity - 1]
            hashsum = hashsum % self.capacity
        return hashsum

    # Insert a key,value pair to the hashtable
    # Input:  key - string
    # 		  value - anything
    # Output: void
    def insert(self, value):
        # 1. Increment size
        self.size += 1
        # 2. Compute index of key
        index = self.hash(value)
        # Go to the node corresponding to the hash
        node = self.buckets[index]
        # 3. If bucket is empty:
        if node is None:
            # Create node, add it, return
            self.buckets[index] = Node(index, value)
            return
        # 4. Iterate to the end of the linked list at provided index
        ok = 1
        prev = node
        while node is not None:
            prev = node
            node = node.next
            if prev.value == value:
                ok = 0
                self.size -= 1
        # Add a new node at the end of the list with provided key/value
        if ok == 1:
            prev.next = Node(index, value)

    # Find a data value based on key
    # Input:  key - string
    # Output: value stored under "key" or None if not found
    def find(self, key):
        # 1. Compute hash
        index = self.hash(key)
        # 2. Go to first node in list at bucket
        node = self.buckets[index]
        # 3. Traverse the linked list at this node
        while node is not None and node.value != key:
            node = node.next
        # 4. Now, node is the requested key/value pair or None
        if node is None:
            return None
        else:
            return node.value
