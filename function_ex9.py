def personDetails(**kwargs):
    #print(kwargs)
    if kwargs['age']>=30:
        # print(kwargs['name'])
        print(kwargs)
def details():
    return 1,"Dharmishtha",30,"Python"
personDetails(name="Dharmishtha",age=30)
personDetails(city="Ahedmbad",name="Dhruv",age=20)
personDetails(name="Abhijit",age=22)
personDetails(name="etets",age=30)
print(details())

# #________________________________
# def persondetails(**kwargs):
#     if kwargs['age']>=55:
#         print(kwargs)
# persondetails(name="mahendra",age=60)
# persondetails(name="Abhijit",age=45)
# persondetails(name="piyush",city="neemuch",age=70)
# persondetails(name="anshu",age=30)
