import json

############## Writing to Json###############
# device_info = { "vendor" : "cisco",
#                 "model" : "Catalyst9300",
#                 "intf_info" : {"intf_names": ["gig0/1", "gig0/2", "gig0/3"],
#                 "desc" : "Connected to server 1",
#                 "speed" : 1000
                
#                 }
# }  

# json_file = open("test.json", 'w')

# json_data = json.dump(device_info, json_file, indent=4)


############# Reading from Json #####################

json_file = open ("test.json", 'r')

my_data = json.load(json_file)
print(my_data)