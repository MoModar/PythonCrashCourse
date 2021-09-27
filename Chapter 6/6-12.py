# Try it your self. Extensions 6-12.

cities = {'tartous': {'country': 'syria', 'population': 1000000, 'fact': 'middle east', },
          'kristiansand': {'country': 'norway', 'population': 150000, 'fact': 'scandinavia'},
          'nants': {'country': 'france', 'population': 350000, 'fact': 'europe'},
          }


# Improving the output from exercise 6-11

for cityname, cityinfo in cities.items():
    print("\nThe city's name is: " + cityname.title() + ".\nExtra information about the city is following: ")
    location = cityinfo['country'] + " in " + cityinfo['fact']
    if location == 'syria' + " in " 'middle east':
        print("\tThe city is located in Syria in the Middle East")
    else:
        print("\tThe city is located in " + location.title())
    population = cityinfo['population']
    print("\tThe population of the country amounts " + str(population) + ".")
