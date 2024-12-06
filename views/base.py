import constant.constant as CONST
from views.shows import Shows


class Prompts:
    def __init__(self):
        self.show = Shows()

    def tournament_name(self):
        self.show.show("Création d'un tournoi", CONST.MESSAGE, "Nom du tournoi")
        tournament_name = input('Quel est le nom du tournoi ? ')
        return tournament_name

    def tournament_place(self):
        self.show.show("Création d'un tournoi", CONST.MESSAGE, 'Emplacement du tournoi')
        tournament_place = input('Veuillez entrer l\'emplacement du tournoi : ')
        return tournament_place

    def tournament_number_of_rounds(self):
        self.show.show("Création d'un tournoi", CONST.MESSAGE, 'Nombre de tours')
        number_of_rounds = input('Combien de tours comprend le tournoi ? ')
        return number_of_rounds

    def tournament_number_players(self):
        self.show.show("Création d'un tournoi", CONST.MESSAGE, 'Nombre de joueurs')
        number_players = input('Combien de joueurs participent au tournoi ? ')
        return number_players

    def tournament_description(self):
        self.show.show("Création d'un tournoi", CONST.MESSAGE, 'Description du tournoi')
        tournament_description = input('Veuillez entrer la description du tournoi : ')
        return tournament_description

    def ranking(self, players_list):
        self.show.show("Classement provisoire", CONST.RANKING, players_list)
        input('Appuyer sur une touche pour continuer...')
        return None

    def end_tournament(self, players_list):
        self.show.show("Classement final", CONST.END_TOURNAMENT, players_list)
        input("Appuyer sur une touche...")
        return None

    def new_player(self):
        player_informations = {}
        self.menu.view_menu('Nouveau joueur')
        player_informations['name'] = input('Quel est le prénom du joueur ? ').capitalize()
        if player_informations['name'] != "":
            player_informations['surname'] = input('Quel est le nom de famille du joueur ? ').upper()
            player_informations['birthday'] = input('Quel est la date de naissance du joueur ? [DD-MM-YYYY] ')
            player_informations['chess_id'] = input('Quel est l\'identifiant du joueur ? ').upper()
        return player_informations

    def tournament_choice(self, tounaments_list):
        self.show.show("Liste des tournois", CONST.LIST_TOURNAMENTS, tounaments_list)
        tournament_choice = input("Quel tournoi voulez vous continuer ? ")
        return tournament_choice

    def tournament_information(self, tournament):
        self.show.show("Information sur le tournoi", CONST.TOURNAMENT_INFORMATIONS, tournament)
        input('Appuyer sur une touche pour continuer...')

    def player_choice(self, players_list):
        self.show.show("Ajout d'un joueur", CONST.PLAYER_CHOICE, players_list)
        add_player_choice = input("Comment ajouter le joueur ? ")
        return add_player_choice

    def player_update(self, old_player_informations, new_player):
        players_data = [old_player_informations, new_player]
        self.show.show("Doublon détecté", CONST.UPDATE_PLAYER_CHOICE, players_data)
        update_choice = input("Souhaitez-vous mettre à jour le joueur (y/n) ?")
        return update_choice

    def matches_list(self, round_number, matches_list):
        self.show.show(f"Voici les matchs du Round {round_number}", CONST.MATCHES_LIST, matches_list)
        input('Appuyer sur une touche pour continuer...')

    def winner_player(self, match):
        self.show.show("Résultat du match", CONST.MATCH, match)
        winner_player = input("Qui est le vainqueur ? ")
        return winner_player

    def main_menu_choice(self, have_an_unfinished_tournament):
        self.show.show("Menu principal", CONST.MAIN, have_an_unfinished_tournament)
        user_choice = input('Que souhaitez-vous faire ? ')
        return user_choice

    def tournament_list(self):
        tournament_choice = input('Quel tournoi reprendre ? ')
        return tournament_choice

    def message(self, title, message):
        self.show.show(title, CONST.MESSAGE, message)
        input('Appuyer sur une touche pour continuer...')
