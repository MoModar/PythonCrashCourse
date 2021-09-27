pet1 = {'pets_name' : 'mathilda',
        'owners_name' : 'sami'}
pet2 = {'pets_name' : 'weedo',
        'owners_name' : 'alice'}
pet3 = {'pets_name' : 'boris',
        'owners_name' : 'modar'}

pets = [pet1, pet2, pet3]
for pet in pets:
    print("Pet's name is: " + pet['pets_name'].title() + ", and owner's name is: " + pet['owners_name'].title() + ".")