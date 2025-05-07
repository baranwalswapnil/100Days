while True:
 a= input("Enter an Input: ")
 try:
    for i in range (1,11):
        print(f'{int(a)} x {i} = {int(a)* (i)}')
 except:
    print("Enter an integer")
 finally:
    print("Code is Executed")