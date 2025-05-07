# a= int(input("What is ypour age: "))
# print("Your age is", a )

# # Conditional Operators
# # <,>,>=,<=,==,!=
# print(a<18)
# print(a>18)
# print(a<=18)
# print(a>=18)
# print(a==18)
# print(a!=18)

# if (a>17):
#     print("You can drive")
# else: 
#     print("You Can't drive")

# print()



# appleprice = 10
# budget = int(input("Enter the input: "))

# if (0< budget - appleprice <50):
#     print("Alexa add 1 kg apple to cart")
# elif (budget - appleprice >70):
#     print("It's okay you can buy more tha 1 kg")
# else:
#     print("You can't buy")

print()

num= int(input("Enter the value of num: "))
if (num<0):
    print("The given number is negative")
elif(num==0):
    print("The given number is 0")
else:
    print("The given number is positive")
print()


num = int(input("Enter the input: "))
if (num < 0):
    print("Number is negative.")
elif (num > 0):
    if (num <= 10):
        print("Number is between 1-10")
    elif (num > 10 and num <= 20):
        print("Number is between 11-20")
    else:
        print("Number is greater than 20")
else:
    print("Number is zero")
