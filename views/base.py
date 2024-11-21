import os
from views.menus import Menus
from constante.constante import Constante


class View:
    def __init__(self):
        self.const = Constante()
        self.menu_view = Menus()

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

        print("******************************\n"
              "* Bienvenue sur le           *\n"
              "*      gestionnaire de       *\n"
              "*           tournoi d'echecs *\n"
              "******************************\n"
              "                              \n"
              "******************************\n"
              f"*{" "*spaces_needed_left}{menu_title}{" "*spaces_needed_right}*\n"
              "******************************\n")

    def prompt_for_tournament_name(self):
        pass

    def prompt_for_tournament_place(self):
        pass

    def prompt_for_tournament_number_of_rounds(self):
        pass

    def prompt_for_new_player(self):
        pass

    def prompt_for_tournament_description(self):
        pass

    def prompt_for_tournament_new_tournament(self):
        pass

    def prompt_menu(self, menu_choice):
        self.clear_screen()
        if menu_choice == self.const.MAIN:
            self.headset_menu("Menu principal")
            user_choice = self.menu_view.main_menu()
        elif menu_choice == self.const.RESUME_TOURNAMENT:
            user_choice = 1
        return user_choice

    def prompt_for_list_tournaments(self, list_tournaments):
        self.clear_screen()
        self.headset_menu("Liste des tournois")
        for tournament in list_tournaments:
            print(f"*{tournament}*\n")
        print("*                            *\n"
              "******************************\n")
        tournament_choice = input("Quel tournoi reprendre ?")
        return tournament_choice
