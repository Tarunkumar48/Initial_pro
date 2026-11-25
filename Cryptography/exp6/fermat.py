import random
import time

n = int(input("Enter an integer: "))  # Read integer n
start = time.time()  # Record start time

# Check primality using Fermat's test
if n <= 1:
    print("Composite")
elif n == 2 or n == 3:
    print("Prime")
elif n % 2 == 0:
    print("Composite")
else:
    a = random.randint(2, n - 2)  # Choose random a in [2, n-2]
    print(a)
    result = pow(a, n - 1, n)  # Compute a^(n-1) mod n
    if result != 1:
        print("Composite")
    else:
        print("Probably Prime")

end = time.time()  # Record end time

print("Execution time =", end - start, "seconds")  
