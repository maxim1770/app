import json

# Data to_cyrillic be written
dictionary = {
    "id": "04",
    "name": "sunil",
    "department": "HR"
}

# Serializing json
json_object = json.dumps(dictionary, indent=4)
print(json_object)

print(type(json_object))
