# TRY IT YOURSELF
# 10-10. Common Words:

filename = 'Bruin Adams.txt'
"""Text from (http://gutenberg.org/ )"""

with open(filename, encoding='utf8') as file_object:
    contents = file_object.read()
    print(contents.lower().count('the'))
