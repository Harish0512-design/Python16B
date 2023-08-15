import re

# matcher = re.compile("ab").finditer("ababab")
# count = 0
# for match in matcher:
#     count += 1
#     print(str(match.start()) + "------------" + str(match.end()) + "-------" + match.group())
#
# print(count)

# l = re.split('\.', "www.google.com")
# print(l)

# l = re.split(',', "www,google,com")
# print(l)

# import re,urllib
# import urllib.request
#
# sites = "google rediff".split()
# print(sites)
# for s in sites:
#     print("Searching...", s)
#     u = urllib.request.urlopen("http://" + s + ".com")
#     text = u.read()
#     title = re.findall("<title>.*</title>", str(text), re.I)
#     print(title[0])


# for i in range(10):
#     if i == 10:
#         break
#     print(i)
# else:
#     print("Loop executed without breaking")

# i = 0
# while i<10:
#     if i == 12:
#         break
#     print(i)
#     i = i+1
# else:
#     print("Loop executed without breaking")

# limit = int(input())
# lst = []
# res = ""
# for _ in range(1, limit + 1):
#     lst.append(input())
# for i in lst:
#     res+=str(len(i))
#
# print(res)
