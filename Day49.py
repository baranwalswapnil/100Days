# f= open('file.txt', 'r') 
# # print(f)
# text= f.read()
# print(text)
# f.close()

# f= open('file.txt', 'w')
# text=f.write("This is write method")
# print(text)
# f.close()
with open('file.txt', 'r') as f:
    fb=f.read()
    print(fb)