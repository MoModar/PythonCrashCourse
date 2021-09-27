#Looping through a dikctionary:

favorite_languages={'modar': 'python',
                    'alice': 'java',
                    'kheder': 'javascript',
                    'zein': 'sql'}

#for name, language in favorite_languages.items():
 #   print(name.title() + "'s favorite language is: "
  #        + language.title() + ".")
#Making a new list comparing with the old one with if statment:

friends=['kheder' , 'zein']
for name in favorite_languages:
    print(name.title())
    if name in friends:
        print("Hei " + name + ", I see your favorite language is: "
              + favorite_languages[name].title() + ".")
