favorite_languages = {
    'modar': 'c++',
    'zein': 'python',
    'alice': 'java',
    'mohannad': 'java'
}
print("Modar's favorite programming language is: "+str(favorite_languages['modar'].title()) + ".")

#Looping through the ditionary's Keys , using the for statment and sorted() function:

for name in sorted(favorite_languages):
    print(name.title() + ", thank you for taking the vote")

#Looping through all dictionary's values, using the values() method:

print("\nThe following languages have been mentioned: ")
for language in favorite_languages.values():
    print(language.title())

#Looping through all dictionary's values, using  values() method and set() function to avoid repetitions :


print("The following languages have been mentioned: ")

for language in set(favorite_languages.values()):
    print(language.title())
