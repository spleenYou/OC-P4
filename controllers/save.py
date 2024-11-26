import json
from constante import constante


class Save:
    def __init__(self):
        self.const = constante.Constante()

    def save_tournament(self, tournament_to_save, tournaments_list):
        tournament_update = False
        new_list_tournaments = []
        if len(tournaments_list) > 0:
            for tournament in tournaments_list:
                if tournament.id == tournament_to_save.id:
                    tournament = tournament_to_save
                    tournament_update = True
                new_list_tournaments.append(tournament)
        if not tournament_update:
            new_list_tournaments.append(tournament_to_save)
        tournaments_list_dict = []
        for tournament in new_list_tournaments:
            players_list = []
            for player in tournament.players_list:
                players_list.append({'chess_id': player.chess_id})
            tournaments_list_dict.append({'name': tournament.name,
                                          'place': tournament.place,
                                          'round_number': tournament.round_number,
                                          'players_list': players_list,
                                          'description': tournament.description,
                                          'id': tournament.id,
                                          'date_start': tournament.date_start,
                                          'date_stop': tournament.date_stop,
                                          'number_of_rounds': tournament.round_number,
                                          'rounds_list': tournament.rounds_list})
        self.save_data(self.const.FILENAME_TOURNAMENTS_LIST, tournaments_list_dict)
        if tournament_update:
            return "Sauvegarde du tournoi mis à jour"
        else:
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
            self.save_data(self.const.LIST_PLAYERS, players_list)
            return 'Joueur sauvegardé'
        else:
            return 'Le joueur existe déja'

    def save_data(self, filename, content_file):
        with open(f'data/{filename}', 'w') as file:
            json.dump(content_file, file, indent=4, sort_keys=True)
