# with open('file2.txt', 'r') as f:
#     f.seek(5)
#     print(f.read(3))
#     print(type(f))
#     print(f.tell())


#############################################

with open('file2.txt', 'w') as f:
    f.write("Hello Harry")
    f.truncate(5)
    
with open('file2.txt', 'r') as f:
    print(f.read())