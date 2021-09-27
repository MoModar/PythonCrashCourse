#Dictionaries-introduction:
alien_0={'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])
#output a key from a ditionary:
new_points=alien_0['points']
print("You just earned " + str(new_points) + " points!")
#Addin new keys to a dictionary:
alien_0['x_position']=0
alien_0['y_position']=25
print(alien_0)