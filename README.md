# Hash Table Implementation Lab

## Overview

A hands-on **lab project implementing a hash table from scratch** in Python. This educational project demonstrates fundamental data structure concepts including hash functions, collision resolution, and key-value storage without relying on Python's built-in dictionary functionality for the core implementation.

---

## What You'll Learn

- 🔐 How hash functions convert keys to indices
- 🛡️ Collision resolution using separate chaining
- ⚡ O(1) average-case lookup performance
- 📊 Time and space complexity analysis
- 🎯 Implementing abstract data types
- 🧪 Testing data structure implementations

---

## Lab Objectives

By completing this lab, you will:

1. Understand how hash tables work internally
2. Implement a custom hash function
3. Handle hash collisions properly
4. Create add, remove, and lookup operations
5. Analyze algorithm performance
6. Test edge cases and validate correctness

---

## Hash Table Basics

### What is a Hash Table?

A **hash table** is a data structure that maps keys to values for highly efficient lookup. It uses a **hash function** to compute an index into an array of buckets, from which the desired value can be found.

### Key Components

1. **Hash Function**: Converts any key into a numeric hash code
2. **Buckets**: Storage locations for key-value pairs
3. **Collision Handling**: Strategy for when two keys hash to the same location

---

## Implementation

### Class Structure

```python
class HashTable():
    def __init__(self):
        self.collection = {}
    
    def hash(self, string):
        # Returns hash code for a string
        
    def add(self, key, value):
        # Adds or updates a key-value pair
        
    def remove(self, key):
        # Removes a key-value pair
        
    def lookup(self, key):
        # Retrieves value for a given key
```

---

## Method Specifications

### `__init__(self)`

**Purpose**: Initialize an empty hash table

**Implementation**:
```python
def __init__(self):
    self.collection = {}
```

**Details**:
- Creates an empty dictionary to store buckets
- Each bucket will hold key-value pairs that hash to the same value

---

### `hash(self, string)`

**Purpose**: Compute a hash code for a string key

**Parameters**:
- `string` (str): The key to hash

**Returns**: int - The computed hash value

**Algorithm**:
```python
def hash(self, string):
    hash = 0
    for c in string:
        hash += ord(c)
    return hash
```

**How it works**:
1. Start with hash = 0
2. For each character in the string:
   - Get its ASCII value using `ord()`
   - Add it to the hash
3. Return the final hash sum

**Examples**:
```python
ht = HashTable()
print(ht.hash('a'))      # 97
print(ht.hash('hello'))  # 532 (104+101+108+108+111)
print(ht.hash('world'))  # 552
```

**Collision Example**:
```python
# Anagrams produce the same hash
ht.hash('listen')  # 650
ht.hash('silent')  # 650 (same letters = same sum)
```

---

### `add(self, key, value)`

**Purpose**: Add or update a key-value pair in the hash table

**Parameters**:
- `key` (str): The key to store
- `value` (any): The value to associate with the key

**Returns**: None

**Algorithm**:
```python
def add(self, key, value):
    computed_hash = self.hash(key)
    
    if computed_hash not in self.collection:
        self.collection[computed_hash] = {}
    
    self.collection[computed_hash][key] = value
```

**How it works**:
1. Compute the hash of the key
2. Check if a bucket exists at that hash
   - If not, create a new empty bucket (dictionary)
3. Store the key-value pair in the bucket

**Examples**:
```python
ht = HashTable()
ht.add('name', 'Alice')
ht.add('age', 25)
ht.add('city', 'NYC')
ht.add('name', 'Bob')  # Updates 'name' to 'Bob'
```

---

### `remove(self, key)`

**Purpose**: Remove a key-value pair from the hash table

**Parameters**:
- `key` (str): The key to remove

**Returns**: None

**Algorithm**:
```python
def remove(self, key):
    computed_hash = self.hash(key)
    
    if computed_hash in self.collection:
        if key in self.collection[computed_hash]:
            del self.collection[computed_hash][key]
```

**How it works**:
1. Compute the hash of the key
2. Check if a bucket exists at that hash
3. Check if the key exists in the bucket
4. If found, delete the key-value pair

**Examples**:
```python
ht = HashTable()
ht.add('name', 'Alice')
ht.add('age', 25)

ht.remove('age')       # Removes 'age'
ht.remove('email')     # Does nothing (key doesn't exist)
```

---

### `lookup(self, key)`

**Purpose**: Retrieve the value associated with a key

**Parameters**:
- `key` (str): The key to look up

**Returns**:
- The value if the key exists
- `None` if the key doesn't exist

**Algorithm**:
```python
def lookup(self, key):
    computed_hash = self.hash(key)
    
    if computed_hash in self.collection:
        if key in self.collection[computed_hash]:
            return self.collection[computed_hash][key]
    
    return None
```

**How it works**:
1. Compute the hash of the key
2. Check if a bucket exists at that hash
3. Check if the key exists in the bucket
4. Return the value if found, otherwise return `None`

**Examples**:
```python
ht = HashTable()
ht.add('name', 'Alice')
ht.add('age', 25)

print(ht.lookup('name'))   # Output: Alice
print(ht.lookup('age'))    # Output: 25
print(ht.lookup('email'))  # Output: None
```

---

## Collision Resolution

### The Problem

Different keys can produce the same hash value (a **collision**):

```python
ht = HashTable()
print(ht.hash('listen'))  # 650
print(ht.hash('silent'))  # 650  ← Collision!
```

### The Solution: Separate Chaining

This implementation uses **separate chaining** with nested dictionaries:

```python
# Internal structure with collision
{
    650: {
        'listen': 'value1',
        'silent': 'value2'
    },
    532: {
        'hello': 'value3'
    }
}
```

Each bucket (hash code) contains a dictionary of actual key-value pairs.

### How It Handles Collisions

```python
ht = HashTable()

# Add 'listen'
ht.add('listen', 'value1')
# Internal: {650: {'listen': 'value1'}}

# Add 'silent' (collides with 'listen')
ht.add('silent', 'value2')
# Internal: {650: {'listen': 'value1', 'silent': 'value2'}}

# Both keys are retrievable
print(ht.lookup('listen'))  # value1
print(ht.lookup('silent'))  # value2
```

---

## Performance Analysis

### Time Complexity

| Operation | Average Case | Worst Case |
|-----------|-------------|------------|
| `hash()` | O(k)* | O(k)* |
| `add()` | O(1) | O(n)** |
| `lookup()` | O(1) | O(n)** |
| `remove()` | O(1) | O(n)** |

\* where k = length of the key string  
\** when all keys collide into one bucket

### Space Complexity

- **O(n)** where n = number of key-value pairs stored

### Why O(1) Average Case?

With a good hash function:
- Keys are distributed evenly across buckets
- Few collisions occur
- Direct bucket access is O(1)
- Dictionary lookup within bucket is O(1)

### Worst Case Scenario

If all keys hash to the same bucket:
- All n items are in one bucket
- Lookup requires searching through all n items
- Performance degrades to O(n) linear search

---

## Lab Exercises

### Exercise 1: Basic Operations

Test the fundamental operations:

```python
ht = HashTable()

# Add some data
ht.add('apple', 'red')
ht.add('banana', 'yellow')
ht.add('cherry', 'red')

# Look up values
print(ht.lookup('apple'))   # Should print: red
print(ht.lookup('banana'))  # Should print: yellow

# Update a value
ht.add('banana', 'green')
print(ht.lookup('banana'))  # Should print: green

# Remove a key
ht.remove('cherry')
print(ht.lookup('cherry'))  # Should print: None
```

---

### Exercise 2: Test Collision Handling

Verify that collisions are handled correctly:

```python
ht = HashTable()

# These may collide (test with anagrams)
ht.add('listen', 'value1')
ht.add('silent', 'value2')

# Both should be retrievable
assert ht.lookup('listen') == 'value1'
assert ht.lookup('silent') == 'value2'

# Remove one shouldn't affect the other
ht.remove('listen')
assert ht.lookup('listen') is None
assert ht.lookup('silent') == 'value2'

print('✓ Collision handling works correctly')
```

---

### Exercise 3: Edge Cases

Test boundary conditions:

```python
ht = HashTable()

# Test 1: Lookup in empty table
assert ht.lookup('nonexistent') is None

# Test 2: Remove from empty table
ht.remove('nonexistent')  # Should not crash

# Test 3: Add and immediate remove
ht.add('temp', 'value')
ht.remove('temp')
assert ht.lookup('temp') is None

# Test 4: Update same key multiple times
ht.add('counter', 1)
ht.add('counter', 2)
ht.add('counter', 3)
assert ht.lookup('counter') == 3

print('✓ All edge cases handled correctly')
```

---

### Exercise 4: Build a Phone Book

Create a practical application:

```python
def phone_book_demo():
    phonebook = HashTable()
    
    # Add contacts
    phonebook.add('Alice', '555-0101')
    phonebook.add('Bob', '555-0102')
    phonebook.add('Charlie', '555-0103')
    
    # Look up a number
    name = 'Alice'
    number = phonebook.lookup(name)
    if number:
        print(f"{name}'s number: {number}")
    else:
        print(f"{name} not found")
    
    # Update a number
    phonebook.add('Bob', '555-9999')
    print(f"Bob's new number: {phonebook.lookup('Bob')}")
    
    # Remove a contact
    phonebook.remove('Charlie')
    print(f"Charlie after removal: {phonebook.lookup('Charlie')}")

phone_book_demo()
```

---

### Exercise 5: Analyze Hash Distribution

Study how keys distribute across buckets:

```python
def analyze_distribution():
    ht = HashTable()
    
    words = ['apple', 'banana', 'cherry', 'date', 'elderberry',
             'fig', 'grape', 'honeydew', 'kiwi', 'lemon']
    
    for word in words:
        ht.add(word, f'{word} value')
        hash_val = ht.hash(word)
        print(f'{word:12} -> hash: {hash_val}')
    
    print(f'\nTotal buckets used: {len(ht.collection)}')
    print(f'Total items stored: {len(words)}')
    
    # Check for collisions
    for hash_val, bucket in ht.collection.items():
        if len(bucket) > 1:
            print(f'Collision at {hash_val}: {list(bucket.keys())}')

analyze_distribution()
```

---

## Testing Framework

### Complete Test Suite

```python
def run_tests():
    print('Running Hash Table Tests...\n')
    
    # Test 1: Basic add and lookup
    print('Test 1: Basic Operations')
    ht = HashTable()
    ht.add('key1', 'value1')
    assert ht.lookup('key1') == 'value1'
    print('✓ Passed\n')
    
    # Test 2: Update existing key
    print('Test 2: Update Key')
    ht.add('key1', 'new_value')
    assert ht.lookup('key1') == 'new_value'
    print('✓ Passed\n')
    
    # Test 3: Remove key
    print('Test 3: Remove Key')
    ht.remove('key1')
    assert ht.lookup('key1') is None
    print('✓ Passed\n')
    
    # Test 4: Lookup non-existent key
    print('Test 4: Missing Key')
    assert ht.lookup('nonexistent') is None
    print('✓ Passed\n')
    
    # Test 5: Multiple keys
    print('Test 5: Multiple Keys')
    ht.add('a', 1)
    ht.add('b', 2)
    ht.add('c', 3)
    assert ht.lookup('a') == 1
    assert ht.lookup('b') == 2
    assert ht.lookup('c') == 3
    print('✓ Passed\n')
    
    # Test 6: Collision handling
    print('Test 6: Collisions')
    ht2 = HashTable()
    ht2.add('listen', 'v1')
    ht2.add('silent', 'v2')
    assert ht2.lookup('listen') == 'v1'
    assert ht2.lookup('silent') == 'v2'
    print('✓ Passed\n')
    
    print('All tests passed! ✓')

if __name__ == '__main__':
    run_tests()
```

---

## Lab Questions

### Conceptual Questions

1. **Why do anagrams produce the same hash in this implementation?**
   - Because the hash function sums ASCII values
   - Letter order doesn't matter, only which letters are present

2. **What's the advantage of using nested dictionaries for collision handling?**
   - O(1) lookup within buckets (dictionaries are hash tables themselves)
   - Better than lists which require O(n) linear search

3. **When would this hash table perform poorly?**
   - When many keys are anagrams
   - When keys have similar character compositions
   - When all keys happen to sum to the same value

4. **How could you improve the hash function?**
   - Consider character position: `hash = hash * 31 + ord(c)`
   - Use a larger prime number multiplier
   - Apply modulo to limit hash range

---

### Coding Challenges

#### Challenge 1: Add a Size Method

Implement a method that returns the number of items:

```python
def __len__(self):
    total = 0
    for bucket in self.collection.values():
        total += len(bucket)
    return total

# Test it
ht = HashTable()
ht.add('a', 1)
ht.add('b', 2)
print(len(ht))  # Should print: 2
```

---

#### Challenge 2: Add an Items Method

Return all key-value pairs:

```python
def items(self):
    all_items = []
    for bucket in self.collection.values():
        for key, value in bucket.items():
            all_items.append((key, value))
    return all_items

# Test it
ht = HashTable()
ht.add('a', 1)
ht.add('b', 2)
print(ht.items())  # [('a', 1), ('b', 2)]
```

---

#### Challenge 3: Improve the Hash Function

Implement a better hash that considers position:

```python
def hash(self, string):
    hash = 0
    for i, c in enumerate(string):
        hash = (hash * 31 + ord(c)) % (10**9 + 9)
    return hash

# Test: 'listen' and 'silent' should now have different hashes
```

---

#### Challenge 4: Add Clear Method

Remove all items from the hash table:

```python
def clear(self):
    self.collection = {}

# Test it
ht = HashTable()
ht.add('a', 1)
ht.add('b', 2)
ht.clear()
assert ht.lookup('a') is None
```

---

#### Challenge 5: Implement Contains

Check if a key exists:

```python
def __contains__(self, key):
    return self.lookup(key) is not None

# Test it
ht = HashTable()
ht.add('name', 'Alice')
print('name' in ht)     # True
print('email' in ht)    # False
```

---

## Common Mistakes to Avoid

### Mistake 1: Not Creating Buckets

```python
# ❌ Wrong - will crash
def add(self, key, value):
    computed_hash = self.hash(key)
    self.collection[computed_hash][key] = value  # KeyError!

# ✓ Correct - check if bucket exists
def add(self, key, value):
    computed_hash = self.hash(key)
    if computed_hash not in self.collection:
        self.collection[computed_hash] = {}
    self.collection[computed_hash][key] = value
```

---

### Mistake 2: Not Checking for Key Existence

```python
# ❌ Wrong - may crash
def remove(self, key):
    computed_hash = self.hash(key)
    del self.collection[computed_hash][key]  # May raise KeyError

# ✓ Correct - check before deleting
def remove(self, key):
    computed_hash = self.hash(key)
    if computed_hash in self.collection:
        if key in self.collection[computed_hash]:
            del self.collection[computed_hash][key]
```

---

### Mistake 3: Returning Wrong Value for Missing Keys

```python
# ❌ Wrong - should return None
def lookup(self, key):
    computed_hash = self.hash(key)
    return self.collection[computed_hash][key]  # May crash

# ✓ Correct - return None if not found
def lookup(self, key):
    computed_hash = self.hash(key)
    if computed_hash in self.collection:
        if key in self.collection[computed_hash]:
            return self.collection[computed_hash][key]
    return None
```

---

## Visualization

### How the Hash Table Looks Internally

```python
ht = HashTable()
ht.add('cat', 'meow')    # hash('cat') = 312
ht.add('dog', 'woof')    # hash('dog') = 314
ht.add('act', 'perform') # hash('act') = 312 (collision with 'cat')

# Internal structure:
# {
#     312: {
#         'cat': 'meow',
#         'act': 'perform'  ← Collision handled
#     },
#     314: {
#         'dog': 'woof'
#     }
# }
```

---

## Resources for Learning More

### Hash Functions
- Study different hash algorithms (DJB2, FNV, MurmurHash)
- Learn about cryptographic vs non-cryptographic hashes
- Understand hash distribution and collision rates

### Collision Resolution
- **Separate Chaining** (this lab's approach)
- **Open Addressing** (linear probing, quadratic probing)
- **Double Hashing**

### Advanced Topics
- Load factors and dynamic resizing
- Perfect hashing
- Consistent hashing (distributed systems)

---

## Conclusion

Congratulations! You've implemented a working hash table from scratch. You now understand:

✅ How hash functions map keys to indices  
✅ How collision resolution works  
✅ Why hash tables are O(1) on average  
✅ The trade-offs between simplicity and performance  

This knowledge is fundamental to understanding:
- Python dictionaries
- Database indexing
- Caching systems
- Symbol tables in compilers

---

## Next Steps

1. **Complete all exercises** in this lab
2. **Attempt all coding challenges**
3. **Experiment** with different hash functions
4. **Profile performance** with different data sets
5. **Extend** the implementation with new features

---

## Submission Checklist

- [ ] Implemented all required methods
- [ ] All test cases pass
- [ ] Completed at least 3 coding challenges
- [ ] Answered conceptual questions
- [ ] Tested with collision scenarios
- [ ] Code is well-commented
- [ ] README is updated with findings

---

## License

This project is provided for educational purposes.

---

## Author

Created as an educational lab for learning data structures and algorithms.
