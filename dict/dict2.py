sw1 = { "device_ip": "10.1.3.4", "model": 9800, "site" : "site-a", "rack" : "rack-1", "os-ver" : 16.6, "mgmt_ips" : ["10.3.3.1", "10.3.3.2"] }

# print (sw1.items())

for k, v in sw1.items():
        print (k,v)