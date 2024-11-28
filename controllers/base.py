import re
import constant.constant as CONST
from models.tournament import Tournament
from models.player import Player
from controllers.load import Load
from controllers.save import Save


class Controller:
    def __init__(self, view):
        self.view = view
        self.save = Save()
        self.list_players = Load().read_file_players()
        self.tournaments_list = Load().read_file_tournaments()

    def create_tournament(self):
        name = self.view.prompt_for_tournament_name()
        if name == '':
            return self.main_menu()
        place = self.view.prompt_for_tournament_place()
        description = self.view.prompt_for_tournament_description()
        number_of_rounds = 0
        while number_of_rounds < 4:
            number_of_rounds = self.view.prompt_for_tournament_number_of_rounds()
            if number_of_rounds != '':
                number_of_rounds = int(number_of_rounds)
                if number_of_rounds < 4:
                    self.view.show_message(title="Erreur", message="Le nombre de tour minimum est 4", need_pause=True)
            else:
                number_of_rounds = 0
        min_players = 6
        number_players = 0
        error_message = ''
        while number_players < min_players:
            if error_message != '':
                self.view.show_message(title="Erreur", message=error_message, need_pause=True)
            number_players = self.view.prompt_for_tournament_number_players()
            if number_players != '':
                number_players = int(number_players)
                if (number_players % 2) == 0:
                    if number_players < (number_of_rounds + 2):
                        error_message = f'Nombre de joueurs minimum : {number_of_rounds + 2}'
                else:
                    error_message = 'Nombre de participants impaires'
            else:
                error_message = 'Nombre de participant invalide'
        players_list = []
        for i in range(number_players):
            players_list.append([])
        rounds_list = []
        for i in range(number_of_rounds):
            rounds_list.append([])
        tournament = Tournament(id=len(self.tournaments_list)+1,
                                name=name,
                                place=place,
                                players_list=players_list,
                                description=description,
                                number_of_rounds=number_of_rounds,
                                rounds_list=rounds_list)
        self.tournaments_list.append(tournament)
        self.save.save_tournament(self.tournaments_list)
        return tournament

    def run_tournament(self, tournament):
        self.view.show_tournament_information(tournament)
        players_list_complete = self.check_players(tournament.players_list)
        if not players_list_complete:
            self.add_player(tournament.players_list)

    def check_players(self, players_list):
        for player in players_list:
            if not isinstance(player, Player):
                return False
        return True

    def choice_tournament(self):
        tournament_choice = self.view.prompt_menu(CONST.MENU_LIST_TOURNAMENTS, self.tournaments_list)
        tournament = self.tournaments_list[int(tournament_choice) - 1]
        return tournament

    def start_round(self):
        pass

    def end_turn(self):
        pass

    def start_match(self, players):
        pass

    def end_match(self, players):
        pass

    def get_players(self):
        add_choice = self.view.prompt_for_add_player_choice()
        print(add_choice)

    def add_existant_player(self):
        pass

    def add_new_player(self):
        new_player = True
        player_informations_error_message = ""
        birthday_verification_re = re.compile('^[0-9]{2}-[0-9]{2}-[0-9]{4}$')
        chess_id_verification_re = re.compile('^[A-Z]{2}[0-9]{4}$')
        while new_player:
            player_informations = self.view.prompt_for_new_player(player_informations_error_message)
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

    def ask_menu_choice(self, menu):
        if menu == CONST.MAIN:
            menu_choice = self.view.prompt_menu(CONST.MAIN)
        return menu_choice
