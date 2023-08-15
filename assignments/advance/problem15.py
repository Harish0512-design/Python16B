# 15)Program to create and insert data into a text file.
# filehanding


# creating a new file
# f = open(r"/file.txt", "x")
# f.write("Hello World")
# f.close()
#
# f = open(r"/file.txt", "r")
# print(f.read())
# f.close()
#
# f = open(r"/file.txt", "a")
# f.write("El Niño")
# f.close()
#
# f = open(r"/file.txt", "r")
# print(f.read())
# f.close()
#
# f = open(r"/file.txt", "a")
# f.write("new Hello World2")
# f.close()
#
# f = open(r"/file.txt", "r")
# print(f.read())
# f.close()

# f = open(r'D:\SVU projects\tweaktechtechnologies\file.txt')
# print(f.tell())
# print(f.read())
# print(f.tell())
# f.close()
#
# book = {}
# book['tom'] = {
#     "name": "Tom",
#     "address": "1b, green street, NY"
# }
# book['john'] = {
#     "name": "John",
#     "address": "3b, green street, NY"
# }
# book['tim'] = {
#     "name": "Tim",
#     "address": "2b, green street, NY"
# }
#
# import json
#
# with open(r'D:\SVU projects\tweaktechtechnologies\file.txt', "w") as f:
#     k = json.dump(book, f)
#     print(type(k))
#
# s = json.dumps(book)
# print(type(s))
