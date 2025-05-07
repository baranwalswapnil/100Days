# a = int(input("Enter the input: "))
# print(f"Multiplication of {a} is")
# #

# # for i in range(1,11):
# #     print((a) * (i+1))

# for i in range(1,11):
#     print(f"{a} X {i}= {a*(i)}")

# a = input("Enter you Input Data: ")
# try:
#    for i in range(1,11):
#       print(f"{(a)} X {i} is = {int(a)* i}")
# except:
#        print("Enter an integer")

# 

while True:
    a = input("Enter your Input Data: ")
        
    try:
        num = int(a)
        for i in range(1, 11):
            print(f"{num} X {i} is = {num * i}")
    except:
        print("Error: Please enter an integer")
    
    print() 