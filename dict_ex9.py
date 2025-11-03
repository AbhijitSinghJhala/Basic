# dict1 = {1:0,2:0,3:0,4:0}
# #for k,v in dict1.items():
# #    dict1[k]=k**2

# dict1 = {k:k**2 for k in dict1}
# print(dict1)

#_________________________________________

state_capital = {'Gujarat':'Gandhinagar','Maharashtra':'Mumbai','Rajasthan':'Jaipur'}
state_capital_length = {k:len(k) for k,v in state_capital.items()}
print(state_capital_length)