i =input("Enter the input: ")
print(f"Here is the table of {i}")
for a in range(1,11):
   try:
      print(f" {int(i)} x {a} = {(i*a)}")
   except:
        print("Please Enter an Integer")
   