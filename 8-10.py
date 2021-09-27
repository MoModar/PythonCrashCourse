# TRY IT YOURSELF
# 8-10,Great Magicians.


def show_magicians(names):
    for name in names:
        msg = name.title()
        print(msg)


magician_names = ['abraham', 'jaga', 'solvei', 'kadabra']
show_magicians(magician_names)


def modify_magicians(n):
    for i in range(len(magician_names)):
        magician_names[i] += " The Great"


modify_magicians(magician_names)
show_magicians(magician_names)


