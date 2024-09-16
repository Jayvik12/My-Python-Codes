device_info1 = { "device_ip": "10.1.3.4", "model": 9800, "site" : "site-a", "rack" : "rack-1", "os-ver" : 16.6, "mgmt_ips" : ["10.3.3.1", "10.3.3.2"] }

device_info2 = { "device_ip": "10.2.3.4", "model": 9500, "site" : "site-b", "rack" : "rack-2", "os-ver" : 16.2, "mgmt_ips" : ["20.3.3.1", "10.3.3.2"] }

device_info3 = { "device_ip": "10.3.3.4", "model": 9300, "site" : "site-c", "rack" : "rack-3", "os-ver" : 16.3, "mgmt_ips" : ["30.3.3.1", "10.3.3.2"] }


device_info = [device_info1, device_info2, device_info3]

print ( device_info)