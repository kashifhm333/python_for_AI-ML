dist = {
    "name": "ronaldo",
    "age": 38,
    "city": "madrid"
}


print(dist["name"]) # it will print the value of the key "name"
print(dist["age"]) # it will print the value of the key "age"


info = {
    "name": "ronaldo",
    "age": 38,
    "subjects": ["math", "science", "english"],
    "address": {
        "city": "madrid",
        "country": "spain"
    }
    
}


print(info["address"]["city"]) # it will print the value of the key "city" in the nested dictionary "address"
print(info["address"]["country"]) # it will print the value of the key "country" in the nested dictionary "address"

# for printing all the keys in the dictionary

print(info.keys()) # it will print all the keys in the dictionary

print(info.get("name")) # it will print the value of the key "name" in the dictionary


# update

update = info.update({
    "car": "Bugatti",
})


print(info.keys())
