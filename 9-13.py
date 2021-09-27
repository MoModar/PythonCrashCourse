# Try It Yourself
# 9-13. OrderedDict Rewrite:

from collections import OrderedDict

glossary = OrderedDict()

glossary['syntax'] = 'a line of code'
glossary['attribute'] = 'an instance attribute is a Python variable belonging to one, and only one, object'
glossary['variable'] = 'a Python variable is a reserved memory location to store values'

for word, value in glossary.items():
    print(word.title() + " is " + value + ".")