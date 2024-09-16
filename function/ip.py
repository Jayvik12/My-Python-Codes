"""
ip = input ("Enter the ip address x.x.x.x (0-255): ")

if ip[0:3] == "10.":
    print ("this is class A ip")
if ip[0:4] == "172.":
        print ("this is class B ip")
if ip[0:4] == "192.":
        print ("this is a Class C ip" )
else:
        print ("this is not a valid ip")
       
 """

"""
ip = input ("Enter the ip address x.x.x.x (0-255): ")

if ip[0:3] == "10.":
    print ("this is class A ip")
if ip[0:4] == "172." and float(ip[4:7])>=16 and float(ip[4:7]) <=31.:
        print ("this is class B ip")
if ip[0:4] == "192." and ip[4:8]== "168.":
        print ("this is a Class C ip" )
else:
       print ("this is not a private ip")
       
"""       
"""
ip = input ("Enter the ip address x.x.x.x (0-255): ")

if ip.startswith ("10."):
        print("this is a Class A private ip address")
        
elif ip.startswith ("172") and float(ip[4:7])>=16 and float(ip[4:7]) <=31.:
      print ("this is class B ip")
      
elif ip.startswith("192") and ip[4:8]== "168.":
     print ("this is a Class C ip" ) 
     
else:
    print ("this is not a private ip")


"""   



   
"""
ip = input ("Enter the ip address x.x.x.x (0-255): ")

if ip.startswith ("10."):
        print("this is a Class A private ip address")
        
elif ip.startswith("172") and 16 <= float(ip[4:7]) <= 31:
      print ("this is class B ip")
      
elif ip.startswith("192.168"):
     print ("this is a Class C ip" ) 
     
else:
    print ("this is not a private ip")

"""




def food_selection(food):
        if food.startswith ("biryani"):
                message ="Please pack Biryani"
                
        elif food.startswith ("chole"):
                message= "Please pack Chole bhature"

        elif food.startswith ("veg"):
                message= "Please pack Veg Biryani"      
        
        else:
                message = "pack anything which is available"
        return message


food = input ("Enter the choice of food: ")
msg = food_selection(food)
print(msg)  