import struct

lst = [1, 2, 3]

print(bytes(lst))

print(struct.calcsize('i'))
print(struct.calcsize('f'))
print(struct.calcsize('s'))
print(struct.calcsize('b'))
print(struct.calcsize('100s'))