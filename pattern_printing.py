# ### p1
# '''
# *
# *  *
# *  *  *
# *  *  *  *
# '''
# num = int(input("Enter number "))
# for i in range(num):        
#     for j in range(i):
#         print("*",end=" ")
#     print()


#---------------------------
# ### p2


# '''
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
# '''
# num = int(input("Enter number "))
# for i in range(1,num+1):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()


#---------------------------------------
######
#Reverse printing----

# num = int(input("Enter number: "))
# for i in range(num):
#     for j in range(i,num):
#         print("*",end=" ")
#     print( )


###___________________________>

# num = int(input("Enter number: "))
# for i in range(num):
#     for j in range(i,num):
#         print("*",end=" ")
#     print( )
# for i in range(num):        
#     for j in range(i):
#         print("*",end=" ")
#     print()



####----------------------------------->



# num = int(input("Enter number: "))
# for i in range(num):        
#     for j in range(i):
#         print("*",end=" ")
#     print()
# for i in range(num):
#     for j in range(i,num):
#         print("*",end=" ")
#     print()

##__________________________________________

# num = int(input("Enter number "))
# for i in range(1,num+1,2):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()

###__________________________________________

# num = int(input("Enter number "))
# odd=0
# even=0
# for i in range(1,num+1):
#     for j in range(1,i+1):
#         if i%2==0:
#         even+=1
#     else:
#         odd+=1
#         print(j,end=" ")
#     print()

#_________________________________________________________

# num = int(input("Enter number "))
# count=1
# for i in range (1,num+1):
#     for j  in range (1,i+1):
#             print(count,end=" ")
#     print()
#     count+=2 

#_________________________________________________________

# num = int(input("Enter number "))
# cnt=1                                                                 
# for i in range (1,num+1):
#     for j  in range (1,i+1):
#             print(cnt,end=" ")
#             cnt+=2               #cmt = cmt + 2 
#     print()

#_________________________________________________________

rows = int(input("Enter number :"))

# rows =5
for i in range(1,rows+1):
    num = 2*i -1   #odd number
    for j in range(i):  #print i times
        print(num,end=" ")
    print()

  '''
  how to work program
  
  num= 2 * i - 1
  1 = 2 * 1 - 1 => 1
  3 = 2 * 2 - 1 => 3 3
  5 = 2 * 3 - 1 => 5 5 5
  7 = 2 * 4 - 1 => 7 7 7 7
  9 = 2 * 5 - 1 => 9 9 9 9 9
  '''
