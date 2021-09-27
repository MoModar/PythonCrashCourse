favorite_places = { 'modar': ['neapoli', 'melbourne', 'tartous'],
                    'zein' : ['nants', 'kristiansand','paris'],
                    'alice' : ['japan', 'south korea', 'albania'],}

for name, places in favorite_places.items():
    print("\n" + name.title() + "'s favorite places are: " )
    for place in places:
        print("\t" + place.title() + ", ")
print(".")
