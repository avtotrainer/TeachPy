# JSON – მონაცემების შენახვა და წაკითხვა

import json

data = {"name": "John Doe", "age": 30, "city": "New York"}

json_data = json.dumps(data, indent=4)

print(json_data)

with open("data.json", "w") as f:
    json.dump(data, f, indent=4)

with open("data.json", "r") as f:
    data = json.load(f)

print(data)
