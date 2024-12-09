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
        self.tournaments_list = Load().read_file_tournaments(self.all_players_list)

    def create_tournament(self):
        name = self.view.prompt_for_tournament_name()
        if name == '':
            return None
        place = self.view.prompt_for_tournament_place()
        description = self.view.prompt_for_tournament_description()
        minimum_number_of_rounds = 4
        number_of_rounds = 0
        while number_of_rounds < minimum_number_of_rounds:
            number_of_rounds = self.view.prompt_for_tournament_number_of_rounds()
            if self.is_int(number_of_rounds):
                number_of_rounds = int(number_of_rounds)
                if number_of_rounds < 4:
                    self.view.message("Erreur", "Le nombre de tour minimum est 4")
            else:
                self.view.message("Erreur", "Veuillez rentrer un nombre")
                number_of_rounds = 0
        minimum_players = number_of_rounds + 3
        if minimum_players % 2:
            minimum_players = minimum_players + 1
        number_players = 0
        while number_players == 0:
            number_players = self.view.prompt_for_tournament_number_players()
            if self.is_int(number_players):
                number_players = int(number_players)
                if (number_players % 2) == 0:
                    if number_players < minimum_players:
                        self.view.message("Erreur", f"Nombre de joueurs minimum : {minimum_players}")
                        number_players = 0
                else:
                    self.view.message("Erreur", "Nombre de participants impaires")
                    number_players = 0
            else:
                self.view.message("Erreur", "Veuillez rentrer un nombre")
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
                matches_list.append(Match(None, 0, None, 0))
            new_round.matches_list = matches_list
        self.tournaments_list.append(tournament)
        self.save.save_tournaments(self.tournaments_list)
        return tournament

    def run_tournament(self, tournament):
        self.view.show_tournament_information(tournament)
        if not tournament.has_all_players():
            self.add_player(tournament)
        self.update_tournament_players_scores(tournament)
        while not tournament.is_finished():
            self.view.show_ranking(tournament.players_list)
            round_number_show = tournament.round_number + 1
            tournament.sort_list()
            matches_list = tournament.rounds_list[tournament.round_number].matches_list
            tournament.make_matches()
            self.view.show_matches_list(round_number_show, matches_list)
            for match in matches_list:
                match_define = False
                while not match_define:
                    winner_player = self.view.show_match_result(match)
                    if self.is_int(winner_player):
                        winner_player = int(winner_player)
                        if (winner_player >= 0) and (winner_player <= 2):
                            match winner_player:
                                case 0:
                                    winner_player = None
                                case 1:
                                    winner_player = match.white_player
                                case 2:
                                    winner_player = match.black_player
                            match_define = match.define_score(winner_player)
            tournament.sort_list_by_score()
            self.save.save_tournaments(self.tournaments_list)
            tournament.next_round()
        self.view.message("Tournoi terminé", "Voici le résultat du tournoi")
        self.view.show_end_tournament(tournament.players_list)
        return None

    def update_tournament_players_scores(self, tournament):
        for player in tournament.players_list:
            player.score = 0
        for round in tournament.rounds_list:
            if round.is_finished():
                for match in round.matches_list:
                    match.update_score()

    def choice_tournament(self):
        tournament_choice = None
        tournaments_finished_list = []
        for tournament in self.tournaments_list:
            if not tournament.is_finished():
                tournaments_finished_list.append({"tournament": tournament,
                                                  "index": self.tournaments_list.index(tournament)})
        while tournament_choice is None:
            tournament_choice = self.view.prompt_for_tournament_choice(tournaments_finished_list)
            if self.is_int(tournament_choice):
                tournament_choice = int(tournament_choice)
                if tournament_choice == CONST.QUIT:
                    return None
                elif tournament_choice > len(tournaments_finished_list):
                    self.view.message("Erreur", "Veuillez rentrer un tournoi existant")
                    tournament_choice = None
            else:
                self.view.message("Erreur", "Veuillez rentrer un nombre")
                tournament_choice = None
        return tournaments_finished_list[tournament_choice - 1]["tournament"]

    def add_player(self, tournament):
        players_list_choice = []
        for player in self.all_players_list:
            if player not in tournament.players_list:
                players_list_choice.append(player)
        while not tournament.has_all_players():
            index_player_to_add = None
            while index_player_to_add is None:
                if len(players_list_choice):
                    index_player_to_add = self.view.prompt_for_player_choice(players_list_choice)
                else:
                    index_player_to_add = 0
                if self.is_int(index_player_to_add):
                    new_player = None
                    index_player_to_add = int(index_player_to_add)
                    if index_player_to_add > 0 and index_player_to_add <= len(players_list_choice):
                        new_player = players_list_choice[index_player_to_add - 1]
                        tournament.add_player(new_player)
                        players_list_choice.remove(new_player)
                    elif index_player_to_add == 0:
                        new_player = self.add_new_player()
                        if new_player:
                            tournament.add_player(new_player)
                            self.all_players_list.append(new_player)
                        else:
                            index_player_to_add = None
                    if new_player:
                        self.save.save_player(self.all_players_list)
                        self.save.save_tournaments(self.tournaments_list)
                else:
                    index_player_to_add = None

    def is_int(self, value_to_check):
        try:
            int(value_to_check)
        except ValueError:
            return False
        else:
            return True

    def add_new_player(self):
        birthday_verification_re = re.compile('^[0-9]{2}-[0-9]{2}-[0-9]{4}$')
        chess_id_verification_re = re.compile('^[A-Z]{2}[0-9]{4}$')
        new_player_name = self.view.prompt_for_new_player_name()
        if new_player_name != "":
            new_player_surname = self.view.prompt_for_new_player_surname(new_player_name)
            new_player_birthday = None
            while not new_player_birthday:
                new_player_birthday = self.view.prompt_for_new_player_birthday(new_player_name, new_player_surname)
                if not birthday_verification_re.match(new_player_birthday):
                    self.view.message("Erreur", "Date de naissance incorrecte")
                    new_player_birthday = None
            new_player_chess_id = None
            while not new_player_chess_id:
                new_player_chess_id = self.view.prompt_for_new_player_chess_id(new_player_name, new_player_surname)
                if not chess_id_verification_re.match(new_player_chess_id):
                    self.view.message("Erreur", "Chess id invalide")
                    new_player_chess_id = None
            return Player(new_player_surname,
                          new_player_name,
                          new_player_birthday,
                          new_player_chess_id)
        else:
            return None

    def is_first_time(self):
        if self.tournaments_list == []:
            return True
        return False

    def main_menu(self, have_tournament, have_an_unfinished_tournament):
        menu_choice = self.view.prompt_for_main_menu_choice(have_tournament, have_an_unfinished_tournament)
        if self.is_int(menu_choice):
            return int(menu_choice)
        else:
            return None

    def tournaments_updates(self):
        user_choice = None
        while user_choice is None:
            user_choice = self.view.prompt_for_tournaments_management(self.tournaments_list)
            if self.is_int(user_choice):
                user_choice = int(user_choice)
                if user_choice == 0:
                    return None
                if user_choice <= len(self.tournaments_list):
                    self.update_tournament(self.tournaments_list[user_choice - 1])
                if user_choice > len(self.tournaments_list):
                    self.view.message("Erreur", "Le tournoi sélectionné n'est pas dans la liste")
            else:
                user_choice = None
        return None

    def update_tournament(self, tournament):
        new_tournament_name = self.view.prompt_for_tournament_name(tournament.name)
        new_tournament_place = self.view.prompt_for_tournament_place(tournament.place)
        new_tournament_description = self.view.prompt_for_tournament_description(tournament.description)
        if new_tournament_name != '':
            tournament.name = new_tournament_name
        if new_tournament_place:
            tournament.place = new_tournament_place
        if new_tournament_description:
            tournament.description = new_tournament_description
