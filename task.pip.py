
#task-10
class Song:
    def __init__(self, title, artist, duration):
        self.title = title
        self.artist = artist
        self.duration = duration

    def __str__(self):
        return f"{self.title} by {self.artist}, Duration: {self.duration}"

class MusicPlayer:
    def __init__(self):
        self.playlist = []
        self.current_song_index = -1
        self.is_playing = False

    def add_song(self, song):
        self.playlist.append(song)

    def play(self):
        if self.playlist:
            self.current_song_index = 0
            self.is_playing = True
            print(f"Playing: {self.playlist[self.current_song_index]}")
        else:
            print("No songs in the playlist.")

    def pause(self):
        if self.is_playing:
            self.is_playing = False
            print("Paused")

    def stop(self):
        if self.is_playing or self.current_song_index != -1:
            self.is_playing = False
            self.current_song_index = -1
            print("Stopped")

    def next_song(self):
        if self.playlist and self.current_song_index < len(self.playlist) - 1:
            self.current_song_index += 1
            print(f"Playing next song: {self.playlist[self.current_song_index]}")
        else:
            print("No more songs in the playlist.")

    def previous_song(self):
        if self.playlist and self.current_song_index > 0:
            self.current_song_index -= 1
            print(f"Playing previous song: {self.playlist[self.current_song_index]}")
        else:
            print("No previous song in the playlist.")

# Example usage
if __name__ == "__main__":
    song1 = Song("Song One", "Artist A", "3:45")
    song2 = Song("Song Two", "Artist B", "4:30")
    player = MusicPlayer()
    player.add_song(song1)
    player.add_song(song2)
    player.play()
    player.next_song()
    player.pause()
    player.stop()
