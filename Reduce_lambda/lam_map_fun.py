lst_numbers=[2,3,4,5]
ans=list(map(lambda num:num*num,lst_numbers))
print(ans)

def convertFar(celcius):
    fan=(celcius*9/5)+32
    return fan
lst_cel = [22,12,2,9]
ans=list(map(lambda celcius:(celcius*9/5)+32,lst_cel))
print(ans)