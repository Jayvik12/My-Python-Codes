
# positional argument
# variable positional argument
# keyword argument
# variable keyword argument

## using *variable

# def add (a, b, c, *var):
#     print(a)
#     print(b)
#     print(c)
#     print(var)

# x = 10
# y = 20
# z = 30
# p = 1
# q = 2
# r = 3

# add(x,y,z,p,q,x)

# Using variable Keyword variable

# def add (a, b, c, *var, ssl=False, verbose=0):
    
#     print(a)
#     print(b)
#     print(c)
#     print(var)
#     print(ssl)
#     print(verbose)

# x = 10
# y = 20
# z = 30
# p = 1
# q = 2
# r = 3

# add(x, y, z, p, q, x, ssl=True, verbose=3 )

# using **(double star) variable

# def add (a, b, c, *var, ssl=False, verbose=0, **kvar):
    
#     print(a)
#     print(b)
#     print(c)
#     print(var)
#     print(ssl)
#     print(verbose)
#     print(kvar)

# x = 10
# y = 20
# z = 30
# p = 1
# q = 2
# r = 3

# add(x, y, z, p, q, x, ssl=True, verbose=3, abc="test1", xyz="test2", lmn="test3" )


# another way to write same code

def add (a, b, c, *var, ssl=False, verbose=0, **kvar):
    
    print(a)
    print(b)
    print(c)
    print(var)
    print(ssl)
    print(verbose)
    print(kvar)

x = 10
y = 20
z = 30
p = 1
q = 2
r = 3
data = {'abc': 'test1', 'xyz': 'test2', 'lmn': 'test3'}
add(x, y, z, p, q, x, ssl=True, verbose=3, **data )