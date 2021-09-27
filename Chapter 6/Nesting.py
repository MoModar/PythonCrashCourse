#Making an empty list for storing aliens
aliens = []

#Making 30 green aliens.
for alien_number in range(30):
    new_alien = {'color' : 'green', 'points' : 5, 'speed' : 'slow'}
    aliens.append(new_alien)

#Show the first five aliens:
for alien in aliens[:5]:
    print(alien)
print("...")

#Show how many aliens have been created:
print("The total number of aliens: " + str(len(aliens)))

#Changing the first 3 alien's values usinga loop with if statment:
for alien in aliens[:4]:
    if alien['color'] == 'green':
        alien['color'] = 'yello'
        alien['speed'] = 'medium'
        alien['points'] = 10

#Showing first 5 aliens:
for alien in aliens[:5]:
    print(alien)
print("...")



