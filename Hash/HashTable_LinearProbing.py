class HashTableLinearProbing:
    _DEFAULT_SIZE = 8
    _DELTED_VALUE = "==DELETED=="
    _LOAD_FACTOR = 0.75
    _MIN_FACTOR = 1/4

    def __init__(self):
        self.container = [None] * self._DEFAULT_SIZE
        self.capacity = self._DEFAULT_SIZE
        self.size = 0

    def hash_function(self, key, capacity=None):
        if capacity == None:
            capacity = self.capacity
        return key % capacity

    def add(self, key):
        hash_value = self.hash_function(key)

        while self.container[hash_value] is not None:
            if self.container[hash_value] == key:
                return

            hash_value = (hash_value + 1) % self.capacity

        self.container[hash_value] = key

        self.size += 1

        if (self.size/self.capacity) >= self._LOAD_FACTOR:
            self._resize(self.capacity * 2)

    def _resize(self, new_capacity):
        new_container = [None]*new_capacity

        for key in self.container:
            if (key != None) and (key != self._DELTED_VALUE):
                hash_value = self.hash_function(key, new_capacity)

                while new_container[hash_value] is not None:
                    hash_value = (hash_value + 1) % self.capacity

                new_container[hash_value] = key

        self.capacity = new_capacity
        self.container = new_container

    def remove(self, key):
        hash_value = self.hash_function(key)

        while self.container[hash_value] is not None:
            if key != self.container[hash_value]:
                hash_value = (hash_value + 1) % self.capacity
                continue

            self.container[hash_value] = self._DELTED_VALUE
            self.size -= 1
            if (self.size/self.capacity) <= self._MIN_FACTOR:
                self._resize(self.capacity // 2)
            return

        raise KeyError(f"Key {key} is not in Hash Table")

    def get(self, key):
        hash_value = self.hash_function(key)

        while self.container[hash_value] is not None:
            if key == self.container[hash_value]:
                return hash_value

            hash_value = (hash_value + 1) % self.capacity

        raise KeyError(f"Key {key} not in Hash Table")

    def exists(self, key):
        hash_value = self.hash_function(key)

        while self.container[hash_value] is not None:
            if key == self.container[hash_value]:
                return True

            hash_value = (hash_value + 1) % self.capacity

        return False

    def printHashTable(self):
        print(self.container)


hash_table = HashTableLinearProbing()

hash_table.printHashTable()

hash_table.add(43)
hash_table.add(35)
hash_table.add(78)
hash_table.add(56)
hash_table.add(23)

hash_table.printHashTable()

hash_table.add(32)

hash_table.printHashTable()

hash_table.add(54)

hash_table.printHashTable()

hash_table.remove(43)
hash_table.remove(35)

hash_table.printHashTable()

hash_table.remove(23)

hash_table.printHashTable()

print(hash_table.get(78))

print(hash_table.exists(78))

print(hash_table.exists(999))
