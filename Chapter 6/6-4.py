#Try it your self 6-3/6-4. Glossary-2:
#glossary = {
#    'function' : 'block of code that performs a particular task',
#    'dictionary' : 'data container',
#    'method' : 'similar to function can be used in the class',
#    'loop' : 'helps you to execute a block of code repeatedly',
#    'word5' : '5dose not matter',
#    'word6' : '6dose not matter',
#    'word7' : '7dose not matter'
#}

#for word, meaning in glossary.items():
 #   print(word + "\n" + meaning )

#Try it your self. 6-5:
rivers = {'nile' : 'egypt', 'amazon' : 'brazil', 'al-fourat' : 'syria'}
for river, country in rivers.items():
    print("The " + str(river.title()) + " runs through " + str(country.title()) + ".")

#Creating loop for river's name output:
for river in sorted(rivers):
    print(river)
#Creating loop for country's name output:
for country in rivers.values():
    print(country)
