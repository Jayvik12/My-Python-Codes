def add (a, b):
    output = a + b
    return output

# def add (a, b):
#     return a + b

# x = 10
# y = 20
# temp = add (x, y) #this value gets copied into above a , b
# print (temp)

a = input("Enter value for a : ")
b = input ("Enter value for b : ")


temp = add (int(a), int(b)) 
print (temp)