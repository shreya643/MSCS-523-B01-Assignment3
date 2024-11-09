class HashTableChaining:
    def __init__(self, ini_capacity=10):
        self.table = [[] for _ in range(ini_capacity)]
        self.capacity = ini_capacity
        self.size = 0

    def hash_function(self, key):
        return hash(key) % self.capacity

    def insert(self, key, value):
        index = self.hash_function(key)
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value  
                return
        self.table[index].append([key, value])
        self.size += 1
        if self.size / self.capacity > 0.7: 
            self.resize()

    def search(self, key):
        index = self.hash_function(key)
        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]
        return None

    def delete(self, key):
        index = self.hash_function(key)
        for i, pair in enumerate(self.table[index]):
            if pair[0] == key:
                self.table[index].pop(i)
                self.size -= 1
                return True
        return False 

    def resize(self):
        new_capacity = self.capacity * 2
        new_table = [[] for _ in range(new_capacity)]
        for chain in self.table:
            for key, value in chain:
                index = hash(key) % new_capacity
                new_table[index].append([key, value])
        self.table = new_table
        self.capacity = new_capacity


hash_table = HashTableChaining()
hash_table.insert("test1", 1)
hash_table.insert("test2", 2)
hash_table.insert("test3", 3)
hash_table.insert("test4", 4)
hash_table.insert("test5", 5)

print("Search 'test1':", hash_table.search("test1"))
print("Search 'test3':", hash_table.search("test3"))

hash_table.delete("test3")
print("Search 'test3' after deletion:", hash_table.search("test3"))