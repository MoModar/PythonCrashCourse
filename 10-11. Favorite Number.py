# TRY IT YOURSELF
# 10-11. Favorite Number:
import json

file_name = 'favorite_numbers'
fav_numb = input("Please, enter your favorite number: ")
with open(file_name, 'w') as f_obj:
    json.dump(fav_numb, f_obj)

with open(file_name) as f_obj:
    json.load(f_obj)
    print("I know your favorite number is: " + fav_numb)
