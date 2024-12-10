from views.show import Show


class Prompt:
    def __init__(self):
        self.show = Show()

    def for_tournament_name(self, tournament_name=None):
        self.show.tournament_name(tournament_name)
        tournament_name = input("Quel est le nouveau nom du tournoi ? ")
        return tournament_name

    def for_tournament_place(self, tournament_place=None):
        self.show.tournament_place(tournament_place)
        tournament_place = input("Où se trouve le tournoi ? ")
        return tournament_place

    def for_tournament_number_of_rounds(self):
        self.show.display("Création d'un tournoi", ["Nombre de tours"], "center")
        number_of_rounds = input("Combien de tours comprend le tournoi ? ")
        return number_of_rounds

    def for_tournament_number_players(self):
        self.show.display("Création d'un tournoi", ["Nombre de joueurs"], "center")
        number_players = input("Combien de joueurs participent au tournoi ? ")
        return number_players

    def for_tournament_description(self, tournament_description=None):
        self.show.tournament_description(tournament_description)
        tournament_description = input("Veuillez entrer la description du tournoi : ")
        return tournament_description

    def for_player_name(self, player_name=None):
        self.show.player_name(player_name)
        player_name = input("Quel est le prénom du joueur ? ").capitalize()
        return player_name

    def for_player_surname(self, player_name, player_surname=None):
        self.show.player_surname(player_name, player_surname)
        player_surname = input(f"Quel est le nom de famille de {player_name} ? ").upper()
        return player_surname

    def for_player_birthday(self, player_name, player_surname, player_birthday=None):
        self.show.player_birthday(player_name, player_surname, player_birthday)
        player_birthday = input(f"Quel est la date de naissance de {player_surname} {player_name} ? [DD-MM-YYYY] ")
        return player_birthday

    def for_player_chess_id(self, player_name, player_surname, player_chess_id=None):
        self.show.player_chess_id(player_name, player_surname, player_chess_id)
        player_chess_id = input(f"Quel est l'identifiant de {player_surname} {player_name} ? ").upper()
        return player_chess_id

    def for_tournament_choice(self, tournaments_list):
        self.show.tournaments_list(tournaments_list)
        tournament_choice = input("Quel tournoi choisissez-vous ? ")
        return tournament_choice

    def for_player_choice(self, players_list):
        self.show.players(players_list)
        add_player_choice = input("Quel joueur ajouter au tournoi ? ")
        return add_player_choice

    def for_player_update(self, old_player_informations, new_player):
        # a refaire
        players_data = [old_player_informations, new_player]
        for player in players_data:
            if players_data.index(player) == 0:
                self.decorated_text(f"Pour le Chess ID : {player.chess_id}", align="left")
                self.decorated_text("")
                self.decorated_text("Anciennes données :", align="left")
            else:
                self.decorated_text("Nouvelles données :", align="left")
            self.decorated_text(f" Nom de famille : {player.surname}", align="left")
            self.decorated_text(f" Prénom : {player.name}", align="left")
            self.decorated_text(f" Date de naissance : {player.birthday}", align="left")
        self.show.display("Doublon détecté", self.content, "left")
        update_choice = input("Souhaitez-vous mettre à jour le joueur (y/n) ?")
        return update_choice

    def for_main_menu_choice(self, have_tournament, have_an_unfinished_tournament):
        self.show.main_menu(have_tournament, have_an_unfinished_tournament)
        user_choice = input('Que souhaitez-vous faire ? ')
        return user_choice

    def for_tournament_list(self):
        tournament_choice = input('Quel tournoi reprendre ? ')
        return tournament_choice

    def for_tournament_management_choice(self, tournaments_list):
        self.show.tournaments_list(tournaments_list)
        tournament_choice = input("Quel tournoi souhaitez-vous mettre à jour ? ")
        return tournament_choice

    def for_reports_menu_choice(self):
        self.show.reports_menu()
        user_choice = input("Quel rapport souhaitez-vous ? ")
        return user_choice

    def for_tournament_reports_menu(self):
        self.show.tournament_reports_menu()
        user_choice = input("Que souhaitez-vous voir ? ")
        return user_choice
