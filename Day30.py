# def factorial(n):
#     if (n == 0 or n == 1):
#        return 1
#     else:
#         return n * factorial(n-1)

# n = int(input("Enter the input: "))

# print(factorial(n))

def fibonacci_sequence(np):
    if (np == 0):
        return 0
    elif (np ==1):
        return 1
    else:
        return (np - 1) + (np - 2)

np = int(input("Enter the input: "))

print(fibonacci_sequence(np))