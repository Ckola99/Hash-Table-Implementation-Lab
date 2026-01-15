class HashTable():
    def __init__(self):
        self.collection = {}

    def hash(self, string):
        hash = 0
        for c in string:
            hash += ord(c)
        
        return hash
    
    def add(self, key, value):
        computed_hash = self.hash(key)

        if computed_hash not in self.collection:
            self.collection[computed_hash] = {}

        self.collection[computed_hash][key] = value



    def remove(self, key):
        computed_hash = self.hash(key)

        if computed_hash in self.collection:
            if key in self.collection[computed_hash]:
                del self.collection[computed_hash][key]
        

    def lookup(self, key):
        computed_hash = self.hash(key)

        if computed_hash in self.collection:
            if key in self.collection[computed_hash]:
                return self.collection[computed_hash][key]
        
        return None
