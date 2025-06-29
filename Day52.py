# def double(x):
#     return x*2

# print(double(5))

#######################

# double = lambda x: x*2

# print(double(5))

#######################

def appl(fx, value):
    return 6+fx(value)
# def add(x, appl):
#     return x + 1

# print(appl(add, 4))



########################


def appl(fx, value):
    return 6+fx(value)

print(appl(lambda x: x+1, 4))
