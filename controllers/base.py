import re
import os
from constante.constante import Constante
from models.tournament import Tournament
from models.player import Player


class Controller:
    def __init__(self, view):
        self.view = view
        self.const = Constante()
        self.tournament = ''

    def run(self):
        pass

    def start_tournament(self):
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

        number_players_validate = False
        error_message = ''
        while not number_players_validate:
            number_players = self.view.prompt_for_tournament_number_players(error_message)
            if number_players != '':
                number_players = int(number_players)
                if (number_players % 2) == 0:
                    if number_players <= (number_of_rounds + 2):
                        number_players_validate = True
                    else:
                        error_message = f'Nombre de joueurs minimum : {number_of_rounds + 2}'
                else:
                    error_message = 'Nombre de participants impaires'
            else:
                error_message = 'Nombre de participant non rentré'
        self.players = [4]
        self.tournament = Tournament(name=name,
                                     place=place,
                                     round_number=0,
                                     players_list=self.players,
                                     description=description,
                                     number_of_rounds=number_of_rounds)
        print(self.tournament)
        self.get_players()

    def list_tournaments(self):
        return ["tournoi"]  # à refaire

    def resume_tournament(self, tournament):
        print("Résumé du tournoi")

    def end_tournament(self):
        pass

    def start_round(self):
        pass

    def end_turn(self):
        pass

    def start_match(self, players):
        pass

    def end_match(self, players):
        pass

    def get_players(self):
        self.view.prompt_for_add_player_choice()

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

    def main_menu(self):
        user_menu_choice = None
        while not user_menu_choice:
            user_menu_choice = self.view.prompt_menu(self.const.MAIN)
            if user_menu_choice == self.const.START_TOURNAMENT:
                self.start_tournament()
            elif user_menu_choice == self.const.RESUME_TOURNAMENT:
                list_tournaments = self.list_tournaments()
                tournaments_number = len(list_tournaments)
                tournament_choice = self.view.prompt_menu(self.const.RESUME_TOURNAMENT, list_tournaments)
                if int(tournament_choice) == 0 or int(tournament_choice) > tournaments_number:
                    user_menu_choice = None
                else:
                    self.resume_tournament(tournament_choice)
            elif user_menu_choice == self.const.LIST_TOURNAMENTS:
                print("liste")
            elif user_menu_choice == self.const.LIST_PLAYERS:
                print("players")
            elif user_menu_choice == self.const.QUIT:
                print('Au revoir !')
                os._exit(os.EX_OK)
            else:
                user_menu_choice = None

    def check_path_data_exist(self):
        if not os.path.exists('data/'):
            os.makedirs('data/')
        self.check_files_data_exist()

    def check_files_data_exist(self):
        if not os.path.isfile(f'data/{self.const.PATH_FILE_PLAYERS_LIST}'):
            with open(f'data/{self.const.PATH_FILE_PLAYERS_LIST}', 'w', newline='') as file:
                file.write('[]')
        if not os.path.isfile(f'data/{self.const.PATH_FILE_TOURNAMENTS_LIST}'):
            with open(f'data/{self.const.PATH_FILE_TOURNAMENTS_LIST}', mode='w', newline='') as file:
                file.write('[]')
