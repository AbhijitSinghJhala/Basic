car_data = {
"EV":
    {"maruti":
        {"baleno":{"price": 700000, "model":"vx"},
          "scros":{"price":799999,"model":"lx"}
        },
    "hundai":
        {"verna":{"price":1100000,"model":"t"},
        "creta":{"price":1205000,"model":"v"}}
},
"disel":
    {"maruti":
        {"baleno":{"price": 700000, "model":"vx"},
          "scros":{"price":799999,"model":"lx"}
        },
    "hundai":
        {"verna":{"price":1100000,"model":"t"},
        "creta":{"price":1205000,"model":"v"}}
},
"petrol":
    {"maruti":
        {"baleno":{"price": 700000, "model":"vx"},
          "scros":{"price":799999,"model":"lx"}
        },
    "hundai":
        {"verna":{"price":1100000,"model":"t"},
        "creta":{"price":1205000,"model":"v"}}
}}

# print(car_data["EV"])
# print(car_data.keys())

k = input("enter a car: ")
print(f"this is your {k} variant {car_data[k]}")
# ______________________

# # Get the price of EV Maruti Baleno
# price = car_data["EV"]["maruti"]["baleno"]["price"]
# print(price)  # Output: 700000

# # Get model of diesel Hyundai Creta
# model = car_data["disel"]["hundai"]["creta"]["model"]
# print(model)  # Output: "v"

# # List all fuel types
# print(car_data.keys())  # dict_keys(['EV', 'disel', 'petrol'])

# # List all brands under petrol
# print(car_data["petrol"].keys())  # dict_keys(['maruti', 'hundai'])


##__________________________________________________________________________

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

##__________________________________________________________________________
##__________________________________________________________________________

# dict1 = {1: 'apple', 2: 'banana', 3: 'cherry', 4: 'date'}
# for key in dict1:
#     print(f"Key: {key}")
#     print(f"Value: {dict1[key]}")

###______________________________________________________

# dict1 = {1: 'apple', 2: 'banana', 3: 'cherry', 4: 'date'}
# for key in dict1.keys():
#     print(f"Key: {key}")

# for value in dict1.values():
#     print(f"Value: {value}")

###______________________________________________________

# dict1 = {101 : ['apple', 'banana'], 
#          102 : ['cherry', 'date'],
#          103 : ['fig', 'grape'],
#          104 : ['kiwi', 'lemon']
#          }

# for k,v in dict1.items():
#     print(k)
#     for i in v:
#         print(f"\t{i} ")

###_______________________________________________________________

# dict1 = {101 : ['apple', 'banana', 19000], 
#          102 : ['cherry', 'date', 20000],
#          103 : ['fig', 'grape', 21000],
#          104 : ['kiwi', 'lemon', 22000]
#          }

# for k,v in dict1.items():
#     if v[2] > 20000:
#         print(k)
#         for i  in v:
#             print("\t",i)

###_______________________________________________________________

# dict1 = {101 : ['Dhruv','Parimal','DS',23000],
#          102 : ['Romil','C G Road' , 'Python' , 32000],
#          205 : ['Dhruti' , 'Bhanagar' , 'python' , 23000],
#          207 : ['Dharmishtha' , 'Parimal' , 'python-java-st' , 20000]
#          }

# for key,val in dict1.items():
    
#     if val[3]>20000:
#         print(key)
#         for i in val:        
#             print("\t",i)

###_______________________________________________________________
#find total score of no.

dict1 = {101 : ['Dhruv','Parimal',90,80,70],
         102 : ['Romil','C G Road' , 90,80,77],
         205 : ['Dhruti' , 'Bhanagar' , 90,83,71],
         207 : ['Dharmishtha' , 'Parimal' , 92,67,72]
            }
# for k,v in dict1.items():
#     marks = v[3:]
#     total = sum(marks)
#     print(f"ID: {k} Name: {v[0]} Total Marks: {total}")

result =[]
for k,v in dict1.items():
    marks = v[2:]
    total = sum(marks)
    result.append((v[0],total))
result = tuple(result)
print(result)

##__________________________________________________________________________
##__________________________________________________________________________

dict1 = {1:"Ahmedabad",2:"Baroda",3:"Surat",1:"Jamnagar",1:"Rajkot",5:"Surat","1":"Bhavnagar"}
for k,v in dict1.items():
    print(f"{k}  ---> {v}")
print(f"{dict1} - {len(dict1)}")


##__________________________________________________________________________

dict1 = {
    "1":"one",
    "2" : "Two",
    "3" : "Three"
}
# access item - key

print(dict1["2"])

# add item in dictionary 
dict1[2]="Two"
#update value
dict1["2"]="Twenty Two"

print(dict1)

del dict1["3"]
print(dict1)

# delete dictionary
# del dict1

dict2 = {101 : ['Dhruv','Parimal','DS',23000],
         102 : ['Romil','C G Road' , 'Python' , 32000],
         205 : ['Dhruti' , 'Bhanagar' , 'python' , 23000],
         207 : ['Dharmishtha' , 'Parimal' , 'python-java-st' , 20000]
         }
print(dict2[101][2])

del dict2[207][1]

print(dict2)


##__________________________________________________________________________

# fetch subjects 

dict2 = {101 : ['Dhruv','Parimal','DS',23000],
         102 : ['Romil','C G Road' , 'Python' , 32000],
         205 : ['Dhruti' , 'Bhanagar' , 'python' , 23000],
         207 : ['Dharmishtha' , 'Parimal' , 'python-java-st' , 20000]
         }
# for i in dict2.keys():
#     print(f"{dict2[i]} -{dict2[i][2]}")

for j in dict2.values():
    print(f"{j} -  {j[2]}")


##__________________________________________________________________________

city_names ={'Ahemedabad' : "" , "baroda" : "" , "surat" : ""}
for k in city_names:
    # city_names[k]=k.upper()
    city_names[k]=len(k)

print(city_names)


##__________________________________________________________________________

sales_data = [{"product": "Pen", "price": 10, "units_sold": 10},
    {"product": "Notebook", "price": 50, "units_sold": 90},
    {"product": "Pencil", "price": 5, "units_sold": 300},
    ]
# list ->dic
# dic - dic 
# len of list 3 
for i in sales_data:
    if i['units_sold']>100:
        print(i)


##____________________________________________________________________

#fetch/filter only those product whose units_sold are more then 100
sales_data = {
    "Pen":{"product_discription": "Pentonic Pen", "price": 10, "units_sold": 10},
    "Notebook" : {"product_discription": "DOMS Notebook", "price": 50, "units_sold": 90},
    "Pencil" :  {"product_discription": "DOMS Pencil", "price": 5, "units_sold": 300},
}


##____________________________________________________________________

# dict1 = {1:0,2:0,3:0,4:0}
# #for k,v in dict1.items():
# #    dict1[k]=k**2

# dict1 = {k:k**2 for k in dict1}
# print(dict1)

#_________________________

state_capital = {'Gujarat':'Gandhinagar','Maharashtra':'Mumbai','Rajasthan':'Jaipur'}
state_capital_length = {k:len(k) for k,v in state_capital.items()}
print(state_capital_length)


##____________________________________________________________________

# state_capital= {'Gujarat':'Gandhinagar','Maharashtra':'Mumbai','Rajasthan':'Jaipur'}
# state_capital_1= {k:v.upper() for k,v in state_capital.items() if len(k)>7}
# print(state_capital_1)

#_______________________________

#convert capital into upper if capital is greater than 5
#else convert capital into lower
state_capital= {'Gujarat':'Gandhinagar','Maharashtra':'Mumbai','Rajasthan':'Jaipur'}
state_capital_1={k:v.upper() if len(v)>7 else v.lower() for k,v in state_capital.items()}
print(state_capital_1)


##____________________________________________________________________

