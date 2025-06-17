while True :
 a = input("Enter the input: ")

 key = input("Enter your Key: ")

 b= input(str("Do you wana encode or decode: " )).lower()
 print(b)

 if b == "encode":
   result = a + key
   print("Encoded:", result)
 elif b == "decode":
   De= a.replace(key, "" )
   print(De)
 else :
  print("Enter valid data")