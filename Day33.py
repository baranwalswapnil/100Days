A ={"a": "Hello"
    ,"b": "World"
    , 1:"is"}
# print(A)
# print(A[1]) #gives error when key is not present 
# print(A.get("b")) #Give none as output when an key is not found
# print(A.keys())
# print()
# # 
# # 
# for y in A.keys(): 
#     print(A[y])  #print values of the keys

# print(A.values())
# for val in A.values():
#     print(val)

# for key in A.keys():
#     print(f"The value correspondig to the key {key} is {A[key]}")

# for key in A.keys():
#     print(key)


print(A.items())

for key, value in A.items():
    print(f"The value corresponding to key {key} is {value}")