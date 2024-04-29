thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

travel_log = { "Countries visited":{
    "France" : ["Paris","Lyon"],
    "Germany": ["Berlin","Hamburg"]
}}
# for i in thisdict:
#     print(i)

order = {
    "starter": {1: "Salad", 2: "Soup"},
    "main": {1: ["Burger", "Fries"], 2: ["Steak"]},
    "dessert": {1: ["Ice Cream"], 2: []},
}

print(travel_log["Countries visited"].keys())

print(order[2])