import os
import constant.constant as CONST
from models.player import Player


class Show:
    def decoration(function):
        "Contour decoration"

        def text_decorated(*args, **kwargs):
            print(CONST.STARS_LINE_FULL)
            print(CONST.STARS_LINE)
            function(*args, **kwargs)
            print(CONST.STARS_LINE)
            print(CONST.STARS_LINE_FULL)
            print()

        return text_decorated

    def clear_screen(self):
        "Clean the console for all os"
        command = "clear"
        if os.name in ("nt", "dos"):
            command = "cls"
        os.system(command)

    def display(self, title, content, align):
        """Manages the display on the console

        Args:
            title (str): Title to show
            content (list): List of the text to show
            align (str): Position of the content. Three possiblities left, center or right
        """
        self.clear_screen()
        self.head_menu()
        self.title_menu(title)
        self.show_content(content, align)

    @decoration
    def show_content(self, content, align):
        """Shows the content decorated

        Args:
            content (list): list of the content (str) to show
            align (str): Position of contents. Three possiblities left, center or right
        """
        if content:
            for text in content:
                self.decorated_text(text, align)

    @decoration
    def head_menu(self):
        "Shows the name of the program decorated"
        self.decorated_text("Gestionnaire de tournoi d'echecs")

    @decoration
    def title_menu(self, title):
        "Shows the title decorated"
        self.decorated_text(title)

    def decorated_text(self, text, align="center"):
        """Shows the text decorated

        Args:
            text (str): Text to show and decorate
            align (str): Position of contents. Three possiblities left, center or right. Default : center
        """
        if text == CONST.TOP_DECORATION:
            print(CONST.STARS_LINE_FULL)
            print(CONST.STARS_LINE)
        elif text == CONST.BOTTOM_DECORATION:
            print(CONST.STARS_LINE)
            print(CONST.STARS_LINE_FULL)
        elif text == CONST.STARS_LINE_FULL:
            print(CONST.STARS_LINE_FULL)
        else:
            spaces_needed = CONST.FRAME_LENGHT - 2 * CONST.NUMBER_SIDE_STARS - len(text)
            match align:
                case "left":
                    spaces_left = CONST.SPACE_REQUIRED
                    spaces_right = spaces_needed - spaces_left
                case "right":
                    spaces_right = CONST.SPACE_REQUIRED
                    spaces_left = spaces_needed - spaces_right
                case "center":
                    spaces_left = int(spaces_needed / 2)
                    spaces_right = int(spaces_needed / 2)
                    if spaces_needed % 2 == 1:
                        spaces_right = spaces_right + 1
                case _:
                    spaces_left = CONST.SPACE_REQUIRED
                    spaces_right = CONST.SPACE_REQUIRED
            print(
                f"{'*'*CONST.NUMBER_SIDE_STARS}"
                f"{' '*spaces_left}{text}"
                f"{' '*spaces_right}"
                f"{'*'*CONST.NUMBER_SIDE_STARS}"
            )

    def wait(self):
        "SHow a waiting line if a pause is needed"
        input("Appuyer sur une touche pour continuer...")

    def tournament_name(self, tournament_name=None):
        """Shows the tournament's name

        Args:
            tournament_name (str): Name of the tournament. Needed for change view
        """
        content = []
        if tournament_name:
            content.append(f"Nom actuel : {tournament_name}")
            content.append("Appuyer sur entrée pour ne pas modifier")
            self.display("Mise à jour d'un tournoi", content, "center")
        else:
            content.append("Nom du tournoi")
            content.append("Appuyer sur entrée pour annuler")
            self.display("Création d'un tournoi", content, "center")

    def tournament_place(self, tournament_place=None):
        """Shows the tournament's place

        Args:
            tournament_place (str): Place of the tournament. Needed for change view
        """
        if tournament_place:
            content = []
            content.append(f"Emplacement actuel : {tournament_place}")
            content.append("Appuyer sur entrée pour ne pas modifier")
            self.display("Mise à jour d'un tournoi", content, "center")
        else:
            self.display("Création d'un tournoi", ["Emplacement du tournoi"], "center")

    def tournament_description(self, tournament_description=None):
        """Shows the tournament's description

        Args:
            tournament_description (str): Description of the tournament. Needed for change view
        """
        if tournament_description:
            content = []
            content.append(f"Emplacement actuel : {tournament_description}")
            content.append("Appuyer sur entrée pour ne pas modifier")
            self.display("Mise à jour d'un tournoi", content, "center")
        else:
            self.display("Création d'un tournoi", ["Description du tournoi"], "center")

    def player_name(self, player_name=None):
        """Shows the player's name

        Args:
            player_name (str): Name of the player. Needed for change view
        """
        if player_name:
            content = []
            content.append(f"Prénom actuel : {player_name}")
            content.append("Appuyer sur entrée pour ne pas modifier")
            self.display("Mise à jour du joueur", content, "center")
        else:
            self.display("Nouveau joueur", ["Prénom du joueur"], "center")

    def player_surname(self, player_name, player_surname=None):
        """Shows the player's surname

        Args:
            player_name (str): Name of the player
            player_surname (str): Surname of the player. Needed for change view
        """
        if player_surname:
            content = []
            content.append(f"Nom actuel de {player_name} : {player_surname}")
            content.append("Appuyer sur entrée pour ne pas modifier")
            self.display("Mise à jour du joueur", content, "center")
        else:
            self.display("Nouveau joueur", [f"Nom de {player_name}"], "center")

    def player_birthday(self, player_name, player_surname, player_birthday=None):
        """Shows the player's birthday

        Args:
            player_name (str): Name of the player
            player_surname (str): Surname of the player
            player_birthday (str): Birthday of the player. Needed for change view
        """
        if player_birthday:
            content = []
            content.append(f"Date d'anniversaire actuelle : {player_birthday}")
            content.append("Appuyer sur entrée pour ne pas modifier")
            self.display("Mise à jour du joueur", content, "center")
        else:
            self.display(
                "Nouveau joueur",
                [
                    f"Date de naissance de {
                         player_surname} {player_name}"
                ],
                "center",
            )

    def player_chess_id(self, player_name, player_surname, player_chess_id):
        """Shows the player's chess id

        Args:
            player_name (str): Name of the player
            player_surname (str): Surname of the player
            player_chess_id (str): Chess id of the player. Needed for change view
        """
        if player_chess_id:
            content = []
            content.append(f"Date d'anniversaire actuelle : {player_chess_id}")
            content.append("Appuyer sur entrée pour ne pas modifier")
            self.display("Mise à jour du joueur", content, "center")
        else:
            self.display(
                "Nouveau joueur",
                [f"Identifiant international de {player_surname} {player_name}"],
                "center",
            )

    def main_menu(self, have_tournament, have_an_unfinished_tournament, have_player):
        """Shows the main menu

        Args:
            have_tournament (boo): True if at least one tournament is registered
            have_an_unfinished_tournament (bool) : True if at least one tournament is unfinished
            have_player (bool): True if at least one player is registered
        """
        content = []
        content.append("1- Nouveau tournoi")
        if have_tournament and have_an_unfinished_tournament:
            content.append("2- Reprendre un tournoi")
        else:
            content.append("2- Pas de tournoi en cours")
        if have_tournament:
            content.append("3- Mise à jour des tournois")
        else:
            content.append("3- Pas de tournoi enregistré")
        if have_player:
            content.append("4- Mise à jour des joueurs")
        else:
            content.append("4- Pas de joueur enregistré")
        content.append("5- Rapports")
        content.append("0- Quitter")
        self.display("Menu principal", content, "left")

    def ranking(self, players_list):
        """Shows the ranking of all players

        Args:
            players_list (list): List of the players's object
        """
        content = []
        for player in players_list:
            position_in_list = players_list.index(player) + 1
            zero = ""
            if position_in_list < 10:
                zero = "0"
            content.append(
                f"{zero}{position_in_list} - "
                f"{player.surname} "
                f"{player.name} "
                f"({player.chess_id}) : "
                f"{player.score}"
            )
        self.display("Classement provisoire", content, "left")

    def tournament_information(self, tournament):
        """Shows the tournament information

        Args:
            tournament (object): Tournament you want to know information
        """
        content = []
        content.append(f" Nom : {tournament.name}")
        content.append(f" Emplacement : {tournament.place}")
        content.append(f" description : {tournament.description}")
        content.append(f" Nombre de tours : {tournament.number_of_rounds()}")
        content.append(f" Tour effectué : {tournament.round_number}")
        content.append(f" Nombre de joueurs : {len(tournament.players_list)}")
        for player in tournament.players_list:
            if player:
                content.append(f" - {player.surname} {player.name}")
            else:
                content.append(" - Non défini")
        self.display("Information sur le tournoi", content, "left")

    def reports_menu(self):
        "Shows the menu for reports"
        content = []
        content.append("1- Liste des joueurs par ordre alphabétique")
        content.append("2- Liste des tournois")
        content.append("3- Informations sur un tournoi")
        content.append("0- Retour")
        self.display("Rapports", content, "left")

    def tournament_reports_menu(self, tournament):
        """Shows the reports menu for a tournament choiced

        Args:
            tournament (object): Tournament you want to know information
        """
        content = []
        content.append(f"Nom du tournoi :         {tournament.name}")
        content.append(f"Emplacement du tournoi : {tournament.place}")
        content.append(f"Description du tournoi : {tournament.description}")
        content.append(
            f"Nombre de joueurs :      {
                       len(tournament.players_list)}"
        )
        content.append(f"Date de début :          {tournament.date_start}")
        if tournament.is_finished():
            content.append(f"Date de fin :            {tournament.date_end}")
        else:
            content.append("Date de fin :            tournoi non terminé")
        content.append("")
        content.append(CONST.STARS_LINE_FULL)
        content.append("")
        content.append("1- Liste des joueurs")
        content.append("2- Déroulement du tournoi")
        content.append("0- Retour")
        self.display("Information sur le tournoi", content, "left")

    def matches_list(self, round_number, matches_list):
        """Shows the list of matches of one round

        Args:
            round_number (int): Number of the round in progress
            matches_list (list): List of tound's matches
        """
        content = []
        for match in matches_list:
            content.append("  Match :")
            content.append(
                f"   - {match.white_player["player"].surname} "
                f"{match.white_player["player"].name} "
                f"({match.white_player["player"].chess_id}) : "
                f"{match.white_player["player"].score} pt"
            )
            content.append(
                f"   - {match.black_player["player"].surname} "
                f"{match.black_player["player"].name} "
                f"({match.black_player["player"].chess_id}) : "
                f"{match.black_player["player"].score} pt"
            )
            if matches_list.index(match) != (len(matches_list) - 1):
                content.append(" ")
        self.display(
            f"Voici les matchs du Round {
                     round_number}",
            content,
            "left",
        )

    def players(self, players_list, sort=False, new_player_possible=True):
        """Shows all the players in a list. Can be sort. Cancel proposal view is optional

        Args:
            players_list (list): List of players
            sort (bool): True if you wish to sort the list of players alphabetically
            new_player_possible (bool): True if you wish to show the cancel proposal
        """
        players_to_show = []
        for player in players_list:
            if isinstance(player, Player):
                players_to_show.append(player)
        if sort:
            players_to_show = sorted(players_to_show, key=lambda player: player.name)
            players_to_show = sorted(players_to_show, key=lambda player: player.surname)
        content = []
        for player in players_to_show:
            position_in_list = players_to_show.index(player) + 1
            zero = ""
            if position_in_list < 10:
                zero = "0"
            content.append(
                f"{zero}{position_in_list} - {player.surname} {player.name} ({player.chess_id})"
            )
        for i in range(len(players_to_show), len(players_list)):
            content.append("-- - Joueur non renseigné")
        if new_player_possible:
            content.append(" ")
            content.append("00 - Nouveau joueur")
        self.display("Liste des joueurs", content, "left")

    def match_result(self, match):
        """Shows a match for result request

        Args:
            match (object): Match you want to see
        """
        content = []
        content.append(
            f"    1 - {match.white_player["player"].surname} "
            f"{match.white_player["player"].name} "
            f"({match.white_player["player"].chess_id})"
        )
        content.append(
            f"    2 - {match.black_player["player"].surname} "
            f"{match.black_player["player"].name} "
            f"({match.black_player["player"].chess_id})"
        )
        content.append("    0 - Match nul")
        self.display("Résultat du match", content, "left")

    def tournaments_list(self, tournaments_list, cancel=True):
        """Shows the list of tournaments. Optional cancel proposal view

        Args:
            tournaments_list (list): List of tournaments
            cancel (bool): True if you wish to see the cancel proposal
        """
        content = []
        for tournament in tournaments_list:
            position_in_list = tournaments_list.index(tournament) + 1
            zero = ""
            if position_in_list < 10:
                zero = "0"
            content.append(f"{zero}{position_in_list} - " f"{tournament.name}")
        if cancel:
            content.append(" ")
            content.append("0 - Annuler")
        self.display("Liste des tournois", content, "left")

    def rounds_list(self, rounds_list):
        """Shows the list of rounds

        Args:
            rounds_list (list): List of rounds
        """
        content = []
        for round in rounds_list:
            content.append(f"Round {rounds_list.index(round) + 1} :")
            if round.is_finished():
                for match in round.matches_list:
                    content.append("   Match :")
                    content.append(
                        f"      - {match.white_player["player"].surname} "
                        f"{match.white_player["player"].name} "
                        f"- {match.white_player["score"]}pt"
                    )
                    content.append(
                        f"      - {match.black_player["player"].surname} "
                        f"{match.black_player["player"].name} "
                        f"- {match.black_player["score"]}pt"
                    )
            else:
                content.append("    Non joué")
            if rounds_list.index(round) != (len(rounds_list) - 1):
                content.append("")
        self.display("Rounds du tournoi", content, "left")

    def end_tournament(self, players_list):
        """Shows the final classment of the tournament

        Args:
            players_list (list): List of players in the tournament
        """
        content = []
        for player in players_list:
            s = ""
            if player.score > 1:
                s = "s"
            content.append(
                f"{players_list.index(player) + 1} - "
                f"{player.surname} "
                f"{player.name} "
                f"({player.chess_id}) "
                f"avec {player.score} pt{s}"
            )

        self.display("Classement final", content, "left")

    def message(self, title, message):
        """Shows a message. message must be a string, not a list

        Args:
            title (str): Title of the message
            message (str): Message you want to be show
        """
        content = [message]
        self.display(title, content, "center")
        self.wait()
