"""

ip = input ("Enter the ip (0-255) x.x.x.x ")
ip = ip.split(".")

if (int(ip[0]) >=0 and int(ip[0])<=255) and (int(ip[1]) >=0 and int(ip[1])<=255) and (int(ip[2]) >=0 and int(ip[2])<=255) and (int(ip[3]) >=0 and int(ip[3])<=255):
    print ("This is a valid ip wrt octects")
else:
        print("Given ip is not a valid ip please enter valid ip")
        
"""



"""

    
ip = input ("Enter the ip (0-255) x.x.x.x ")

for char in ip:
    if char.isalpha() or char in "!@#$%^&*()_+?><:{}|,":
        print ("Given Ip is not valid ip, Please enter IP in between 0-255 ")
        flag = True
        break
    else:
        flag = False
 

#if flag == True:
if flag == False:
    ip = ip.split(".")

    if (int(ip[0]) >=0 and int(ip[0])<=255) and (int(ip[1]) >=0 and int(ip[1])<=255) and (int(ip[2]) >=0 and int(ip[2])<=255) and (int(ip[3]) >=0 and int(ip[3])<=255):
        print ("This is a valid ip wrt octects")
    else:
    
        print("Given ip is not a valid ip, please enter valid ip")        
        
        
"""




"""

 
ip = input ("Enter the ip (0-255) x.x.x.x ")

flag = True
for char in ip:
    if char.isalpha() or char in "!@#$%^&*()_+?><:{}|,":
        print ("Given Ip is not valid ip, Please enter IP in between 0-255 ")
        flag = False
        break

 
if flag:
    ip = ip.split(".")

    if (int(ip[0]) >=0 and int(ip[0])<=255) and (int(ip[1]) >=0 and int(ip[1])<=255) and (int(ip[2]) >=0 and int(ip[2])<=255) and (int(ip[3]) >=0 and int(ip[3])<=255):
        print ("This is a valid ip wrt octects")
    else:
    
        print("Given ip is not a valid ip, please enter valid ip")  
        
"""



def ip_octet_validation(ip):
    flag = True
    for char in ip:
        
        if char.isdecimal() != True and char != ".":
            message="Given ip is not valid ip, Please enter IP in between 0-255 for each octects"
        # flag = False
            exit()

    
    if flag == True:
        ip = ip.split(".")

        if (int(ip[0]) >=0 and int(ip[0])<=255) and (int(ip[1]) >=0 and int(ip[1])<=255) and (int(ip[2]) >=0 and int(ip[2])<=255) and (int(ip[3]) >=0 and int(ip[3])<=255):
            message= "This is a valid ip wrt octects"
        else:
        
            message = "Given ip is not a valid ip, please enter valid ip"        
    return message


while True:
    ip = input ("Enter the ip (0-255) x.x.x.x ")
    msg = ip_octet_validation(ip)
    print (msg)

    choice = input ("Do you want to continue ? (y/n)" )
    if choice == "n":
        break
    elif choice =="y":
        continue    