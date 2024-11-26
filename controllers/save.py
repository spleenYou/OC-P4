import json


class Save:
    def __init__(self):
        pass

    def save_tournament(self, tournament):
        pass

    def save_player(self, new_player, players_list):
        file_name_players_list = 'players.json'
        player_already_save = False
        if len(players_list) > 0:
            for player in players_list:
                if player.chess_id == new_player.chess_id:
                    player_already_save = True
        if not player_already_save:
            players_list.append({'surname': new_player.surname,
                                 'name': new_player.name,
                                 'birthday': new_player.birthday,
                                 'chess_id': new_player.chess_id})
            self.save_data(file_name_players_list, players_list)
            return 'Joueur sauvegardé'
        else:
            return 'Le joueur existe déja'

    def save_round(self, round):
        pass

    def save_match(self, match):
        pass

    def save_data(self, filename, content_file):
        with open(f'data/{filename}', 'w') as file:
            json.dump(content_file, file, indent=4, sort_keys=True)
