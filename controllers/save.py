import json
import constant.constant as CONST
from models.player import Player


class Save:
    def save_tournaments(self, tournaments_list):
        tournaments_list_dict = []
        for tournament in tournaments_list:
            players_list = []
            rounds_list = []
            for player in tournament.players_list:
                chess_id = ''
                if isinstance(player, Player):
                    chess_id = player.chess_id
                players_list.append({'chess_id': chess_id})
            for round in tournament.rounds_list:
                matches_list = []
                for match in round.matches_list:
                    scores_list = []
                    white_player_chess_id = ""
                    black_player_chess_id = ""
                    if match.have_players():
                        white_player_chess_id = match.white_player["player"].chess_id
                        black_player_chess_id = match.black_player["player"].chess_id
                    scores_list.append([white_player_chess_id, match.white_player["score"]])
                    scores_list.append([black_player_chess_id, match.black_player["score"]])
                    matches_list.append(scores_list)
                rounds_list.append(matches_list)
            tournaments_list_dict.append({'name': tournament.name,
                                          'place': tournament.place,
                                          'players_list': players_list,
                                          'description': tournament.description,
                                          'date_start': tournament.date_start,
                                          'date_end': tournament.date_end,
                                          'rounds_list': rounds_list})
        self.save_data(CONST.FILENAME_TOURNAMENTS_LIST, tournaments_list_dict)
        return "Tournoi sauvegardé"

    def save_player(self, all_players_list):
        players_list_to_save = []
        for player in all_players_list:
            players_list_to_save.append({'surname': player.surname,
                                         'name': player.name,
                                         'birthday': player.birthday,
                                         'chess_id': player.chess_id})
        self.save_data(CONST.FILENAME_PLAYERS_LIST, players_list_to_save)

    def save_data(self, filename, content_file):
        with open(f'data/{filename}', 'w') as file:
            json.dump(content_file, file, indent=4, sort_keys=True)
