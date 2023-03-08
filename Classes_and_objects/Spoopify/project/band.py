from project.album import Album
from project.song import Song


class Band:
    def __init__(self, name: str):
        self.albums = []
        self.name = name

    def add_album(self, album: Album):
        album_found = False
        for a in self.albums:
            if a.name == album.name:
                album_found = True
        if album_found:
            return f"Band {self.name} already has {album.name} in their library."
        else:
            self.albums.append(album)
            return f"Band {self.name} has added their newest album {album.name}."

    def remove_album(self, album_name: str):
        a_found = False
        for album in self.albums:
            if album.name == album_name:
                a_found = True
                if album.published:
                    return f"Album has been published. It cannot be removed."
                else:
                    return f"Album {album_name} has been removed."
        if not a_found:
            return f"Album {album_name} is not found."

    def details(self):
        result = []
        for album in self.albums:
            result.append(album.details())
        to_print = '\n'.join(result)
        return f"Band {self.name}\n{to_print}"


song = Song("Running in the 90s", 3.45, False)
print(song.get_info())
album = Album("Initial D", song)
second_song = Song("Around the World", 2.34, False)
print(album.add_song(second_song))
print(album.details())
print(album.publish())
band = Band("Manuel")
print(band.add_album(album))
print(band.remove_album("Initial D"))
print(band.details())
