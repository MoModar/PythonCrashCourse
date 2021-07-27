# TRY IT YOURSELF
# 10-8. Cats and Dogs:

file_names = ['dogs.txt', 'cats.txt', 'shit.txt']

for file_name in file_names:
    try:
        with open(file_name, 'r') as file_object:
            contents = file_object.read()
    except FileNotFoundError:
        print("\nOPS, the file: " + file_name + " does not exist!")
    else:
        print(contents)
