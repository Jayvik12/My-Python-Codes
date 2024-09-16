
'''
listoflists =[[1,2,3],[4,5,6],[7,8,9]]

listoflists[0]

>>> listoflists[0]
[1, 2, 3]
>>>
>>> listoflists[1]
[4, 5, 6]
>>>
>>>
>>> listoflists[3]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list index out of range
>>>
>>>
>>> listoflists[2]
[7, 8, 9]
>>>
>>>
>>>
>>> listoflists[0][1]   #list of list concept
2
>>> templist = ["router", 16.6]
>>>
>>> templist[0][2]
'u'
>>>
>>> ip_list = ["10.1.1.0", "172.16.1.1", "192.168.1.1"]
>>>
>>>
>>> for item in ip_list:
...     print("configuring", item)
...
configuring 10.1.1.0
configuring 172.16.1.1
configuring 192.168.1.1
>>>


>>> config_set = ["conf t", "interface g0/0", "switchport mode access", "switchport access vlan 10"]
>>>
>>> for item in config_set:
...     print(item)
...
conf t
interface g0/0
switchport mode access
switchport access vlan 10
>>>




'''





listoflistoflist = [[[1,2,3],[4,5,6],[7,8,9] ] , [[10,20,30], [40,50,60], [100,200,300] ] ]

for item in listoflistoflist:
 #   print (item)
    for ele in item:
  #      print(ele)
        for i in ele:
            print (i)