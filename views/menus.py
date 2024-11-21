import os
from constante.constante import Constante


class Menus:
    def __init__(self):
        self.const = Constante()

    def clear_screen(self):
        """
        Clean the console for all os
        """
        command = 'clear'
        if os.name in ('nt', 'dos'):
            command = 'cls'
        os.system(command)

    def headset_menu(self, menu_title):
        spaces_needed = 28 - len(menu_title)
        spaces_needed_left = int(spaces_needed / 2)
        spaces_needed_right = int(spaces_needed / 2)

        if spaces_needed % 2:
            spaces_needed_right = spaces_needed_right + 1
            print(spaces_needed)
        self.clear_screen()
        print("******************************\n"
              "* Bienvenue sur le           *\n"
              "*      gestionnaire de       *\n"
              "*           tournoi d'echecs *\n"
              "******************************\n"
              "                              \n"
              "******************************\n"
              f"*{" "*spaces_needed_left}{menu_title}{" "*spaces_needed_right}*\n"
              "******************************\n")

    def main_menu(self):
        self.headset_menu("Menu principal")
        print("******************************\n"
              "*                            *\n"
              "* Que souhaitez-vous faire ? *\n"
              "*                            *\n"
              "*   1- Nouveau tournoi       *\n"
              "*   2- Reprendre un tournoi  *\n"
              "*   3- Liste des tournois    *\n"
              "*   4- Liste des joueurs     *\n"
              "*   5- Quitter               *\n"
              "*                            *\n"
              "******************************\n")

    def list_tournaments_menu(self, list_tournaments):
        self.headset_menu("Liste des tournois")
        for tournament in list_tournaments:
            print(f"*{tournament}*\n")
        print("*                            *\n"
              "******************************\n")
