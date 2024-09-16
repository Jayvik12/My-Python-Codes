
# site_list = ["site-A", "site-B", "site-C", "site-D"]

# device_list = ['sw1', 'sw2', 'sw3', 'sw4']

# intf_conf_data = [{
#     "intf_name" : "gig0/1",
#     "desc" : "Connected to Server 1",
#     "speed" : 1000,
#     "duplex" : "full"
# },
# {
#     "intf_name" : "gig0/2",
#     "desc" : "Connected to Server 2",
#     "speed" : 1000,
#     "duplex" : "full"
# },
# {

#     "intf_name" : "gig0/3",
#     "desc" : "Connected to Server 3",
#     "speed" : 1000,
#     "duplex" : "full"
# },
# {

#     "intf_name" : "gig0/4",
#     "desc" : "Connected to Server 4",
#     "speed" : 1000,
#     "duplex" : "full"
# }
# ]    


# intf_syntax = {
#         "intf_name" :"interface {}",
#         "desc" : "description {}",
#         "speed" : "speed {}",
#         "duplex" : "duplex {}"
# }



# for s in site_list:
#     print ( "Configuring the Site " , s, "\n")

#     for d in device_list:
#         print( "Connecting to", d , "\n")

#         for i in intf_conf_data:
#             print(intf_syntax["intf_name"].format(i["intf_name"]))
#             print(intf_syntax["desc"].format(i["desc"]))
#             print(intf_syntax["speed"].format(i["speed"]))
#             print(intf_syntax["duplex"].format(i["duplex"]))
#             print(" \n")



def configure_sites(site_list, device_list, intf_conf_data, intf_syntax):
    for site in site_list:
        print("Configuring the Site", site, "\n")

        for device in device_list:
            print("Connecting to", device, "\n")

            for intf in intf_conf_data:
                print(intf_syntax["intf_name"].format(intf["intf_name"]))
                print(intf_syntax["desc"].format(intf["desc"]))
                print(intf_syntax["speed"].format(intf["speed"]))
                print(intf_syntax["duplex"].format(intf["duplex"]))
                print("\n")


site_list = ["Site-A", "Site-B", "Site-C", "Site-D"]
device_list = ['sw1', 'sw2', 'sw3', 'sw4']
intf_conf_data = [
    {"intf_name": "gig0/1", "desc": "Connected to Server 1", "speed": 1000, "duplex": "full"},
    {"intf_name": "gig0/2", "desc": "Connected to Server 2", "speed": 1000, "duplex": "full"},
    {"intf_name": "gig0/3", "desc": "Connected to Server 3", "speed": 1000, "duplex": "full"},
    {"intf_name": "gig0/4", "desc": "Connected to Server 4", "speed": 1000, "duplex": "full"}
]
intf_syntax = {
    "intf_name": "interface {}",
    "desc": "description {}",
    "speed": "speed {}",
    "duplex": "duplex {}"
}

configure_sites(site_list, device_list, intf_conf_data, intf_syntax)