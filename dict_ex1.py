# dict1 = {1:"Ahmedabad",2:"Baroda",3:"Surat"}
# print(dict1)
dict1 = {1:"Ahmedabad",2:"Baroda",3:"Surat",1:"Jamnagar",1:"Rajkot",5:"Surat","1":"Bhavnagar"}
print(f"{dict1} - {len(dict1)}")
key1= dict1.keys()
print(f"{key1} - {type(key1)}")
value1=dict1.values()
print(f"{value1} - {type(value1)}")
print(f"{dict1.items()}")

print(f"{dict1.keys()} - {type(dict1.keys())}")
print(dict1.values())