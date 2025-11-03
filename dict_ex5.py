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