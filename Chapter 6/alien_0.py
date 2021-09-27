#Starting wi an empty dictionary:
alien_0 = {}
alien_0['weight'] = '25 kg'
alien_0['height'] = '120 cm'
alien_0['color'] = 'green'
alien_0['points'] = 5
print(alien_0)
#Modifying Values in a Dictionary:
alien_0['color'] = 'yellow'
print("The alien is " + alien_0['color'] + " now!")
#Deleting Key-Value Pairs:
print(alien_0)
del alien_0['height']
del alien_0['weight']
print(alien_0)
