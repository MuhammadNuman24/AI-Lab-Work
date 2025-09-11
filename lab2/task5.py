# Given dictionary
sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}

keys = ["name", "salary"]
#New dictionary
new_dict = {}
for k in keys:
    new_dict[k] = sample_dict[k]

# Display result
print("New dictionary:", new_dict)
