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