class MusicPlayer:
    def __init__(self):
        self.playlist = []

    def add_song(self, song):
        self.playlist.append(song)
        print(f"Added song: {song}")

    def play_song(self):
        if not self.is_empty():
            song = self.playlist.pop()
            print(f"Now playing: {song}")
        else:
            print("No songs to play!")

    def current_song(self):
        if not self.is_empty():
            print(f"Current song: {self.playlist[-1]}")
        else:
            print("No song is currently playing")

    def is_empty(self):
        return len(self.playlist) == 0

player = MusicPlayer()

player.add_song("Song 1")
player.add_song("Song 2")
player.add_song("Song 3")
player.add_song("Song 4")
player.add_song("Song 5")
player.play_song()     
player.play_song()      
player.current_song()   
player.play_song()     
player.play_song()      
player.play_song()      
player.play_song()     
