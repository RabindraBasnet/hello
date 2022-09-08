people = [
    { "name": "Harry", "house":"Gryfffindor"},
    { "name": "Cho", "house":"Ravenclaw" }, 
    { "name": "Draco", "house":"slytherin"}    
]

people.sort(key = lambda person: person["name"])

print(people)