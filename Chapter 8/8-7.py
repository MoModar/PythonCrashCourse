# TRY IT YOURSELF
# 8-7, Album.

def make_album(artist_name, album_title, tracks_number= ''):
    album = {'Artist': artist_name.title(), 'Title': album_title.title(), 'Track': tracks_number}
    return album


wael_kfuri = make_album(artist_name='wael kfuri', album_title='seher al-gharam', tracks_number='12')
print(wael_kfuri)

pink_floyd = make_album(artist_name='pink floyd', album_title='the wall', tracks_number='6')
print(pink_floyd)

eminem = make_album(artist_name='eminem', album_title='lost your self')
print(eminem)
