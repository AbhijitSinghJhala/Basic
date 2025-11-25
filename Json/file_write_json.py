import json
data={"age":30,"city":"New York","name":"John"}
with open("file.json", "w") as file:
    json.dump(data, file)
    print("data written to successfully")