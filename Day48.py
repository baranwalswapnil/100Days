x= 10

def my_function():
    global x
    x= 4
    y= 5
    print(y)

my_function()
print(y) #error since local var
print(x)