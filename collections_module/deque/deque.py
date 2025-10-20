# Why 'deque' was introduced?
# -----------------------------
# Python's built-in list can be used as Queue(FIFO) and Stack(LIFO) but it's inefficient in certain cases.
# suppose, lst.append() -> o(1), lst.pop() -> o(1), 
# but, lst.pop(0), lst.insert(1, 3) -> o(n), because all other elements need to be shifted in memory.


# Deque is a double ended queue which allows fast appends and pops from both ends. o(1)

# UseCase of Deque:
# ------------------
# FIFO Queue:	Implementing task queues (e.g., processing requests)
# LIFO Stack:	Implementing undo/redo or backtracking
# Sliding Window:	For moving averages, max/min in time series
# Breadth-First Search (BFS):	Queue operations in graph/tree algorithms
# Rate Limiter / Log Buffer:	Keep last n operations efficiently
# Message Handling Systems:	Store and consume messages quickly

# Core Operations:
# 1.append(x)	          :  Add to right end	             O(1)
# 2.appendleft(x)	      :  Add to left end	             O(1)
# 3.pop()	              :  Remove from right end	         O(1)
# 4.popleft()	          :  Remove from left end	         O(1)
# 5.extend(iterable)	  :  Add multiple items to right	 O(k)
# 6.extendleft(iterable)  :	Add multiple items to left	     O(k)
# 7.clear()	              : Remove all elements	             O(n)
# 8.rotate(n)	          : Rotate elements right (n>0) or left (n<0)	O(k)
# 9.reverse()	          : Reverse the deque in place	      O(n)


from collections import deque

# deque creation
d = deque()

print(d)
# output: deque([])
