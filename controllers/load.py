import json
from models.tournament import Tournament
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
                player_data = []
                if len(player['chess_id']):
                    player_data = self.find_player_data_by_chess_id(player['chess_id'])
                tournament.add_player(player_data)
            for round in tournament_data_dict['rounds_list']:
                new_round = tournament.add_round()
                for match in round:
                    new_match = new_round.add_match()
                    score_list = []
                    for score in match:
                        if score[0] == "null":
                            player = None
                        else:
                            player = self.find_player_data_by_chess_id(score[0], tournament.players_list)
                        score_list.append([player, score[1]])
                    new_match.define_score_table(score_list)
                    if player is not None:
                        new_match.update_score()
            if tournament.has_all_players():
                tournament.sort_list_by_score()
            tournament.count_round_number()
            tournaments_list.append(tournament)
        return tournaments_list

    def find_player_data_by_chess_id(self, chess_id, players_list=None):
        player_find = []
        if players_list is not None:
            for player in players_list:
                if player.chess_id == chess_id:
                    return player
        else:
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
