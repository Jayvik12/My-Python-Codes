
    # device_info = { "vendor" : "cisco",
    #                 "model" : "Catalyst9300",
    #                 "intf_info" : {"intf_names": ["gig0/1", "gig0/2", "gig0/3"], "desc": "connected to server1", "speed": 1000}
    #                 }
                    
    # print ( device_info["intf_info"]["desc"])     

    # print ( device_info ["intf_info"]["intf_names"][1])






def device(device_info):
    return device_info



device_info = { "vendor" : "cisco",
                "model" : "Catalyst9300",
                "intf_info" : {"intf_names": ["gig0/1", "gig0/2", "gig0/3"], "desc": "connected to server1", "speed": 1000}
                }
                
temp = device(device_info)
print(temp)

