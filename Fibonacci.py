# Fibonacci sequence in Python

# Take input from user
n = int(input("Enter the number of terms: "))

# First two terms
a, b = 0, 1

print("Fibonacci sequence:")
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b
