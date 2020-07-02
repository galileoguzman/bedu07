class Song():
    '''
    THis class will save information about a song.
    '''
    def __init__(self, title, album, singer):
        self.title = title
        self.album = album
        self.singer = singer

    def get_title_and_singer(self):
        return f'{self.title} - {self.singer}'


cancion = Song('Alexander Hamilton', 'Hamilton', 'Lin Manuel Miranda')
print(cancion.get_title_and_singer())
