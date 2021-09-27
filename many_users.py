users = {'mmoalla' : {'first' : 'modar',
                     'last' : 'moalla',
                     'location' : 'kristiansand'},
         'khassaad' : {'first' : 'kheder',
                     'last' : 'assaad',
                     'location' : 'lebanon'},}
for user_name, user_info in users.items():
    print("\nUsername: " + user_name)
    fullname = user_info['first'] + " " + user_info['last']
    location = user_info['location']

    print("\tFullname: " + fullname.title())
    print("\tLocation: " + location.title())
