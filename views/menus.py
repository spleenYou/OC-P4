import os
import constant.constant as CONST


class Menus:
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

    def view_menu(self, title, view='', thing_to_show=None):
        self.clear_screen()
        self.head_menu()
        self.title_menu(title)
        match view:
            case CONST.MAIN:
                self.main_menu(thing_to_show)
            case CONST.MENU_LIST_TOURNAMENTS:
                self.list_tournaments_menu(thing_to_show)
            case CONST.SHOW_TOURNAMENT_INFORMATIONS:
                self.show_tournament_information(thing_to_show)
            case CONST.MENU_PLAYER_CHOICE:
                self.show_player_choice(thing_to_show)
            case CONST.UPDATE_PLAYER_CHOICE:
                self.show_players_with_same_chess_id(thing_to_show)
            case CONST.MESSAGE:
                self.show_message(thing_to_show)
            case _:
                pass

    @decoration
    def show_message(self, thing_to_show):
        self.decorated_text(thing_to_show)

    @decoration
    def show_players_with_same_chess_id(self, players_data):
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

    @decoration
    def show_player_choice(self, players_list):
        for player in players_list:
            text = f"{players_list.index(player) + 1} - {player.surname} {player.name} ({player.chess_id})"
            self.decorated_text(text, align="left")
        self.decorated_text(text="0 - Nouveau joueur", align="left")

    @decoration
    def show_tournament_information(self, tournament):
        self.decorated_text(f" Nom : {tournament.name}", align="left")
        self.decorated_text(f" Emplacement : {tournament.place}", align="left")
        self.decorated_text(f" description : {tournament.description}", align="left")
        self.decorated_text(f" Nombre de tours : {tournament.number_of_rounds}", align="left")
        self.decorated_text(f" Tour effectué : {tournament.round_number}", align="left")
        self.decorated_text(f" Nombre de joueurs : {len(tournament.players_list)}", align="left")
        for player in tournament.players_list:
            if player:
                self.decorated_text(f" - {player.surname} {player.name}", align="left")
            else:
                self.decorated_text(" - Non défini", align="left")

    @decoration
    def head_menu(self):
        self.decorated_text("Gestionnaire de tournoi d'echecs")

    @decoration
    def main_menu(self, first_time):
        self.decorated_text("1- Nouveau tournoi", align="left")
        if first_time:
            self.decorated_text("Pas de tournoi enregistré", align="left")
        else:
            self.decorated_text("2- Reprendre un tournoi", align="left")
        self.decorated_text("3- Liste des tournois", align="left")
        self.decorated_text("4- Liste des joueurs", align="left")
        self.decorated_text("0- Quitter", align="left")

    @decoration
    def title_menu(self, title):
        self.decorated_text(title)

    @decoration
    def list_tournaments_menu(self, tounaments_list):
        for tournament in tounaments_list:
            tournament_view = f'{tounaments_list.index(tournament) + 1} - {tournament.name}'
            self.decorated_text(tournament_view, align="left")
        self.decorated_text("0 - Annuler", align="left")

    def decorated_text(self, text='', align="center"):
        if text == CONST.TOP_DECORATION:
            print(CONST.STARS_LINE_FULL)
            print(CONST.STARS_LINE)
            pass
        elif text == CONST.BOTTOM_DECORATION:
            print(CONST.STARS_LINE)
            print(CONST.STARS_LINE_FULL)
            pass
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
