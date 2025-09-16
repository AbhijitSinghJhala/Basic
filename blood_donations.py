age = int(input("Enter age "))
weight =int(input("Enter weight "))
if age>18:
    if weight>55:
        print("Eligible to donate blood")
    else:
        print("not eligible to donate blood due to underweight ")
else: 
    print("not eligible to donate blood due to age")

# if age>18 and weight>55:
#     print("eligible to donate blood")
#else:
#   print("not eligible to donate blood")