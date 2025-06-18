class Favorite_album:
    def __init__(self):
        self.album = []
    def add_to_album(self , song):
        self.album.append(song)
    def play_next_song(self):
        if self.is_album_empty() == False:
            print("playing " , self.album[-1])
            self.album.pop()
        else:
            print("no songs to play")
    def play_album(self):
            while True:
                if self.is_album_empty() == False:
                    print("plying" , self.album[-1])
                    self.album.pop()
                else:
                    print("album is empty")
                    break
    def is_album_empty(self):
            if len(self.album) == 0:
                return True
            else:
                return False
obj = Favorite_album()
obj.add_to_album("song 1")
obj.add_to_album("song 2")
obj.add_to_album("song 3")
obj.add_to_album("song 4")
obj.add_to_album("song 5")
obj.add_to_album("song 6")
obj.play_next_song()
obj.play_album()
        
            