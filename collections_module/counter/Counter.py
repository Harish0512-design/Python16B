# Counter is a subclass of Python’s built-in dict class, part of the collections module.
# It’s specifically designed for counting immutable hashable objects — like words, characters, or any kind of item.
# It gives count of elements in decending order.
# ❌ Not thread-safe

# How It Works Internally?
# Counter is just a dictionary subclass (dict under the hood).
# Keys = items being counted.
# Values = integer counts.
# When you increment an item’s count, it just performs: 
# counter[item] = counter.get(item, 0) + 1

# Performance Benefits:
# Highly optimized C-level implementation → faster than manual counting.
# Memory-efficient compared to defaultdict(int).
# Handles missing keys gracefully.
# Methods and Operations on Counter


# Before Counter, people used to manually count using loops and dictionaries:
data = ["apple", "apple", "orange", "orange", "grapes", "apple"]
counts = {}
for item in data:
    counts[item] = counts.get(item, 0) + 1
print(counts)

# This was repetitive and error-prone.
# Counter automates that logic — clean, fast, and built-in.

from collections import Counter

data = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
counter = Counter(data)
print(counter)
# Counter({'apple': 3, 'banana': 2, 'orange': 1})


# 1. Counter Initialization:
empty_counter = Counter() # empty counter
iterable_counter = Counter([1,2,3,4,1,1,2])  # Counter({1: 3, 2: 2, 3: 1, 4: 1}) from iterable
dict_counter = Counter({"a": 4, "b": 3}) # Counter({'a': 4, 'b': 3}) from dict
kwargs_counter = Counter(a=4, b=3,c=1) # Counter({'a': 4, 'b': 3, 'c': 1}) from keyward args

# 2. Access
counter = Counter(['apple', 'apple', 'orange', 'dragonfruit'])
print(counter['apple']) # 2
print(counter['watermelon']) # 0

# 3. update()
counter = Counter(['apple', 'apple', 'orange', 'dragonfruit'])
print("Before Update: ", counter)
counter.update(['orange', 'orange', 'dragonfruit'])
print("After Update: ", counter)

# output:
# Before Update:  Counter({'apple': 2, 'orange': 1, 'dragonfruit': 1})
# After Update:  Counter({'orange': 3, 'apple': 2, 'dragonfruit': 2})

# 4. subtract()
counter = Counter(['apple', 'apple', 'orange', 'dragonfruit'])
print("Before Subtract: ", counter)

counter.subtract(['apple', 'dragonfruit'])

print("After Subtract: ", counter)

# Before Subtract:  Counter({'apple': 2, 'orange': 1, 'dragonfruit': 1})
# After Subtract:  Counter({'apple': 1, 'orange': 1, 'dragonfruit': 0})

# 5. most_common()
counter = Counter(['a','a','b','c','d','e','f','b'])
print(counter.most_common())  # [('a', 2), ('b', 2), ('c', 1), ('d', 1), ('e', 1), ('f', 1)]
print(counter.most_common(2)) # [('a', 2), ('b', 2)]

# 6. elements()
counter = Counter("aabbc")
iterator = counter.elements() # <itertools.chain object at 0x000001936268BF70>
print(list(iterator)) # ['a', 'a', 'b', 'b', 'c']

# 7. Counters support addition, subtraction, intersection & union based on counts.
c1 = Counter(a=3, b=1)
c2 = Counter(a=1, b=2)

print(c1 + c2)      # Counter({'a': 4, 'b': 3})
print(c1 - c2)      # Counter({'a': 2})
print(c1 & c2)     # Counter({'a': 1, 'b': 1})  # min counts
print(c1 | c2)      # Counter({'a': 3, 'b': 2})  # max counts

# 7. Deleting or Clearing
del counter['a'] # delets a element
counter.clear() # makes counter empty

# 8. convert to normal dict
dict(counter)

# 9. total()
counter = Counter(['a','a','b','b','b'])
print(counter.total()) # 5