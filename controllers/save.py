import json
import constant.constant as CONST


class Save:
    def save_tournament(self, tournament_to_save, tournaments_list):
        if len(tournaments_list) > 0:
            for tournament in tournaments_list:
                if tournament.id == tournament_to_save.id:
                    tournaments_list.remove(tournament)
        tournaments_list.append(tournament_to_save)
        tournaments_list_dict = []
        for tournament in tournaments_list:
            players_list = []
            rounds_list = []
            matches_list = []
            for player in tournament.players_list:
                players_list.append({'chess_id': player.chess_id})
            for rounds in tournament.rounds_list:
                for match in rounds:
                    matches_list.append([match.score[0], match.score[1]])
                rounds_list.append(matches_list)
            tournaments_list_dict.append({'name': tournament.name,
                                          'place': tournament.place,
                                          'number_of_rounds': tournament.number_of_rounds,
                                          'players_list': players_list,
                                          'description': tournament.description,
                                          'id': tournament.id,
                                          'date_start': tournament.date_start,
                                          'date_stop': tournament.date_stop,
                                          'rounds_list': rounds_list})
        self.save_data(CONST.FILENAME_TOURNAMENTS_LIST, tournaments_list_dict)
        return "Tournoi sauvegardé"

    def save_player(self, new_player, players_list):
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
            self.save_data(CONST.LIST_PLAYERS, players_list)
            return 'Joueur sauvegardé'
        else:
            return 'Le joueur existe déja'

    def save_data(self, filename, content_file):
        with open(f'data/{filename}', 'w') as file:
            json.dump(content_file, file, indent=4, sort_keys=True)
