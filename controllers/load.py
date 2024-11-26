import json
from models import player
from models import tournament
from constante import constante


class Load:

    def __init__(self):
        self.const = constante.Constante()

    def load_tournament(self, tournament):
        pass

    def load_data_players(self):
        players_list = []
        with open(f'data/{self.const.PATH_FILE_PLAYERS_LIST}', 'r') as json_data:
            players_list_dict = json.load(json_data)
            for player_data_dict in players_list_dict:
                new_player = player.Player(player_data_dict['surname'],
                                           player_data_dict['name'],
                                           player_data_dict['birthday'],
                                           player_data_dict['chess_id'])
                players_list.append(new_player)
        return players_list

    def load_data_tournaments(self):
        tournaments_list = []
        with open(f'data/{self.const.PATH_FILE_TOURNAMENTS_LIST}', 'r') as json_data:
            tournaments_list_dict = json.load(json_data)
            for tournament_data_dict in tournaments_list_dict:
                new_tournament = tournament.Tournament(name=tournament_data_dict['name'],
                                                       place=tournament_data_dict['place'],
                                                       round_number=tournament_data_dict['round_number'],
                                                       players_list=tournament_data_dict['players_list'],
                                                       description=tournament_data_dict['description'],
                                                       id=tournament_data_dict['id'],
                                                       date_start=tournament_data_dict['date_start'],
                                                       date_stop=tournament_data_dict['date_stop'],
                                                       number_of_rounds=tournament_data_dict['number_of_rounds'])
                tournaments_list.append(new_tournament)
        return tournaments_list
