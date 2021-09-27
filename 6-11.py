# Try it your self: 6-11, Cities:

cities = {'tartous' : {'country' : 'syria', 'population' : 1000000, 'fact' : 'middle east',},
        'kristiansand' : {'country' : 'norway', 'population' : 150000, 'fact' : 'scandinavia'},
          'nants': {'country': 'france', 'population': 350000, 'fact': 'europe'},
          }

for cityname, cityinfo in cities.items():
    print("\nThe city's name is: " + cityname.title() + ".\nExtra information about the city is following: ")
    location = cityinfo['country'] + " in " + cityinfo['fact']
    print("\tThe city is located in " + location.title())
    population = cityinfo['population']
    print("\tthe population of the country amounts " + str(population) + ".")
