# state_capital= {'Gujarat':'Gandhinagar','Maharashtra':'Mumbai','Rajasthan':'Jaipur'}
# state_capital_1= {k:v.upper() for k,v in state_capital.items() if len(k)>7}
# print(state_capital_1)

#_____________________________________

#convert capital into upper if capital is greater than 5
#else convert capital into lower
state_capital= {'Gujarat':'Gandhinagar','Maharashtra':'Mumbai','Rajasthan':'Jaipur'}
state_capital_1={k:v.upper() if len(v)>7 else v.lower() for k,v in state_capital.items()}
print(state_capital_1)