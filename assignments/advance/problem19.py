# 19)Given an integer,n, perform the following conditional actions by creating two user-defined exceptions.
# If n is odd, raise Weird
# If n is even and in the inclusive range of 2 to 5, raise Not_Weird
# If n is even and in the inclusive range of 6 to 20, raise Weird
# If n is even and greater than 20, raise Not_Weird
# print weird if Weird exception raised and print not weird if Not_Weird exception

class WeirdException(Exception):
    pass


class NotWeirdException(Exception):
    pass


try:
    n = int(input())
    if n % 2 != 0:
        raise WeirdException
    else:
        if 2 <= n <= 5:
            raise NotWeirdException
        elif 6 <= n <= 20:
            raise WeirdException
        elif n > 20:
            raise NotWeirdException
except WeirdException as we:
    print("Weird")
except NotWeirdException as nwe:
    print("Not Weird")
