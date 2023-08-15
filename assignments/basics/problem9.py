# 9.Write a function to check if a number is prime or not.
def check_prime_or_not(number):
    for i in range(2, (number // 2) + 1):
        if number % i == 0:
            print("Not a prime number")
            break
    else:
        print("Is a prime number")

        #
        # for i in range(2, 50):
        #     if check_prime_or_not(i):
        #         print(i, end=",")


print(check_prime_or_not(12))
print(check_prime_or_not(13))
