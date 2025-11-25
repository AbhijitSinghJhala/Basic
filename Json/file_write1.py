with open("textFile.txt","w")  as file:
# file.write("HThis is New File and we have to write some content \n")
# file.write("Today is Saturday")
# file.write("dfgdfgdfg")

    data=input("Enter string to write into file ")
    file.write(data)
    print("Data written successfully ")