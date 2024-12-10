import os
import constant.constant as CONST


class Show:
    def decoration(function):
        def text_decorated(*args, **kwargs):
            print(CONST.STARS_LINE_FULL)
            print(CONST.STARS_LINE)
            function(*args, **kwargs)
            print(CONST.STARS_LINE)
            print(CONST.STARS_LINE_FULL)
            print()
        return text_decorated

    def clear_screen(self):
        """
        Clean the console for all os
        """
        command = 'clear'
        if os.name in ('nt', 'dos'):
            command = 'cls'
        os.system(command)

    def display(self, title, content, align):
        self.clear_screen()
        self.head_menu()
        self.title_menu(title)
        self.show_content(content, align)

    @decoration
    def show_content(self, content_table, align):
        if content_table:
            for content in content_table:
                self.decorated_text(content, align)

    @decoration
    def head_menu(self):
        self.decorated_text("Gestionnaire de tournoi d'echecs")

    @decoration
    def title_menu(self, title):
        self.decorated_text(title)

    def decorated_text(self, text='', align="center"):
        if text == CONST.TOP_DECORATION:
            print(CONST.STARS_LINE_FULL)
            print(CONST.STARS_LINE)
        elif text == CONST.BOTTOM_DECORATION:
            print(CONST.STARS_LINE)
            print(CONST.STARS_LINE_FULL)
        elif text == CONST.STARS_LINE_FULL:
            print(CONST.STARS_LINE_FULL)
        else:
            spaces_needed = CONST.FRAME_LENGHT - 2*CONST.NUMBER_SIDE_STARS - len(text)
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
            print(f"{'*'*CONST.NUMBER_SIDE_STARS}"
                  f"{' '*spaces_left}{text}"
                  f"{' '*spaces_right}"
                  f"{'*'*CONST.NUMBER_SIDE_STARS}")

    def wait(self):
        input('Appuyer sur une touche pour continuer...')

    def tournament_name(self, tournament_name):
        content = []
        if not tournament_name:
            content.append("Nom du tournoi")
            content.append("Appuyer sur entrée pour annuler")
            self.display("Création d'un tournoi", content, "center")
        else:
            content.append(f"Nom actuel : {tournament_name}")
            content.append("Appuyer sur entrée pour ne pas modifier")
            self.display("Mise à jour d'un tournoi", content, "center")

    def tournament_place(self, tournament_place):
        if not tournament_place:
            self.display("Création d'un tournoi", ["Emplacement du tournoi"], "center")
        else:
            content = []
            content.append(f"Emplacement actuel : {tournament_place}")
            content.append("Appuyer sur entrée pour ne pas modifier")
            self.display("Mise à jour d'un tournoi", content, "center")

    def tournament_description(self, tournament_description):
        if not tournament_description:
            self.display("Création d'un tournoi", ["Description du tournoi"], "center")
        else:
            content = []
            content.append(f"Emplacement actuel : {tournament_description}")
            content.append("Appuyer sur entrée pour ne pas modifier")
            self.display("Mise à jour d'un tournoi", content, "center")

    def player_name(self, player_name):
        if not player_name:
            self.display("Nouveau joueur", ["Prénom du joueur"], "center")
        else:
            content = []
            content.append(f"Prénom actuel : {player_name}")
            content.append("Appuyer sur entrée pour ne pas modifier")
            self.display("Mise à jour du joueur", content, "center")

    def player_surname(self, player_name, player_surname):
        if not player_surname:
            self.display("Nouveau joueur", [f"Nom de {player_name}"], "center")
        else:
            content = []
            content.append(f"Nom actuel : {player_surname}")
            content.append("Appuyer sur entrée pour ne pas modifier")
            self.display("Mise à jour du joueur", content, "center")

    def player_birthday(self, player_name, player_surname, player_birthday):
        if not player_birthday:
            self.display("Nouveau joueur", [f"Date de naissance de {player_surname} {player_name}"], "center")
        else:
            content = []
            content.append(f"Date d'anniversaire actuelle : {player_birthday}")
            content.append("Appuyer sur entrée pour ne pas modifier")
            self.display("Mise à jour du joueur", content, "center")

    def player_chess_id(self, player_name, player_surname, player_chess_id):
        if not player_chess_id:
            self.display("Nouveau joueur", [f"Identifiant international de {player_surname} {player_name}"],
                         "center")
        else:
            content = []
            content.append(f"Date d'anniversaire actuelle : {player_chess_id}")
            content.append("Appuyer sur entrée pour ne pas modifier")
            self.display("Mise à jour du joueur", content, "center")

    def main_menu(self, have_tournament, have_an_unfinished_tournament):
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
        content.append("4- Mise à jour des joueurs")
        content.append("5- Rapports")
        content.append("0- Quitter")
        self.display("Menu principal", content, "left")

    def ranking(self, players_list):
        content = []
        for player in players_list:
            position_in_list = players_list.index(player) + 1
            zero = ""
            if position_in_list < 10:
                zero = "0"
            content.append(f"{zero}{position_in_list} - "
                           f"{player.surname} "
                           f"{player.name} "
                           f"({player.chess_id}) : "
                           f"{player.score}")
        self.display("Classement provisoire", content, "left")

    def tournament_information(self, tournament):
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
        content = []
        content.append("1- Liste des joueurs par ordre alphabétique")
        content.append("2- Liste des tournois")
        content.append("3- Informations sur un tournoi")
        content.append("0- Retour")
        self.display("Rapports", content, "left")

    def tournament_reports_menu(self, tournament):
        content = []
        content.append(f"Nom du tournoi :         {tournament.name}")
        content.append(f"Emplacement du tournoi : {tournament.place}")
        content.append(f"Description du tournoi : {tournament.description}")
        content.append(f"Nombre de joueurs :      {len(tournament.players_list)}")
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
        content = []
        for match in matches_list:
            content.append("  Match :")
            content.append(f"   - {match.white_player["player"].surname} "
                           f"{match.white_player["player"].name} "
                           f"({match.white_player["player"].chess_id}) : "
                           f"{match.white_player["player"].score} pt")
            content.append(f"   - {match.black_player["player"].surname} "
                           f"{match.black_player["player"].name} "
                           f"({match.black_player["player"].chess_id}) : "
                           f"{match.black_player["player"].score} pt")
            if matches_list.index(match) != (len(matches_list) - 1):
                content.append(" ")
        self.display(f"Voici les matchs du Round {round_number}", content, "left")

    def players(self, players_list, sort=False, new_player_possible=True):
        if sort:
            players_list = sorted(players_list, key=lambda player: player.name)
            players_list = sorted(players_list, key=lambda player: player.surname)
        content = []
        for player in players_list:
            position_in_list = players_list.index(player) + 1
            zero = ""
            if position_in_list < 10:
                zero = "0"
            content.append(f"{zero}{position_in_list} - {player.surname} {player.name} ({player.chess_id})")
        if new_player_possible:
            content.append(" ")
            content.append("00 - Nouveau joueur")
        self.display("Liste des joueurs", content, "left")

    def match_result(self, match):
        content = []
        content.append(f"    1 - {match.white_player["player"].surname} "
                       f"{match.white_player["player"].name} "
                       f"({match.white_player["player"].chess_id})")
        content.append(f"    2 - {match.black_player["player"].surname} "
                       f"{match.black_player["player"].name} "
                       f"({match.black_player["player"].chess_id})")
        content.append("    0 - Match nul")
        self.display("Résultat du match", content, "left")
        winner_player = input("Qui est le vainqueur ? ")
        return winner_player

    def tournaments_list(self, tournaments_list, cancel_possible=True):
        content = []
        for tournament in tournaments_list:
            position_in_list = tournaments_list.index(tournament) + 1
            zero = ""
            if position_in_list < 10:
                zero = "0"
            content.append(f"{zero}{position_in_list} - "
                           f"{tournament.name}")
        if cancel_possible:
            content.append(" ")
            content.append("0 - Annuler")
        self.display("Liste des tournois", content, "left")

    def rounds_list(self, rounds_list):
        content = []
        for round in rounds_list:
            content.append(f"Round {rounds_list.index(round) + 1} :")
            if round.is_finished():
                for match in round.matches_list:
                    content.append("   Match :")
                    content.append(f"      - {match.white_player["player"].surname} "
                                   f"{match.white_player["player"].name} "
                                   f"- {match.white_player["score"]}pt")
                    content.append(f"      - {match.black_player["player"].surname} "
                                   f"{match.black_player["player"].name} "
                                   f"- {match.black_player["score"]}pt")
            else:
                content.append("    Non joué")
            if rounds_list.index(round) != (len(rounds_list) - 1):
                content.append("")
        self.display("Rounds du tournoi", content, "left")

    def end_tournament(self, players_list):
        content = []
        for player in players_list:
            s = ""
            if player.score > 1:
                s = "s"
            content.append(f"{players_list.index(player) + 1} - "
                           f"{player.surname} "
                           f"{player.name} "
                           f"({player.chess_id}) "
                           f"avec {player.score} pt{s}")

        self.display("Classement final", content, "left")

    def message(self, title, message):
        content = [message]
        self.display(title, content, "center")
        self.wait()
