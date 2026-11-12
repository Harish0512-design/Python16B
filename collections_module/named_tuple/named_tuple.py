# 1. namedtuple():
# ----------------

# 1. A normal tuple is immutable, light weight (memory efficient) but not self-descriptive.
person =('Harish', 27, 'Developer')
print(person[0]) # person's name
print(person[1]) # age
print(person[2]) # role

# Here I need to remember the position of each field, makes hard to read and maintain. You can't give meaningful names

# 2. That's why python introduced namedtuple()
# 3. namedtuple() is a factory function for creating tuple subclasses with named fields
# 4. provides readability like a class and efficiency as a tuple
# 5. namedtuple() uses tuple() under the hood to store values in a fixed structure like tuple not __dict__ like class as it requires extra memory.
# 6. so, no __dict__ which means less RAM Usage (memory efficient)
# 7. Attribute access is O(1), same as tuple indexing, faster than dict lookup.
# 8. namedtuple() is 2-5 times smaller in memory than equivalent class, must faster than a class.

# Advantages:
#------------
# 1. Readable code: Access fields by name instead of index
# 2. Immutable: like tuples - safe for hash keys and data integrity.
# 3. LightWeight: memory efficient, faster than classes
# 4. support tuple operations: you can unpack, iterate, compare
# 5. self-documenting: Field names describe data clearly.

# Disadvantages:
# --------------
# 1. Immutable
# 2. Not suitable for complex objects
# 3. Verbose for many fields: If too many attributes -> use dataclasses instead (python 3.7+)


# Usecases:
#-----------
# ✅ Representing structured data:	            Points, employees, students, transactions
# ✅ Returning multiple values from a function:	Better than returning a tuple
# ✅ Replacing simple data classes:	            When you need immutability and readability
# ✅ Data records from databases / CSVs:	        For fixed schema tabular data
# ✅ Lightweight configuration objects:	        Without creating full class definitions


from collections import namedtuple


# Creating a namedtuple()
Person = namedtuple('Person2', ['name', 'age', 'role'], defaults=['Unknown'])

# creating instances
p1 = Person('Harish', 27, 'Developer')
print(p1)
# output: Person2(name='Harish', age=27, role='Developer')

p2 = Person('Harish2', 27)
print(p2)
# output: Person2(name='Harish2', age=27, role='Unknown')

print(type(p2))
# output: <class '__main__.Person2'>

print(p1._fields)
# output: ('name', 'age', 'role')

print(p1._asdict())
# output: {'name': 'Harish', 'age': 27, 'role': 'Developer'}
# output (Before python 3.7+): OrderedDict([('name', 'Harish'), ('age', 30), ('role', 'Developer')])

print(p1._replace(age=28)) # creates a new object with a copy of old and updates the required fields
# output: Person2(name='Harish', age=28, role='Developer')
print(p1._field_defaults)
# output: {'role': 'Unknown'}

# Creates a new instance from an iterable
p3 = Person._make(['Harish3', 10, 'Tester'])
print(p3)
# output: Person2(name='Harish3', age=10, role='Tester')