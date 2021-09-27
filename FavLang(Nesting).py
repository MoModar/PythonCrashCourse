# Store the favorite languages:
favorite_languages = {'modar' : ['c++', 'python'],
                      'alice' : ['java', 'c'],
                      'zein' : ['python', 'ruby'],
                      'kheder' : ['javascript', 'sql'],
                      'sami' : ['java', 'c#']}
# make output of ppls response.

for name, languages in favorite_languages.items():
    print("\n" + name.title() + "'s favorite languages are:")
    for language in languages:
        print("\t" + language.title())