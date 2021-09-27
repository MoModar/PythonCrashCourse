#6-1. Storing personal info in a Dictionary:
person_0={'first_name': 'modar', 'last_name': 'moalla', 'city': 'kristiansand', 'age': 29}
print("My name is " + person_0['first_name'].title() + " " + person_0['last_name'].title() + ".")
print("I live in " + person_0['city'].title() + ", and im " + str(person_0['age']) + " years old.")
#6-2. Favorite Numbers:
favorite_numbers={'modar': 3,
                  'zein': 4,
                  'kheder': 7,
                  'alice': 10,
                  'hani': 5}
print("Modar's favorite number is " + str(favorite_numbers['modar']) + ".")
print("Alice's favorite number is " + str(favorite_numbers['alice']) + ".")
print("Kheder's favorite number is " + str(favorite_numbers['kheder']) + ".")
print("Zein's favorite number is " + str(favorite_numbers['zein']) + ".")
print("Hani's favorite number is " + str(favorite_numbers['hani']) + ".")
#6-3. Glossary:
programming_words={'list': 'menu', 'loop': 'circle', 'dictionary': 'glossary', 'indentation': 'space', 'syntax': 'code-line'}
print("The programming word 'list' means: " + programming_words['list'] + ".")
print("\nThe programming word 'loop' means: " + programming_words['loop'] + ".")
print("\nThe programming word 'indentation' means: " + programming_words['indentation'] + ".")
print("\nThe programming word 'syntax' means: " + programming_words['syntax'] + ".")
print("\nThe programming word 'dictionary' means: " + programming_words['dictionary'] + ".")
