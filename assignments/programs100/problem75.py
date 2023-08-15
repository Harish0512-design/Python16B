# Please write a program to output a random even number between 0 and 10
# inclusive using random module and list comprehension.
# Hints:
# Use random.choice() to a random element from a list.

import random

print(random.choice(list(range(10))))
print(random.choice([x for x in range(10)]))
print(random.choices([x for x in range(10)]))
