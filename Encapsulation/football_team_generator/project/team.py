from project.player import Player


class Team:
    def __init__(self, name: str, rating: int):
        self.__name = name
        self.__rating = rating
        self.__players = []

    def add_player(self, player: Player):
        if player in self.__players:
            return f"Player {player.name} has already joined"
        else:
            self.__players.append(player)
            return f'Player {player.name} joined team {self.__name}'

    def remove_player(self, player_name: str):
        player_found = False
        player_object = None
        for player in self.__players:
            if player.name == player_name:
                player_found = True
                player_object = player
        if player_found:
            self.__players.remove(player_object)
            return player
        else:
            return f"Player {player_name} not found"

