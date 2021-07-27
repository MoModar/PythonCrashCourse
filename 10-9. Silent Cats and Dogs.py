# TRY IT YOURSELF
# 10-9. Silent Cats and Dogs:

file_names = ['dogs.txt', 'cats.txt', 'shit.txt']

for file_name in file_names:
    try:
        with open(file_name, 'r') as file_object:
            contents = file_object.read()
    except FileNotFoundError:
        pass
    else:
        print(contents)
