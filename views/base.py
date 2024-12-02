from views.menus import Menus
import constant.constant as CONST


class View:
    def __init__(self):
        self.menu = Menus()

    def prompt_for_tournament_name(self):
        self.menu.view_menu(title='Nom du tournoi')
        tournament_name = input('Quel est le nom du tournoi ? ')
        return tournament_name

    def prompt_for_tournament_place(self):
        self.menu.view_menu('Emplacement du tournoi')
        tournament_place = input('Veuillez entrer l\'emplacement du tournoi : ')
        return tournament_place

    def prompt_for_tournament_number_of_rounds(self):
        self.menu.view_menu('Nombre de tours')
        number_of_rounds = input('Combien de tours comprend le tournoi ? ')
        return number_of_rounds

    def prompt_for_tournament_number_players(self):
        self.menu.view_menu('Nombre de joueurs')
        number_players = input('Combien de joueurs participent au tournoi ? ')
        return number_players

    def prompt_for_new_player(self):
        player_informations = {}
        self.menu.view_menu('Nouveau joueur')
        player_informations['name'] = input('Quel est le prénom du joueur ? ').capitalize()
        if player_informations['name'] != "":
            player_informations['surname'] = input('Quel est le nom de famille du joueur ? ').upper()
            player_informations['birthday'] = input('Quel est la date de naissance du joueur ? [DD-MM-YYYY] ')
            player_informations['chess_id'] = input('Quel est l\'identifiant du joueur ? ').upper()
        return player_informations

    def prompt_for_tournament_description(self):
        self.menu.view_menu('Description du tournoi')
        tournament_description = input('Veuillez entrer la description du tournoi : ')
        return tournament_description

    def prompt_for_tournament_choice(self, tounaments_list):
        tournament_choice = self.menu.list_tournaments_menu(tounaments_list)
        return tournament_choice

    def show_tournament_information(self, tournament):
        self.menu.view_menu("Information sur le tournoi", CONST.SHOW_TOURNAMENT_INFORMATIONS, tournament)
        input('Appuyer sur une touche pour continuer...')

    def prompt_for_player_choice(self, players_list):
        self.menu.view_menu(title="Ajout d'un joueur", view=CONST.MENU_PLAYER_CHOICE, thing_to_show=players_list)
        add_player_choice = input("Comment ajouter le joueur ? ")
        return add_player_choice

    def prompt_for_player_update(self, old_player_informations, new_player):
        players_data = [old_player_informations, new_player]
        self.menu.view_menu(title="Doublon détecté", menu=CONST.UPDATE_PLAYER_CHOICE, thing_to_show=players_data)
        update_choice = input("Souhaitez-vous mettre à jour le joueur (y/n) ?")
        return update_choice

    def show_matches_list(self, round_number, matches_list):
        self.menu.view_menu(f"Voici les matchs du Round {round_number}", CONST.SHOW_MATCHES_LIST, matches_list)
        input('Appuyer sur une touche pour continuer...')

    def prompt_menu(self, menu_choice, list_to_show=None):
        if menu_choice == CONST.MAIN:
            self.menu.view_menu("Menu principal", menu_choice, list_to_show)
            user_choice = input('Quel est votre choix ? ')
            if user_choice == "1":
                return CONST.CREATE_TOURNAMENT
            elif user_choice == "2" and not list_to_show:
                return CONST.RESUME_TOURNAMENT
            elif user_choice == "3":
                return CONST.LIST_TOURNAMENTS
            elif user_choice == "4":
                return CONST.LIST_PLAYERS
            elif user_choice == "0":
                return CONST.QUIT
            else:
                return None
        elif menu_choice == CONST.MENU_LIST_TOURNAMENTS:
            self.menu.view_menu("Liste des tournois", menu_choice, list_to_show)
            tournament_choice = input('Quel tournoi reprendre ? ')
            return tournament_choice

    def show_message(self, title, message):
        self.menu.view_menu(title, CONST.MESSAGE, message)
        input('Appuyer sur une touche pour continuer...')
