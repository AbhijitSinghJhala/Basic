import json
with open('file23.json', 'r') as file:
    data = json.load(file)
    print("data:", data)