#Creating a Dicitonary:

alien_1={'x_position': 20, 'y_position': 30, 'speed': 'medium', 'color': 'green'}
print("Orginal x_position: " + str(alien_1['x_position']))

#Move the alien.
#Determine how far to move the alien based on its current speed.

if alien_1['speed'] == 'slow':
    x_increment = 1
elif alien_1['speed'] == 'medium':
    x_increment = 2
else:
#This must be a fast alien.
    x_increment = 3

#The new position is the old position plus the increment.
alien_1['x_position'] = alien_1['x_position'] + x_increment
print("New x_position: " + str(alien_1['x_position']))

#Removing Key-value pairs:
print("Alien1 before removing: " + str(alien_1))
del alien_1['color']
print("Alien1 after removing: " + str(alien_1))
