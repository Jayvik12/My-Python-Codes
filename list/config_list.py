"""

config_list_access = ["conf t", "interface g0/1", "switchport", "switchport mode access", "switchport access vlan 10"]

config_list_trunk = ["conf t", "interface g0/1", "switchport", "switchport mode trunk", "switchport trunk allowed vlan add 10 "]
intf_list = ["g0/1", "g0/2", "g0/3", "g0/4"]



#print (config_list_access)

#for conf in config_list_access:
    print (conf)
    



config_list_access = ["switchport", "switchport mode access", "switchport access vlan 10"]

config_list_trunk = [ "switchport", "switchport mode trunk", "switchport trunk allowed vlan add 10 "]

intf_list = ["g0/1", "g0/2", "g0/3", "g0/4"] 


print ("Conf t ")
for intf in intf_list:
    print( "interface", intf)
    if intf == "g0/1" or intf =="g0/2":
    
        for conf in config_list_access:
            print ( conf)
    else:
        for conf in config_list_trunk:
            print (conf)
            
 """           


##########################################################################################

"""

device_list = ["Sw1", "Sw2", "Sw3", "Sw4"]
            
config_list_access = ["switchport", "switchport mode access", "switchport access vlan 10"]

config_list_trunk = [ "switchport", "switchport mode trunk", "switchport trunk allowed vlan add 10 "]

intf_list = ["g0/1", "g0/2", "g0/3", "g0/4"] 

device_list = ["Sw1", "Sw2", "Sw3", "Sw4"]


for dev in device_list:
    ip = input ( "Enter the device you want to configure : ") 
    print ("configuring device ",dev)
    print ("Conf t ")
    
    for intf in intf_list:
        print( "interface", intf)
        if intf == "g0/1" or intf =="g0/2":
    
            for conf in config_list_access:
                print ( conf)
        else:
            for conf in config_list_trunk:
                print (conf)

"""

config_list_access = ["switchport", "switchport mode access", "switchport access vlan 10"]

config_list_trunk = [ "switchport", "switchport mode trunk", "switchport trunk allowed vlan add 10 "]

intf_list = ["g0/1", "g0/2", "g0/3", "g0/4" , "g1/1", "g1/2", "g1/3", "g1/4"] 


ip = input ( "Enter the device you want to configure : ") 
print ("configuring device ", ip)
print ("Conf t ")
    
for intf in intf_list:
    print( "interface", intf)
    if intf == "g0/1" or intf =="g0/2":
    
        for conf in config_list_trunk:
            print ( conf)
    else:
        for conf in config_list_access:
            print (conf)
