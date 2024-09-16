
"""
ip = input("Enter the IP address x.x.x.x (0-255) :")

newip = ip.split('.')


if int(newip [0]) == 10:
    print( "This is Class A Private IP")
        
elif int(newip [0]) == 172 and int(newip [1]) >= 16 and int(newip [1]) <= 31:
    print ( "This is a Class B Private IP")

elif int(newip [0]) == 192 and int(newip [1]) ==168:
    print ("This is clas C Private Ip")
    
else:
    print("This is not a valid Private IP Address")
    
 """   

#========================================================


    
ip = input("Enter the IP address x.x.x.x (0-255) :")

newip = ip.split('.')

if int(newip [0]) >=0 and int(newip [0] <= 255 and int(newip [1]) >=0 and int(newip [1]) <= 255 and int(newip [2]) >= 0 and int(newip [2]) <= 255 and int(newip [3]) >=0 and int(newip [3]) <=255:
    print ( "This is a valid ip address")


    elif int(newip [0]) == 10:
        print( "This is Class A Private IP")
        
    elif int(newip [0]) == 172 and int(newip [1]) >= 16 and int(newip [1]) <= 31:
        print ( "This is a Class B Private IP")

    elif int(newip [0]) == 192 and int(newip [1]) ==168:
        print ("This is clas C Private Ip")
    
    else:
        print("This is not a valid Private IP Address")
    
elif:    
    print ( "This is not a valid ip please enter values between 0-255")    