from album import Album
from song import Song

song_1 =Song('Mujeres divinas','Despechados','Vicente Fernández')
song_2 =Song('Mátalas','Despechados','Alejandro Fernández')
song_3 =Song('Belleza de cantina','Despechados','Los Huracanes')

despechados=Album()
despechados.songs.append(song_1)
despechados.songs.append(song_2)
despechados.songs.append(song_3)

song_4=Song('Gasolina','para_trapear','dady yanky')
song_5=Song('Rompe','para_trapear','dady yanky')
song_6=Song('La planta','para_trapear','Caos')

para_trapear=Album()
para_trapear.songs.append(song_4)
para_trapear.songs.append(song_5)
para_trapear.songs.append(song_6)

song_7=Song('Heartless','After Hours','The Weeknd')
song_8=Song('Tears in the rain','Kiss Land','The Weeknd')
song_9=Song('In your eyes','After Hourse','The Weeknd')

the_weeknd_album=Album()
the_weeknd_album.songs.append(song_7)
the_weeknd_album.songs.append(song_8)
the_weeknd_album.songs.append(song_9)

song_10=Song('The Stronger','The Score','The Score')
song_11=Song('Dance Monkey','Tones And I','The Kids are coming')
song_12=Song('Pompeii','Bastille','Bad Blood')

Chidas=Album()
Chidas.songs.append(song_10)
Chidas.songs.append(song_11)
Chidas.songs.append(song_12)

song_13=Song('in your eyes','INNA','INNA')
song_14=Song('Antologia','Fijacion oral','Shakira')
song_15=Song('soñe','Soñe','Zoe')

romanticonas=Album()
romanticonas.songs.append(song_13)
romanticonas.songs.append(song_14)
romanticonas.songs.append(song_15)
