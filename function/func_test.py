# def add (a, b):
#     output = a + b
#     return output

## def add (a, b):
##     return a + b


# temp = add (10, 20) #passing arguments
# print (temp)

# #Multiple operations
def sub (a,b):
    output = a - b 
    return output

temp1 = sub (20,10)
print (temp1)


def mul (a, b):
    output = a * b
    return output

temp2 = mul (10,20)
print (temp2)    

# variation 1
def cal (a,b):
    add = a + 
    sub = a - b 
    mul = a * b
    return add, sub, mul

temp= cal(10,20)
print(temp)
temp1, temp2, temp3 = cal(10,20)
print (temp1, temp2, temp3)    

# variation 2
def multi(a, b):
    xyz = a * b , a + b , a * b
    return xyz

temp = multi(10 , 20)
print(temp)

for i in temp:
    print(i)