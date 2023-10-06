############################ 1. Right Half Pyramid ######################################

# *
# * *
# * * *
# * * * *
# * * * * *

# n = int(input())
# for row in range(n+1):
#     for col in range(row):
#         print('*', end=" ")
#     print()

############################# 2. Left half Pyramid ####################################

#     *
#    **
#   ***
#  ****
# *****

# n = int(input())
# for row in range(1,n+1):
#     for col in range(n-row):
#         print(" ", end="")
#     print("*"*row)


############################# 3. Full Pyramid ####################################

#     *
#    * *
#   * * *
#  * * * *
# * * * * *

# n = int(input())
# for row in range(1,n+1):
#     for col in range(n-row):
#         print(" ", end="")
#     print("* "*row)

############################# 4. Inverted Right Half Pyramid ####################################

# * * * * * 
# * * * * 
# * * * 
# * * 
# *

# n = int(input())
# for row in range(n+1):
#     for col in range(n-row):
#         print("*", end=" ")
#     print()

############################# 5. Inverted Right Half Pyramid ####################################

# *****
#  ****
#   ***
#    **
#     *

# n = int(input())
# for row in range(n+1):
#     for col in range(row):
#         print(" ", end="")
#     print("*"*(n-row))


############################# 6. Inverted Full Pyramid ####################################

# * * * * *
#  * * * *
#   * * *
#    * *
#     *

# n = int(input())
# for row in range(n):
#     for col in range(row):
#         print(" ", end="")
#     print("* "*(n-row))

############################# 7. Rhombus Pattern ####################################

# * * * * 
#  * * * * 
#   * * * * 
#    * * * * 
#     * * * *

# n = int(input())
# for row in range(n):
#     for col in range(row):
#         print(" ", end="")
#     print("* "*(n-1))


############################# 8. Diamond  Pattern ####################################

#     *
#    * *
#   * * *
#  * * * *
# * * * * *
# * * * * *
#  * * * *
#   * * *
#    * *
#     *

# n = int(input())
# for row in range(1,n+1):
#     for col in range(n-row):
#         print(" ", end="")
#     print("* "*row)

# for row in range(n):
#     for col in range(row):
#         print(" ", end="")
#     print("* "*(n-row))


############################# 9. Hourglass  Pattern ####################################

# * * * * *
#  * * * *
#   * * *
#    * *
#     *
#     *
#    * *
#   * * *
#  * * * *
# * * * * *

# n = int(input())
# for row in range(n):
#     for col in range(row):
#         print(" ", end="")
#     print("* "*(n-row))

# for row in range(1,n+1):
#     for col in range(n-row):
#         print(" ", end="")
#     print("* "*row)


############################# 10. Hollow Square  Pattern ####################################

# * * * * * 
# *       *
# *       *
# *       *
# * * * * * 

# n = int(input())
# for row in range(n):
#     if row == 0 or row == 4:
#         print("* "*n)
#     else:
#         print("* " + "  "*(n-2) + "*")


############################# 11. Hollow Full Pyramid ####################################

#      *
#     * *
#    *   *
#   *     *
#  *********

# n = 5
# for i in range(n):
#     for j in range(n-i):
#         print(' ', end='') 
#     for j in range(2*i+1):
#         if j==0 or j==2*i or i==n-1:
#             print('*',end='')
#         else:
#             print(' ', end='')
#     print()
    
    

############################# 12. Floyd's Triangle ####################################
# 1 
# 2 3
# 3 4 5
# 4 5 6 7

# n = 5
# for i in range(1,n):
#     for j in range(i,i+i):
#         print(j, end=" ")
#     print()


# 1
# 2 3
# 4 5 6
# 7 8 9 10

# n =5
# c = 1
# for i in range(n):
#     for _ in range(i):
#         print(c,end=" ")
#         c += 1
#     print()


#################################### 13. Palindrome Triangle #################################################
#       1
#     2 1 2
#   3 2 1 2 3
# 4 3 2 1 2 3 4
    
n = int(input("enter numbers "))
m = n*2
for i in range(1,n):
    for j in range(n-i):
        print(' ',end=' ')

    for j in range(i,0,-1):
        print(j, end=' ')

    for j in range(2,i+1):
        print(j, end=" ")
    
    print()
    
    
            



        







