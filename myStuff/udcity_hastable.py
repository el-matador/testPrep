"""Write a HashTable class that stores strings
in a hash table, where keys are calculated
using the first two letters of the string."""

class HashTableCopy(object):
    def __init__(self):
        self.table = []

    def store(self, string):
        """Input a string that's stored in 
        the table."""
        hash_value = self.calculate_hash_value(string)
        self.table.append(hash_value)
        print self.table

    def lookup(self, string):
        """Return the hash value if the
        string is already in the table.
        Return -1 otherwise."""
        hash_value = self.calculate_hash_value(string)
        if hash_value in self.table:
            return hash_value
        else:
            return -1

    def calculate_hash_value(self, string):
        """Helper function to calulate a
        hash value from a string."""
        hashResult = 0
        for char in string:
            hashResult += ord(char)
            
        return hashResult
    

class HashTable(object):
    def __init__(self):
        self.table = [None]*10000

    def store(self, string):
        hv = self.calculate_hash_value(string)
        if hv != -1:
            if self.table[hv] != None:
                self.table[hv].append(string)
            else:
                self.table[hv] = [string]

    def lookup(self, string):
        hv = self.calculate_hash_value(string)
        if hv != -1:
            if self.table[hv] != None:
                if string in self.table[hv]:
                    return hv
        return -1

    def calculate_hash_value(self, string):
        value = ord(string[0])*100 + ord(string[1])
        return value
# Setup
animalsList = ['cat','dog','tac','god','act']
size = len(animalsList)
hash_table = HashTableCopy()

# Test store
for animal in animalsList:
    hash_table.store(animal)
# Should be 8568
print "Look up"

map = {}

for i in range(size):
    if hash_table.table[i] in map:
        map[hash_table.table[i]].append(i)
    else:
        map[hash_table.table[i]] = [i]

print map

for index in map[hash_table.lookup('cat')]:
    print animalsList[index]
    
    