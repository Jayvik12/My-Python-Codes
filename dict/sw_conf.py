
site_list = ["site-A", "site-B", "site-C", "site-D"]

device_list = ['sw1', 'sw2', 'sw3', 'sw4']

intf_conf_data = [{
    "intf_name" : "gig0/1",
    "desc" : "Connected to Server 1",
    "speed" : 1000,
    "duplex" : "full"
},
{
    "intf_name" : "gig0/2",
    "desc" : "Connected to Server 2",
    "speed" : 1000,
    "duplex" : "full"
},
{

    "intf_name" : "gig0/3",
    "desc" : "Connected to Server 3",
    "speed" : 1000,
    "duplex" : "full"
},
{

    "intf_name" : "gig0/4",
    "desc" : "Connected to Server 4",
    "speed" : 1000,
    "duplex" : "full"
}
]    


intf_syntax = {
        "intf_name" :"interface {}",
        "desc" : "description {}",
        "speed" : "speed {}",
        "duplex" : "duplex {}"
}


#print(intf_syntax["intf_name"])
#print (intf_conf_data["intf_name"])
#print(intf_syntax["intf_name"].format("gig0/1")) //hard coded

#print(intf_syntax["intf_name"].format(intf_conf_data["intf_name"]))
#print(intf_syntax["desc"].format(intf_conf_data["desc"]))
#print(intf_syntax["speed"].format(intf_conf_data["speed"]))
#print(intf_syntax["duplex"].format(intf_conf_data["duplex"]))



# for i in intf_conf_data:
#     print(intf_syntax["intf_name"].format(i["intf_name"]))
#     print(intf_syntax["desc"].format(i["desc"]))
#     print(intf_syntax["speed"].format(i["speed"]))
#     print(intf_syntax["duplex"].format(i["duplex"]))





# for d in device_list:
#     print( "Connecting to", d , "\n")

#     for i in intf_conf_data:
#         print(intf_syntax["intf_name"].format(i["intf_name"]))
#         print(intf_syntax["desc"].format(i["desc"]))
#         print(intf_syntax["speed"].format(i["speed"]))
#         print(intf_syntax["duplex"].format(i["duplex"]))



for s in site_list:
    print ( "Configuring the Site " , s, "\n")

    for d in device_list:
        print( "Connecting to", d , "\n")

        for i in intf_conf_data:
            print(intf_syntax["intf_name"].format(i["intf_name"]))
            print(intf_syntax["desc"].format(i["desc"]))
            print(intf_syntax["speed"].format(i["speed"]))
            print(intf_syntax["duplex"].format(i["duplex"]))
            print(" \n")