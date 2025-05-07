#5-12 Good Morning
#12-18 Good Afternoon
#18-22 Good Evening
#22-5 Good Night
a=int(input("What is time right now in 24 hr : "))
if(5<a<12):
    print("Good Morning")
elif(a>12):
    if(18>a>12):
       print("Good Afternoon")
    elif(22>a>18):
        print("Good Evening")
else:
    print("Good Night")

print()
print()