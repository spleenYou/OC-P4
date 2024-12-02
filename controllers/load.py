import json
from models.tournament import Tournament
from models.round import Round
from models.match import Match
from models.player import Player
import constant.constant as CONST


class Load:
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
            tournament = Tournament(name=tournament_data_dict['name'],
                                    place=tournament_data_dict['place'],
                                    description=tournament_data_dict['description'],
                                    id=tournament_data_dict['id'],
                                    date_start=tournament_data_dict['date_start'],
                                    date_stop=tournament_data_dict['date_stop'])
            for player in tournament_data_dict['players_list']:
                player_data = None
                if len(player['chess_id']):
                    player_data = self.find_player_data_by_chess_id(player['chess_id'])
                tournament.add_player(player_data)
            for round in tournament_data_dict['rounds_list']:
                matches_list = []
                for match in round:
                    score_list = []
                    for score in match:
                        score_list.append([self.find_player_data_by_chess_id(score[0]), score[1]])
                    matches_list.append(Match(score_list))
                tournament.add_round(Round(matches_list=matches_list))
            tournaments_list.append(tournament)
        return tournaments_list

    def find_player_data_by_chess_id(self, chess_id):
        player_find = []
        players_list_dict = self.read_json_file(CONST.FILENAME_PLAYERS_LIST)
        for player_data_dict in players_list_dict:
            if player_data_dict['chess_id'] == chess_id:
                player_find = Player(player_data_dict['surname'],
                                     player_data_dict['name'],
                                     player_data_dict['birthday'],
                                     player_data_dict['chess_id'])
                return player_find
        return None

    def read_json_file(self, FILENAME):
        with open(f'data/{FILENAME}', 'r') as json_data:
            return json.load(json_data)
