num_to_find = 10
count = 0

for i in range(5):
    count = count + 1
    if i == num_to_find:
        print("Number found")
        break
else:
    print("Number not found")
