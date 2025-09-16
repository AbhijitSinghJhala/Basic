# month_days = input("enter month:" )
# if "jan":
#     print(31) 
# elif "feb":
#     print(28)
# elif "Mar":
#     print(30)
# elif "apr":
#     print(31)
# else:
#     print(31)


####---------------------->

month = input("Enter Month ")
# Method 1
# if month=='January':
#     print(" 31 days ")
# elif month=='February':
#     print(" 28 or 29 days ")
# elif month=='March':
#     print(" 31 days ")


#Method 2

# if month =='January' or month=='March' or month=='May' or month=='July' or month=='octomber' or month=="Descember":
#     print(" 31 days ")
# elif month=="Febrayry":
#     print(" 28 or 29 days ")
# elif month=='April' or month=='June' or month=='August':
#     print(" 30 days ")
# else:
#     print("invalid month")


# Method 2

# if month in ('January','March','May','July','octomber',"Descember"):
#     print(" 31 days ")
# elif month=="Febrayry":
#     print(" 28 or 29 days ")
# elif month in ('April','June','August','September'):
#     print(" 30 days ")
# else:
#     print("invalid month")


#Method 3

match month:
    case 'January' | 'March' | 'May' | 'July' | 'octomber' | "Descember":
        print("31 days")
    case 'April' | 'June' | 'August' |'September':
        print("30 days")
    case "February":
        print("28 or 29 days")
    case _ :
        print("invalid input ")