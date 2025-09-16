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

num = int(input("Enter number "))
cnt=1
for i in range (1,num+1):
    for j  in range (1,i+1):
            print(cnt,end=" ")
    print()
    cnt+=2