import yaml

############## Writing to yml###############
device_info = { "vendor" : "cisco",
                "model" : "Catalyst9300",
                "intf_info" : {"intf_names": ["gig0/1", "gig0/2", "gig0/3"],
                "desc" : "Connected to server 1",
                "speed" : 1000
                
                }
}  


########2 things to keep in mind while dealing with Yaml data
####### colon space : " "
######## hyphen space - " "


yaml_file = open("test.yml", 'w')

yaml_data = yaml.dump(device_info, yaml_file)


############# Reading from Json #####################

# json_file = open ("test.json", 'r')

# my_data = json.load(json_file)
# print(my_data)