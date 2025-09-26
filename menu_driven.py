# Menu driven program with functions like convert to uppercase, lowercase, find lenth, replace and exit using match case.

while True:

    print("convert into uppercase")
    print("convert into lowercase")
    print("find length of string")
    print("replace substring")
    print("exit")
    choice = int(input("Enter your choice : "))
    match choice:
        case 1:
            str = input("Enter a string: ")
            print(f"Uppercase: {str.upper()}")
        case 2:
            str = input("Enter a string: ")
            print(f"Lowercase: {str.lower()}")      
        case 3:
            str = input("Enter a string: ")     
            print(f"Length of string: {len(str)}")  
        case 4:
            str = input("Enter a string: ") 
            old = input("Enter substring to be replaced: ")     
            new = input("Enter new substring: ")
            print(f"Replaced string: {str.replace(old, new)}")
        case 5:
            print("Exiting...")
            break
        case _:
            print("Invalid choice, please try again.")