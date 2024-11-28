import os
import constant.constant as CONST


class Menus:
    def decoration(function):
        def text_decorated(*args, **kwargs):
            print(CONST.STARS_LINE_FULL)
            print(CONST.STARS_LINE)
            function(*args)
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

    def view_menu(self, title, menu, thing_to_show=None):
        self.clear_screen()
        self.head_menu()
        self.title_menu(title)
        match menu:
            case CONST.MAIN:
                self.main_menu()
            case CONST.MENU_LIST_TOURNAMENTS:
                self.list_tournaments_menu(thing_to_show)
            case CONST.SHOW_TOURNAMENT_INFORMATIONS:
                self.show_tournament_information(thing_to_show)
            case _:
                pass

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
        self.decorated_text("Bienvenue sur le", align="left")
        self.decorated_text("gestionnaire de")
        self.decorated_text("tournoi d'echecs", align="right")

    @decoration
    def main_menu(self):
        self.decorated_text("1- Nouveau tournoi", align="left")
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
            tournament_view = f'{tounaments_list.index(tournament)} - {tournament.name}'
            self.decorated_text(tournament_view)

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
                    spaces_left = 1
                    spaces_right = spaces_needed - spaces_left
                case "right":
                    spaces_right = 1
                    spaces_left = spaces_needed - spaces_right
                case "center":
                    spaces_left = int(spaces_needed / 2)
                    spaces_right = int(spaces_needed / 2)
                    if spaces_needed % 2 == 1:
                        spaces_right = spaces_right + 1
                case _:
                    spaces_left = 1
                    spaces_right = 1
            print(f"{'*'*CONST.NUMBER_SIDE_STARS}"
                  f"{' '*spaces_left}{text}"
                  f"{' '*spaces_right}"
                  f"{'*'*CONST.NUMBER_SIDE_STARS}")
