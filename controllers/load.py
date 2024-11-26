import json
from models import player


class Load:

    def load_tournament(self, tournament):
        pass

    def load_data(self, filename):
        players_list = []
        with open(f'data/{filename}', 'r') as json_data:
            players_list_dict = json.load(json_data)
            for player_data_dict in players_list_dict:
                new_player = player.Player(player_data_dict['surname'],
                                           player_data_dict['name'],
                                           player_data_dict['birthday'],
                                           player_data_dict['chess_id'])
                players_list.append(new_player)
        return players_list
