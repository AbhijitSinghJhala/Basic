car_data = {
"EV":
    {"maruti":
        {"baleno":{"price": 700000, "model":"vx"},
          "scros":{"price":799999,"model":"lx"}
        },
    "hundai":
        {"verna":{"price":1100000,"model":"t"},
        "creta":{"price":1205000,"model":"v"}}
},
"disel":
    {"maruti":
        {"baleno":{"price": 700000, "model":"vx"},
          "scros":{"price":799999,"model":"lx"}
        },
    "hundai":
        {"verna":{"price":1100000,"model":"t"},
        "creta":{"price":1205000,"model":"v"}}
},
"petrol":
    {"maruti":
        {"baleno":{"price": 700000, "model":"vx"},
          "scros":{"price":799999,"model":"lx"}
        },
    "hundai":
        {"verna":{"price":1100000,"model":"t"},
        "creta":{"price":1205000,"model":"v"}}
}}

# print(car_data["EV"])
# print(car_data.keys())

k = input("enter a car: ")
print(f"this is your {k} variant {car_data[k]}")
# ______________________

# # Get the price of EV Maruti Baleno
# price = car_data["EV"]["maruti"]["baleno"]["price"]
# print(price)  # Output: 700000

# # Get model of diesel Hyundai Creta
# model = car_data["disel"]["hundai"]["creta"]["model"]
# print(model)  # Output: "v"

# # List all fuel types
# print(car_data.keys())  # dict_keys(['EV', 'disel', 'petrol'])

# # List all brands under petrol
# print(car_data["petrol"].keys())  # dict_keys(['maruti', 'hundai'])
