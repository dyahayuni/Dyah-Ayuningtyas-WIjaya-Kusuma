def make_album(artist, title, songs=None):
    album = {'artist': artist, 'title': title}
    if songs:
        album['songs'] = songs
    return album


print(make_album('Tulus', 'Monokrom'))
print(make_album('Treasure', 'Now Forever'))
print(make_album('Sheila on 7', 'Kisah Klasik'))

print(make_album('Dewa 19', 'Pandawa Lima', songs=10))