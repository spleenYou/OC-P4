from views.menus import Menus
from constante.constante import Constante


class View:
    def __init__(self):
        self.const = Constante()
        self.menu_view = Menus()

    def prompt_for_tournament_name(self):
        self.menu_view.headset_menu('Nom du tournoi')
        tournament_name = input('Quel est le nom du tournoi ? ')
        return tournament_name

    def prompt_for_tournament_place(self):
        self.menu_view.headset_menu('Emplacement du tournoi')
        tournament_place = input('Veuillez entrer l\'emplacement du tournoi : ')
        return tournament_place

    def prompt_for_tournament_number_of_rounds(self):
        self.menu_view.headset_menu('Nombre de tours')
        number_of_rounds = input('Combien de tours comprend le tournoi ? ')
        return number_of_rounds

    def prompt_for_tournament_number_players(self, error_message):
        self.menu_view.headset_menu('Nombre de joueurs')
        if error_message != "":
            self.show_message(title='Erreur', message=error_message)
        number_players = input('Combien de joueurs participent au tournoi ? ')
        return number_players

    def prompt_for_new_player(self, error_message):
        player_informations = {}
        self.menu_view.headset_menu('Nouveau joueur')
        if error_message != "":
            self.show_message(title='Erreur', message=error_message)
        player_informations['name'] = input('Quel est le prénom du joueur ? ').capitalize()
        if player_informations['name'] != "":
            player_informations['surname'] = input('Quel est le nom de famille du joueur ? ').upper()
            player_informations['birthday'] = input('Quel est la date de naissance du joueur ? [DD-MM-YYYY] ')
            player_informations['chess_id'] = input('Quel est l\'identifiant du joueur ? ').upper()
        return player_informations

    def prompt_for_add_player_choice(self):
        pass

    def prompt_for_tournament_description(self):
        self.menu_view.headset_menu('Description du tournoi')
        tournament_description = input('Veuillez entrer la description du tournoi : ')
        return tournament_description

    def prompt_for_tournament_new_tournament(self):
        pass

    def prompt_menu(self, menu_choice, list_to_show=[]):
        if menu_choice == self.const.MAIN:
            self.menu_view.main_menu()
            user_choice = input('Quel est votre choix ? ')
            if user_choice == "1":
                return self.const.START_TOURNAMENT
            elif user_choice == "2":
                return self.const.RESUME_TOURNAMENT
            elif user_choice == "3":
                return self.const.LIST_TOURNAMENTS
            elif user_choice == "4":
                return self.const.LIST_PLAYERS
            elif user_choice == "5":
                return self.const.QUIT
            else:
                return None
        elif menu_choice == self.const.RESUME_TOURNAMENT:
            self.menu_view.list_tournaments_menu(list_to_show)
            tournament_choice = input('Quel tournoi reprendre ?')
            return tournament_choice

    def show_message(self, title, message, need_pause=False):
        self.menu_view.headset_menu(title)
        self.menu_view.message_view(message)
        if need_pause:
            input('Appuyer sur une touche pour continuer...')
