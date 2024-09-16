
"""
list1 = [[70,80,60], ["15-07-24:10:30:12", "16-07-24:10:30:12", "17-07-24:10:30:12"]]

for item in list1:
    for ele in item:
        print(ele)
    
"""

"""
list1 = [[70,80,60], ["15-07-24:10:30:12", "16-07-24:10:30:12", "17-07-24:10:30:12"]]

new_device_data = list(zip(list1[0], list1[1]))    

print (new_device_data)

"""




#over the terminal
"""
>>> list1 = [[70,80,60], ["15-07-24:10:30:12", "16-07-24:10:30:12", "17-07-24:10:30:12"]]
>>>
>>> for item in list1:
...     print (item[0][0])
...
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
TypeError: 'int' object is not subscriptable
>>> for item in list1:
...     print (item[0][0])
...
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
TypeError: 'int' object is not subscriptable
>>>
>>>
>>> for item in list1:
...     print (item[0])
...
70
15-07-24:10:30:12
>>> lista = ["a", "b", "c"]
>>> listb = [1,2,3]
>>>
>>> listc= tuple(zip(lista, listb))
>>>
>>> listc
(('a', 1), ('b', 2), ('c', 3))
>>>
>>>
>>> listb= (1,2,3)
>>>
>>> listc= tuple(zip(lista, listb))
>>>
>>> listc
(('a', 1), ('b', 2), ('c', 3))
>>>
>>>
>>> listc = tuple(zip("abc","123")
...
... ^Z

  File "<stdin>", line 1
    listc = tuple(zip("abc","123")
                 ^
SyntaxError: '(' was never closed
>>> listc = tuple(zip("abc","123"))
>>>
>>> listc
(('a', '1'), ('b', '2'), ('c', '3'))

"""


device_list = [ "dev1", "dev2", "dev3"]
cpu_util = [70,80,60,10,20,90]

for ut in device_list:
    print(ut)
    for u in cpu_util:
        print("The min cpu utilization is ", min(cpu_util))
    