# Favorite numbers 6-10.

favorite_numbers={'modar':[ 3, 7, 13],
                  'zein': [4, 8, 29],
                  'kheder': [7, 9, 23],
                  'alice': [10, 82, 8],
                  'hani': [1, 5, 12]}

for name, numbers in favorite_numbers.items():
    print(name.title() + "'s favorite numbers are: ")
    for number in numbers:
        print("\t" + str(number))
print(".")
