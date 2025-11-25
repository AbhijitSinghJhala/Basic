# file = open("C:\\Python\\Basic\\Reduce\\reduce_ex1.py","r")
# # data=file.read()
# data=file.read(10)
# print(data)

#_____________________________________

file = open("C:\\Python\\Basic\\Reduce\\reduce_ex1.py","r")
while True:
    line=file.readline()
    if not line :
        break
    print(line)
# -1 EOF
file.close()

#_____________________________________

#file = open("C:\\Users\\Admin\\Downloads\\SQL_Query.txt","r")
file = open("NewFile.txt.txt","r")
print(f"Before reading {file.tell()}")
#data=file.readlines()
data=file.readline()
print(data)
print(f"After reading {file.tell()}")
data=file.readline()
print(f"After reading {file.tell()}")
file.close()    

##_______________________________________

#file = open("C:\\Users\\Admin\\Downloads\\SQL_Query.txt","r")
file = open("NewFile.txt.txt","r")
file.seek(15)
#data=file.readlines()
data=file.readline()
print(data)
print(f"After reading {file.tell()}")
data=file.readline()
print(f"After reading {file.tell()}")

##_______________________________________

file=open("example_reduce.py","r")
data=file.readlines()
for i in data:
    print(i)