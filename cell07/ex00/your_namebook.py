def array_of_names(persons):
    namelist = []
    for first, last in persons.items():
        full_name = first.capitalize() + " " + last.capitalize()
        namelist.append(full_name)
    return namelist
persons = {
    "jean": "valjean",
    "grace": "hopper",
    "xavier": "niel",
    "fifi": "brindacier"
}
print(array_of_names(persons))