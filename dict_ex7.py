sales_data = [{"product": "Pen", "price": 10, "units_sold": 10},
    {"product": "Notebook", "price": 50, "units_sold": 90},
    {"product": "Pencil", "price": 5, "units_sold": 300},
    ]
# list ->dic
# dic - dic 
# len of list 3 
for i in sales_data:
    if i['units_sold']>100:
        print(i)