class HashTableEntry:
    """
    Hash Table entry, as a linked list node.
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

    # def insert(self, key, value):
    #     current_head = None
    #     new_node = HashTableEntry(key, value)
    #     new_node.next = current_head
    #     current_head = new_node

    #     return new_node

    # def remove(self, value):
    #     head = None
    #     current = head
    #     previous = None
    #     while current is not None:
    #         if current.value == value:
    #             previous.next = current.next
    #             return current

    #         previous = current

    #         current = current.next

    #     return None

    # def retrieve(self, value):
    #     head = None
    #     current = head

    #     while current is not None:
    #         if current.value == value:
    #             return current

    #         current = current.next

    #     return None


'''
1. Get bytes for the key
2. Make up a function that returns an index for those bytes
   * Adding the bytes
   * Modding with the hash table size
'''


class HashTable:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = [None] * self.capacity

    """
    A hash table that with `capacity` buckets
    that accepts string keys
    Implement this.
    """

    # def fnv1(self, key):
    """
        FNV-1 64-bit hash function
        Implement this, and/or DJB2.
        """

    def djb2(self, key):
        hash = 5381
        for x in key:
            hash = (hash * 33) + ord(x)

        return hash & 0xFFFFFFFF

    def hash_index(self, key):
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.
        Hash collisions should be handled with Linked List Chaining.
        Implement this.
        Put:
        # Inserts to Head
        # set head to None
        # initiate new node as the new entered value
        # prev node (head) is set to the next node
        # set new node as the current head
        # return new node which is now the current head
        """
        index = self.hash_index(key)
        current_node = self.storage[index]

        if not current_node:
            self.storage[index] = HashTableEntry(key, value)
            return

        while current_node:
            if current_node.key == key:
                current_node.value = value
                return
            elif not current_node.next:
                current_node.next = HashTableEntry(key, value)
                return
            else:
                current_node = current_node.next

    def delete(self, key):
        """
        Remove the value stored with the given key.
        Print a warning if the key is not found.
        Implement this.
        DELETE:
        # find node
        # check to see if the current value is what we are looking for, if it is return the current node (this is us finding the node)
        #find and delete
        # if we can't find the value go to next value
        # if value is not present return None
        """
        index = self.hash_index(key)
        current_node = self.storage[index]

        if current_node.key == key:
            self.storage[index] = current_node.next
            current_node.next = None
            return

        while current_node.next:
            if current_node.next.key == key:
                delete_node = current_node.next
                current_node.next = delete_node.next
                delete_node.next = None
                return
            else:
                current_node = current_node.next
        return print('Warning: Key is not found')

    def get(self, key):
        """
        Retrieve the value stored with the given key.
        Returns None if the key is not found.
        Implement this.
        GET:
        # check to see if the current value is what we are looking for, if it is return the current node
        # if we can't find the value go to next value
        # if value is not present return None
        """
        index = self.hash_index(key)
        current_node = self.storage[index]

        while current_node is not None:
            if current_node.key == key:
                return current_node.value
            else:
                current_node = current_node.next

        return None

    def resize(self):
        """
        Doubles the capacity of the hash table and
        rehash all key/value pairs.
        Implement this.
        """


if __name__ == "__main__":
    ht = HashTable(2)

    ht.put("line_1", "Tiny hash table")
    ht.put("line_2", "Filled beyond capacity")
    ht.put("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.get("line_1"))
    print(ht.get("line_2"))
    print(ht.get("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.get("line_1"))
    print(ht.get("line_2"))
    print(ht.get("line_3"))

    print("")
