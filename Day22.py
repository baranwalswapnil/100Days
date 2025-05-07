# marks=[0,1,2,3,4,5,"Hello",7]
# # print(type(marks))
# print(marks[1:4])
# print(marks[-3])
# print(marks[1:-3])
# print(marks[3])

# if 5 in marks:
#     print("Yes")
# else:
#    print("No")

# if "Ha" in marks:
#   print("Yes")
# else:
#   print("No")

# print(marks)
# print(marks[1:10:2])

# names = ["Milo", "Sarah", "Bruno", "Anastasia", "Rosa"]
# namesWith_O = [item for item in names if "o" in item]
# print(namesWith_O)

# names = ["Milo", "Sarah", "Bruno", "Anastasia", "Rosa"]
# namesWith_O = [item for item in names if (len(names)>4)]
# print(namesWith_O)


lst = [i for i in range(10)]
print(lst)
lst = [i*i for i in range(10) if i%2==0]
print(lst)

# lens=[1,2,3,4,5,6,7,8,9,10,11,12]
# for i in lens:
#    if (i<10):
#        print("Yes")
#    else:
#     print("No")

                ######################Bakchodi##################################
# lens = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

# if len(lens) > 10:  # Check if the length of the list is greater than 10
#     print("No")
# else:
#     print("Yes")