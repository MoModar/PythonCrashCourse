# TRY IT YOURSELF
# 8-8, User Albums

def make_album(artist_name, album_title, track_number=int()):
    album = {'Artist': artist_name.title(), 'Title': album_title.title(), 'Track': track_number}
    if track_number:
        album['Track'] = track_number
    return album


while True:
    artist_name = input("\nPlease enter artist's name: ")
    if artist_name == 'q':
        break
    album_title = input("Please enter album's title: ")
    if album_title == 'q':
        break
    track_number = input("Please type track number: ")
    if track_number == 'q':
        break
    album= make_album(artist_name,album_title)
    print(album)

    print("\nPlease type 'q' when you want to quit!")
