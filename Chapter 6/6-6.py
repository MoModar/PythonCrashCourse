#Try it your self, 6-6:
favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
 }
friends = {'modar', 'alice', 'jen', 'sarah'}
#Alternative 1:
#for name in friends:
#    if name in favorite_languages.keys():
#        print("Hi " + name.title() +
#              ", i see your favorite language is " +
#            favorite_languages[name].title() + "!")
#    else: print("Hi " + name.title() + ", please take the poll :)")
#solution 2:
for name in friends:
    if name not in favorite_languages.keys():
        print("Hi " + name.title() + ", please take the poll :)")
    else:
        print("Hi " + name.title() +
        ", i see your favorite language is " +
        favorite_languages[name].title() + "!")


