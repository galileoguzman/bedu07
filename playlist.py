# Importing albums from music file
from music import (
    despechados,
    para_trapear,
    the_weeknd_album,
    Chidas,
    romanticonas,
)

# For all albums imported add them to a new list
lista=[]
lista.append(despechados)
lista.append(para_trapear)
lista.append(the_weeknd_album)
lista.append(Chidas)
lista.append(romanticonas)

for album in lista:
    print("-----------------------------------------")
    for song in album.songs:
        print(song.get_title_and_singer())
