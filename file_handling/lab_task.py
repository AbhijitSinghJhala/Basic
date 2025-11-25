# Menu Driven Program ,with function 
# 1. read
# 2. write
# 3. copyFile
# 4. append
# 5. Exit

while True:
    print("read")
    print("write")
    print("copyFile")
    print("append")
    print("exit")
    choice = int(input("Enter your choice (1-5) : "))
    match choice:
        case 1:
            # file = open("C:\\Python\\Basic\\Reduce\\reduce_ex1.py","r")
            file = open("C:\\Python\\Basic\\calling_fun.py","r")
            data=file.read()
            print(data)

        case 2:
            with open("car_data.txt","w")  as file:
                data=input("Enter string to write into file ")
                file.write(data)
                print("Data written successfully ")
               
        case 3:
            import shutil
            shutil.copyfile("car_data.txt","car_data_copy.txt")

        case 4:
            with open('car_data.txt','a') as file:
                lst=['data\n','data1\n','tttt\n','234556']
                file.writelines(lst)
                print("Data written Successfully")

        case 5:
            print("Exiting...")       
            break
        case _:
            print("Invalid choice, please try again.")