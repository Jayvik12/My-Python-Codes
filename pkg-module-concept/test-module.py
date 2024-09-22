# import calc

# # # When giving value directly
# var1 = calc.add(10,20)
# print(var1)
# print(calc.__name__)

# another way to give variable
# i = 10
# j = 20
# var1 = calc.add(i,j)
# print(var1)

# from calc import add

# l=10
# m = 20
# var = add (l,m)
# print(var)

from mypkg.calc import add , sub

sum = add(40,20)
print(sum)
sub = sub(40,20)
print(sub)