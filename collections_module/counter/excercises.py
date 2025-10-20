from collections import Counter


# 1. Word Frequency in Text
text = "Python easy to learn and python is great and easy."
words = text.lower().replace(',','').replace('.','').split()
counter = Counter(words)
print(counter) # Counter({'python': 2, 'easy': 2, 'and': 2, 'to': 1, 'learn': 1, 'is': 1, 'great': 1})


# 2. Character Frequency
word = "banana"
counter = Counter(word)
print(counter) # Counter({'a': 3, 'n': 2, 'b': 1})
print(dict(counter)) # {'b': 1, 'a': 3, 'n': 2}


# 3. Inventory Management
stock = Counter(apples=10, oranges=20)
order = Counter(apples=5, oranges=2)
remaining = stock - order
print(remaining) # Counter({'oranges': 18, 'apples': 5})


# 4. Log/Event Analysis
requests = ['200', '404', '200', '500', '404', '200']
print(Counter(requests)) # Counter({'200': 3, '404': 2, '500': 1})


# 5. Voting Systems
votes = ['Alice', 'Bob', 'Alice', 'Charlie', 'Alice']
print(Counter(votes).most_common(1)) # [('Alice', 3)]
