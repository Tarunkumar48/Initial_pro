# import time
# import math

# n = int(input("Enter an integer: "))  
# start = time.time() 

# if n <= 1:      # Check primality
#     print("Invalid")
#     # return False
# else:
#     prime = True
#     for i in range(2, int(math.sqrt(n)) + 1):  # Check divisibility up to √n
#         if n % i == 0:
#             prime = False
#             break
#     if prime:
#         print("Prime")
#     else:
#         print("Composite")

# end = time.time()  
# print("Execution time =", end - start, "seconds") 

import random

# def trial_division(n):
#     if n < 2:
#         return False
#     for i in range(2, int(n ** 0.5) + 1):
#         if n % i == 0:
#             return False
#     return True

# def fermat_test(n):
#     if n < 4:
#         return n in (2, 3)
#     a = random.randrange(2, n - 1)
#     return pow(a, n - 1, n) == 1

def miller_rabin(n):
    if n < 4:
        return n in (2, 3)
    d = n - 1
    while d % 2 == 0:
        d //= 2
    a = random.randrange(2, n - 1)
    x = pow(a, d, n)
    return x == 1 or x == n - 1

n = int(input("Enter number: "))
# print("Trial Division:", trial_division(n))
# print("Fermat:", fermat_test(n))
print("Miller-Rabin:", miller_rabin(n))

