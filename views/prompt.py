from views.show import Show


class Prompt:
    "Manage the prompts"
    def __init__(self):
        self.show = Show()

    def for_tournament_name(self, tournament_name=None):
        """Prompt for the tournament's name

        Args:
            tournament_name (str): Tournament's name, needed if you want to see the change view

        Returns:
            tournament_name (str)
        """
        self.show.tournament_name(tournament_name)
        tournament_name = input("Quel est le nouveau nom du tournoi ? ")
        return tournament_name

    def for_tournament_place(self, tournament_place=None):
        """Prompt for the tournament's place

        Args:
            tournament_place (str): Tournament's place, needed if you want to see the change view

        Returns:
            tournament_place (str)
        """
        self.show.tournament_place(tournament_place)
        tournament_place = input("Où se trouve le tournoi ? ")
        return tournament_place

    def for_tournament_number_of_rounds(self):
        """Prompt for tournament's the number of rounds

        Returns:
            number_of_rounds (str)
        """
        self.show.display("Création d'un tournoi", ["Nombre de tours"], "center")
        number_of_rounds = input("Combien de tours comprend le tournoi ? ")
        return number_of_rounds

    def for_tournament_number_players(self):
        """Prompt for the tournament's place

        Returns:
            number_players (str)
        """
        self.show.display("Création d'un tournoi", ["Nombre de joueurs"], "center")
        number_players = input("Combien de joueurs participent au tournoi ? ")
        return number_players

    def for_tournament_description(self, tournament_description=None):
        """Prompt for the tournament's description

        Args:
            tournament_description (str): Tournament's description, needed if you want to see the change view

        Returns:
            tournament_description (str)
        """
        self.show.tournament_description(tournament_description)
        tournament_description = input("Veuillez entrer la description du tournoi : ")
        return tournament_description

    def for_player_name(self, player_name=None):
        """Prompt for the player's name

        Args:
            player_name (str): Player's name, needed if you want to see the change view

        Returns:
            player_name (str)
        """
        self.show.player_name(player_name)
        player_name = input("Quel est le prénom du joueur ? ").capitalize()
        return player_name

    def for_player_surname(self, player_name, player_surname=None):
        """Prompt for the player's surname

        Args:
            player_surname (str): Player's surname, needed if you want to see the change view

        Returns:
            player_surname (str)
        """
        self.show.player_surname(player_name, player_surname)
        player_surname = input(f"Quel est le nom de famille de {player_name} ? ").upper()
        return player_surname

    def for_player_birthday(self, player_name, player_surname, player_birthday=None):
        """Prompt for the player's birthday

        Args:
            player_name (str): Player's name you want the birthday
            player_surname (str): Player's surname you want the birthday
            player_birthday (str): Player's birthday, needed if you want to see the change view

        Returns:
            player_birthday (str)
        """
        self.show.player_birthday(player_name, player_surname, player_birthday)
        player_birthday = input(f"Quel est la date de naissance de {player_surname} {player_name} ? [DD-MM-YYYY] ")
        return player_birthday

    def for_player_chess_id(self, player_name, player_surname, player_chess_id=None):
        """Prompt for the player's chess id

        Args:
            player_name (str): Player's name you want the birthday
            player_surname (str): Player's surname you want the birthday
            player_chess_id (str): Player's chess id, needed if you want to see the change view

        Returns:
            player_chess_id (str)
        """
        self.show.player_chess_id(player_name, player_surname, player_chess_id)
        player_chess_id = input(f"Quel est l'identifiant de {player_surname} {player_name} ? ").upper()
        return player_chess_id

    def for_tournament_choice(self, tournaments_list, cancel_possible=True):
        """Prompt for the player's birthday

        Args:
            tournaments_list (list): List of the tournaments
            cancel_possible (bool): True if you want to see the cancel possibility, False if not

        Returns:
            tournament_choice (str)
        """
        self.show.tournaments_list(tournaments_list, cancel_possible)
        tournament_choice = input("Quel tournoi choisissez-vous ? ")
        return tournament_choice

    def for_player_choice(self, players_list):
        """Prompt for the player's birthday

        Args:
            player_list (list): List of the players

        Returns:
            add_player_choice (str)
        """
        self.show.players(players_list)
        add_player_choice = input("Quel joueur ajouter au tournoi ? ")
        return add_player_choice

    def for_main_menu_choice(self, have_tournament, have_an_unfinished_tournament, have_player):
        """Prompt for the menu choice

        Args:
            have_tournament (boo): True if at least one tournament is registered
            have_an_unfinished_tournament (bool) : True if at least one tournament is unfinished
            have_player (bool): True if at least one player is registered

        Returns:
            user_choice (str)
        """
        self.show.main_menu(have_tournament, have_an_unfinished_tournament, have_player)
        user_choice = input('Que souhaitez-vous faire ? ')
        return user_choice

    def for_tournament_management_choice(self, tournaments_list):
        """Prompt the tournament you want to change name or place or description

        Args:
            tounraments_list (list): List of the tournaments

        Returns:
            tournament_choiced (str)
        """
        self.show.tournaments_list(tournaments_list)
        tournament_choiced = input("Quel tournoi souhaitez-vous mettre à jour ? ")
        return tournament_choiced

    def for_reports_menu_choice(self):
        """Prompt the menu for reports choice

        Returns:
            report_choiced (str)
        """
        self.show.reports_menu()
        report_choiced = input("Quel rapport souhaitez-vous ? ")
        return report_choiced

    def for_tournament_reports_menu(self, tournament):
        """Prompt the tournament menu

        Args:
            tounrament (object): tournament you want to see report

        Returns:
            user_choice (str)
        """
        self.show.tournament_reports_menu(tournament)
        user_choice = input("Que souhaitez-vous voir ? ")
        return user_choice

    def for_match_result(self, match):
        """Prompt for the match result

        Args:
            match (object): Match you want to tell the result

        Returns:
            winner_player (str)
        """
        self.show.match_result(match)
        winner_player = input("Qui est le vainqueur ? ")
        return winner_player
