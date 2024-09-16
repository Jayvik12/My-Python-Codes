'''
str1 = "I&8n5^d(12i><a"

# ways to clean the string

## for char in "I&8n5^d(12i><a":
formatted_str = ""
for char in str1:
    if char.isalpha():
        formatted_str=formatted_str + char
        
#       print (formatted_str)
       
print (formatted_str)

'''

'''
data = "I&8n5^d(12i><a"

## for char in "I&8n5^d(12i><a":
formatted_str = ""
for char in data:
    if char.isalpha():
        formatted_str += char
        
#       print (formatted_str)
       
print (formatted_str)
'''
'''
data = input("Please enter the alphanumeric data:")
out = ""
for data in data:
    if data.isalpha():
        out = out + data
    
print(out)    
 '''  
'''
data = "T6h32i%&s&8i^s9(I534n250d$i65a"

output = ""
for char in data:
        if char.isalpha():
            output += char

#print(output)   
print(output.replace ("s", "s "))        
   
'''
'''
output ="IndiaisGreat"
output.replace('a', 'a ')
output.replace('a', 'a ', 1)
output.replace('a', 'a ', 1).replace('s', 's ')   
'''


ip = "10.2.3.4"
newip = ip.split('.')
print(newip)
finalip = ".".join(newip)
print(finalip)
'''
for i in finalip:
    if i>=0 and i[0]<=255:
print(ip is valid)
'''