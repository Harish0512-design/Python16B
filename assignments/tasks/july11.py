# 1.Take values of length and breadth of a rectangle from user and check if it is square or not.
# length = int(input("Enter length "))
# breadth = int(input("Enter breadth "))
# if length == breadth:
#     print("Square")
# else:
#     print("not a square")

#
# 2. Take two int values from user and print greatest among them.

# num1 = int(input("Enter a number "))
# num2 = int(input("Enter another number "))
#
# if num2 > num1:
#     print(f"{num2} is greater than {num1}")
#
# elif num2 == num1:
#     print(f"{num1} is equal to {num2}")
#
# else:
#     print(f"{num1} is greater than {num2}")

# 3. A shop will give discount of 10% if the cost of purchased quantity is more than 1000.
# Ask user for quantity
# Suppose, one unit will cost 100.
# Judge and print total cost for user.

# cost_per_unit = 100
# quantity = int(input("Please enter quantity: "))
# total = quantity * cost_per_unit
# if total > 1000:
#     total = total - (0.1 * total)
# print(total)

# 4. A company decided to give bonus of 5% to employee if his/her year of service is more than 5 years.
# Ask user for their salary and year of service and print the net bonus amount.
# salary = float(input("Enter your salary "))
# service = int(input("Enter your service in years "))
#
# if service > 5:
#     net_bonus = (salary * 0.05)
# else:
#     net_bonus = 0
# print(net_bonus)

# 5. A school has following rules for grading system:
# a. Below 25 - F
# b. 25 to 45 - E
# c. 45 to 50 - D
# d. 50 to 60 - C
# e. 60 to 80 - B
# f. Above 80 - A
# Ask user to enter marks…
# marks = int(input("Enter marks"))
# if marks < 25:
#     print("F")
# elif 25 < marks < 45:
#     print("E")
# elif 45 < marks < 50:
#     print("D")
# elif 50 < marks < 60:
#     print("C")
# elif 60 < marks < 80:
#     print("B")
# else:
#     print("A")
# 6. Take input of age of 3 people by user and determine oldest and youngest among them.
# age1 = int(input("Enter age1 "))
# age2 = int(input("Enter age2 "))
# age3 = int(input('Enter age3 '))
# oldest = max(age1, age2, age3)
# youngest = min(age1, age2, age3)
# print(f"{oldest} is the oldest one among {age1}, {age2}, {age3}")
# print(f"{youngest} is the youngest one among {age1}, {age2}, {age3}")

# 7. Write a program to print absolute vlaue of a number entered by user. E.g.-
# INPUT: 1        OUTPUT: 1
# INPUT: -1        OUTPUT: 1
# input_val = int(input())
# print(abs(input_val))

# 8. A student will not be allowed to sit in exam if his/her attendence is less than 75%.
# Take following input from user
# Number of classes held
# Number of classes attended.
# And print
# percentage of class attended
# Is student is allowed to sit in exam or not.

# no_of_classes_held = int(input("Enter no. of classes held "))
# no_of_classes_attended = int(input("Enter no. of classes attended "))
#
# attendance_percentage = (no_of_classes_attended / no_of_classes_held) * 100
# print(attendance_percentage)
# if attendance_percentage < 75:
#     print("Not allowed to exam")
# else:
#     print("Allowed to exam")


# 9. Modify the above question to allow student to sit if he/she has medical cause.
# Ask user if he/she has medical cause or not ( 'Y' or 'N' ) and print accordingly.

# no_of_classes_held = int(input("Enter no. of classes held "))
# no_of_classes_attended = int(input("Enter no. of classes attended "))
# had_medical_cause = input("Did Student had any medical cause? ('Y' or 'N') ")
#
# attendance_percentage = (no_of_classes_attended / no_of_classes_held) * 100
# print(attendance_percentage)
#
# if attendance_percentage < 75:
#     if had_medical_cause == 'Y':
#         print("Allowed to exam")
#     else:
#         print("Not allowed to exam")
# else:
#     print("Allowed to exam")


# 10. If
# x = 2
# y = 5
# z = 0
# then find values of the following expressions:
# a. x == 2
# b. x != 5
# c. x != 5 && y >= 5
# d. z != 0 || x == 2
# e. !(y < 10)

# x = 2
# y = 5
# z = 0
# print(x==2)
# print(x != 5)
# print(x != 5 and y >= 5)
# print(z != 0 or x == 2)
# print(not (y<10))

# 11. How to find the greatest amoung three numbers?
# num1 = int(input())
# num2 = int(input())
# num3 = int(input())
#
# if num1 > num3 and num1 > num2:
#     print("num1 is greater")
# elif num2 > num1 and num2 > num3:
#     print("num2 is greater")
# else:
#     print("num3 is greater")
# 12. How to find the smallest amoung three numbers?
# num1 = int(input())
# num2 = int(input())
# num3 = int(input())
#
# if num1 < num3 and num1 < num2:
#     print("num1 is smallest")
# elif num2 < num1 and num2 < num3:
#     print("num2 is smallest")
# else:
#     print("num3 is smallest")

# Exercise on for loop:
#
# 1.print the sum and product from 1 to 20.

# sum_of_numbers = 0
# product_of_numbers = 1
# for i in range(1, 21):
#     sum_of_numbers += i
#     product_of_numbers *= i
# print(sum_of_numbers)
# print(product_of_numbers)

# 2.print the numbers which is not divisible by 3 , from 1 to 20.

# for i in range(1, 20):
#     if i % 3 != 0:
#         print(i)

# 3.print even numbers between 1 and 20.

# for i in range(1, 21):
#     if i % 2 ==0:
#         print(i)

# 4.print average of numbers from 1 to 20 (should work for any numbers)

# start = int(input())
# end = int(input())
# count = 0
# sum_of_numbers = 0
# for i in range(start, end + 1):
#     count += 1
#     sum_of_numbers += i
# print("The average of numbers in given range is ", (sum_of_numbers / count))

# 5.for numbers from 1 to 20
#    check if the number is divisible by 2,3 or 5
#    or all the three
#    or none of the three
#    (should work for any range of numbers)
#
# start = int(input())
# end = int(input())
# for i in range(start, end + 1):
#     if i % 2 == 0 and i % 3 == 0 and i % 5 == 0:
#         print(i, " is divisible by 2, 3, and 5")
#     elif i % 2 == 0 or i % 3 == 0 or i % 5 == 0:
#         print(i, " is divisible by either 2 or 3 or 5")
#     else:
#         print(i, " is not divisible by any of 2, 3 ,5")


# generators

# def func(lst):
#     for i in lst:
#         # print(i)
#         yield i
#         print("Hii")
#
#
# res = func([1, 2, 3, 4, 5])
# print(res)
# print(func([1,2,3,4,5]))
# for v in res:
#     print(v)

l = []
# d = {}
# import sys
#
# print(sys.getsizeof(l))
# print(sys.getsizeof(d))
