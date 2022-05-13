people = [
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Cho", "house": "Ravenclaw"},
    {"name": "Jim", "house": "Slytherin"},
]
# examples of lambda keys.
people.sort(key=lambda person: person["name"])
print(people)
