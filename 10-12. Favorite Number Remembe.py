# TRY IT YOURSELF
# 10-12. Favorite Number Remembered:
import json

file_name = 'favorite_numbers'
try:
    with open(file_name) as f_obj:
        fav_num = json.load(f_obj)
except FileNotFoundError:
    fav_num = input("Please, enter your favorite number, and i will remember it: ")
    with open(file_name, 'w') as f_obj:
        json.dump(fav_num, f_obj)
else:
    print("I know your favorite number is: " + fav_num)
