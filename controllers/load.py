import json
from models.player import Player
from models.tournament import Tournament
import constant.constant as CONST


class Load:

    def __init__(self):
        pass

    def load_tournament(self, tournament):
        pass

    def read_file_players(self):
        players_list = []
        players_list_dict = self.read_json_file(CONST.FILENAME_PLAYERS_LIST)
        for player_data_dict in players_list_dict:
            players_list.append(Player(player_data_dict['surname'],
                                player_data_dict['name'],
                                player_data_dict['birthday'],
                                player_data_dict['chess_id']))
        return players_list

    def read_file_tournaments(self):
        tournaments_list = []
        with open(f'data/{CONST.FILENAME_TOURNAMENTS_LIST}', 'r') as json_data:
            tournaments_list_dict = json.load(json_data)
        for tournament_data_dict in tournaments_list_dict:
            players_list = []
            rounds_list = []
            matches_list = []
            for player in tournament_data_dict['players_list']:
                players_list.append(self.find_player_data_by_chess_id(player['chess_id']))
            for round in tournament_data_dict['rounds_list']:
                for match in round:
                    matches_list.append([match[0], match[1]])
                rounds_list.append(matches_list)
            tournaments_list.append(Tournament(name=tournament_data_dict['name'],
                                               place=tournament_data_dict['place'],
                                               players_list=players_list,
                                               description=tournament_data_dict['description'],
                                               id=tournament_data_dict['id'],
                                               date_start=tournament_data_dict['date_start'],
                                               date_stop=tournament_data_dict['date_stop'],
                                               number_of_rounds=tournament_data_dict['number_of_rounds'],
                                               rounds_list=rounds_list))
        return tournaments_list

    def find_player_data_by_chess_id(self, chess_id):
        players_list_dict = self.read_json_file(CONST.FILENAME_PLAYERS_LIST)
        for player_data_dict in players_list_dict:
            if player_data_dict['chess_id'] == chess_id:
                player = Player(player_data_dict['surname'],
                                player_data_dict['name'],
                                player_data_dict['birthday'],
                                player_data_dict['chess_id'])
        return player

    def read_json_file(self, FILENAME):
        with open(f'data/{FILENAME}', 'r') as json_data:
            return json.load(json_data)
