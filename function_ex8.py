def addition(*args):
    sum=0
    for i in args:
        if type(i)==int:
            sum+=i
    return sum
ans=addition(12,23)
print(ans)
print(addition(23,657,5656))
print(addition(23,345,567567,13123,34.5656))
print(addition(23,345,"anshu",567567,13123))

#_________________________________


# # def addition(*args):
# #     return sum(args)

def addition(*args):
    sum=0 
    for i in args:
        if type(i)== int:
            sum+=i
        print(sum)
        

print(addition(12,23))
print(addition(23,657,5656))
print(addition(23,345,5656,6789,"oooo"))