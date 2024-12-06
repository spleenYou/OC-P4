import re
import constant.constant as CONST
from models.tournament import Tournament
from models.player import Player
from models.match import Match
from controllers.load import Load
from controllers.save import Save


class Controller:
    def __init__(self, views):
        self.view = views.Prompts()
        self.save = Save()
        self.all_players_list = Load().read_file_players()
        self.tournaments_list = Load().read_file_tournaments()

    def create_tournament(self):
        name = self.view.tournament_name()
        if name == '':
            return None
        place = self.view.tournament_place()
        description = self.view.tournament_description()
        minimum_number_of_rounds = 4
        number_of_rounds = 0
        while number_of_rounds < minimum_number_of_rounds:
            number_of_rounds = self.view.tournament_number_of_rounds()
            if self.is_int(number_of_rounds):
                number_of_rounds = int(number_of_rounds)
                if number_of_rounds < 4:
                    self.view.message("Erreur", "Le nombre de tour minimum est 4")
            else:
                self.view.message("Erreur", "Veuillez rentrer un nombre")
                number_of_rounds = 0
        min_players = number_of_rounds + 1
        if min_players % 2:
            min_players = min_players + 1
        number_players = 0
        error_message = ''
        while number_players < min_players:
            if error_message != '':
                self.view.message("Erreur", error_message)
            number_players = self.view.tournament_number_players()
            if self.is_int(number_players):
                number_players = int(number_players)
                if (number_players % 2) == 0:
                    if number_players < (number_of_rounds + 2):
                        error_message = f'Nombre de joueurs minimum : {number_of_rounds + 2}'
                else:
                    error_message = 'Nombre de participants impaires'
            else:
                error_message = 'Veuillez rentrer un nombre'
                number_players = 0
        tournament = Tournament(id=len(self.tournaments_list)+1,
                                name=name,
                                place=place,
                                description=description)
        for i in range(number_players):
            tournament.add_player([])
        matches_number = int(number_players / 2)
        for i in range(number_of_rounds):
            tournament.add_round()
        for new_round in tournament.rounds_list:
            matches_list = []
            for k in range(matches_number):
                matches_list.append(Match())
                matches_list[k].define_score_table(([None, 0], [None, 0]))
            new_round.matches_list = matches_list
        self.tournaments_list.append(tournament)
        self.save.save_tournaments(self.tournaments_list)
        return tournament

    def run_tournament(self, tournament):
        self.view.tournament_information(tournament)
        if not tournament.has_all_players():
            self.add_player(tournament)
        while not tournament.is_finished():
            self.view.ranking(tournament.players_list_sort)
            round_number_show = tournament.round_number + 1
            tournament.sort_list()
            matches_list = tournament.rounds_list[tournament.round_number].matches_list
            tournament.make_matches()
            self.view.matches_list(round_number_show, matches_list)
            for match in matches_list:
                match_define = False
                while not match_define:
                    winner_player = self.view.winner_player(match)
                    if self.is_int(winner_player):
                        winner_player = int(winner_player)
                        if (winner_player >= 0) and (winner_player <= 2):
                            match_define = match.define_score(winner_player)
            tournament.sort_list_by_score()
            self.save.save_tournaments(self.tournaments_list)
            tournament.next_round()
        self.view.message("Tournoi terminé", "Voici le résultat du tournoi")
        self.view.end_tournament(tournament.players_list_sort)
        return None

    def choice_tournament(self):
        tournament_choice = None
        while tournament_choice is None:
            tournament_choice = self.view.tournament_choice(self.tournaments_list)
            if self.is_int(tournament_choice):
                if int(tournament_choice) == CONST.QUIT:
                    return None
                elif int(tournament_choice) > len(self.tournaments_list):
                    self.view.message("Erreur", "Veuillez rentrer un tournoi existant")
                    tournament_choice = None
            else:
                self.view.message("Erreur", "Veuillez rentrer un nombre")
        return self.tournaments_list[int(tournament_choice) - 1]

    def add_player(self, tournament):
        players_list_choice = []
        for player in self.all_players_list:
            if player not in tournament.players_list:
                players_list_choice.append(player)
        while not tournament.has_all_players():
            index_player_to_add = None
            while index_player_to_add is None:
                index_player_to_add = self.view.player_choice(players_list_choice)
                if self.is_int(index_player_to_add):
                    index_player_to_add = int(index_player_to_add)
                    if index_player_to_add > 0 and index_player_to_add <= len(players_list_choice):
                        new_player = players_list_choice[index_player_to_add - 1]
                        tournament.add_player(new_player)
                        players_list_choice.remove(new_player)
                    elif index_player_to_add == 0:
                        player_informations = self.view.new_player()
                        new_player = Player(player_informations['surname'],
                                            player_informations['name'],
                                            player_informations['birthday'],
                                            player_informations['chess_id'])
                        self.all_players_list.append(new_player)
                        self.save.save_player(self.all_players_list)
                else:
                    index_player_to_add = None
        self.save.save_tournaments(self.tournaments_list)

    def is_int(self, value_to_check):
        try:
            int(value_to_check)
        except ValueError:
            return False
        else:
            return True

    def add_new_player(self):
        new_player = True
        player_informations_error_message = ""
        birthday_verification_re = re.compile('^[0-9]{2}-[0-9]{2}-[0-9]{4}$')
        chess_id_verification_re = re.compile('^[A-Z]{2}[0-9]{4}$')
        while new_player:
            player_informations = self.view.new_player(player_informations_error_message)
            player_informations_error_message = ""
            if player_informations['name'] != "":
                if not birthday_verification_re.match(player_informations['birthday']):
                    player_informations_error_message = 'Date de naissance incorrecte'
                if not chess_id_verification_re.match(player_informations['chess_id']):
                    player_informations_error_message = 'Chess id invalide'
                if player_informations_error_message == '':
                    self.players.append(Player(player_informations['surname'],
                                               player_informations['name'],
                                               player_informations['birthday'],
                                               player_informations['chess_id']))
            elif len(self.players) > 0:
                new_player = False
            else:
                return self.main_menu()

    def is_first_time(self):
        if self.tournaments_list == []:
            return True
        return False

    def have_an_unfinished_tournament(self):
        for tournament in self.tournaments_list:
            if not tournament.is_finished():
                return True
        return False

    def ask_menu_choice(self, menu):
        if menu == CONST.MAIN:
            have_an_unfinished_tournament = self.have_an_unfinished_tournament()
            menu_choice = self.view.main_menu_choice(have_an_unfinished_tournament)
            if self.is_int(menu_choice):
                menu_choice = int(menu_choice)
            else:
                menu_choice = None
        return menu_choice
