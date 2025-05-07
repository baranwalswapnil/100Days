################DEFAULT Function Argument#####################
# # def average(c=9, d=1):
# #  print("The average is", (c+d)/2)

# average()
# average(c=3)
########################ex2############################
# def name(fname, mname, lname="Jha"):
#  print(fname,mname,lname)

# name(fname="Swapnil", mname="Baranwal",)

#########################Keyword Arguement#######################

# def name(fname, mname, lname="Jha"):
#  print(fname,mname,lname)

# name(mname="Swapnil", fname="Baranwal",)

##############example 2😂##############################

# def name(fname, mname, lname):
#     print("Hello,", fname, mname, lname)

# name("Peter", "Quill")

#####################Variable Lengt Arguement###############


# def average(*numbers):
#     sum = 0
#     for i in numbers:
#        sum = sum + i
#     print("The average is", sum/len(numbers))

# average(2,2,2,2,2)

#####################Example 2######################################
# def name(**name):
#     print("Hello", name["fname"], name["mname"], name["lname"])

# name(mname= "Buchanan", lname= "Barnes", fname= "James")

#####################Example 3#####################################

def average(*numbers):
    sum = 0
    for i in numbers:
       sum = sum + i
    return("The average is", sum/len(numbers))

a=average(2,2,2,2,2)
print(a)