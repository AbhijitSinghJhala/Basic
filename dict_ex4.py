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