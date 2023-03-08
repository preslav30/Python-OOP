from project.song import Song


class Album:
    def __init__(self, name: str, *songs):
        self.name = name
        self.published = False
        self.songs = list(songs)

    def add_song(self, song: Song):
        if song.single:
            return f"Cannot add {song.name}. It's a single"

        if self.published:
            return f"Cannot add songs. Album is published."

        # if song in self.songs:
        #     return f"Song is already in the album."

        self.songs.append(song)
        return f"Song {song.name} has been added to the album {self.name}."

    def remove_song(self, song_name: str):
        song_found = False
        if self.published:
            return "Cannot remove songs. Album is published."
        for song in self.songs:
            if song_name == song.name:
                song_found = True
        if song_found:
            return f"Removed song {song_name} from album {self.name}."
        else:
            return "Song is not in the album."

    def publish(self):
        if self.published:
            return f"Album {self.name} is already published."
        self.published = True
        return f"Album {self.name} has been published."

    def details(self):
        result = []
        for song in self.songs:
            result.append(f'== {song.get_info()}')
        result_to_print = '\n'.join(result)
        return f"Album {self.name}\n{result_to_print}"

