import yaml

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

yaml_file = open("test1.yml", 'w')

yaml_data = yaml.dump(intf_conf_data, yaml_file)
