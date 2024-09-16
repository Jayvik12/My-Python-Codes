import yaml
from jinja2 import Environment, FileSystemLoader


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

with open("conf-data.yaml", 'r') as yaml_file:
    intf_conf_data = yaml.load(yaml_file)

env = Environment(loader=FileSystemLoader('.'))
template = env.get_template('intf-syntax.j2')

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