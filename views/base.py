from views.menus import Menus
from constante.constante import Constante


class View:
    def __init__(self):
        self.const = Constante()
        self.menu_view = Menus()

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

    def prompt_menu(self, menu_choice, list_to_show=[]):
        if menu_choice == self.const.MAIN:
            self.menu_view.main_menu()
            user_choice = input("Quel est votre choix ? ")
            if user_choice == "1":
                return self.const.START_TOURNAMENT
            elif user_choice == "2":
                return self.const.RESUME_TOURNAMENT
            elif user_choice == "3":
                return self.const.LIST_TOURNAMENTS
            elif user_choice == "4":
                return self.const.LIST_PLAYERS
            elif user_choice == "5":
                return self.const.QUIT
            else:
                return None
        elif menu_choice == self.const.RESUME_TOURNAMENT:
            self.menu_view.list_tournaments_menu(list_to_show)
            tournament_choice = input("Quel tournoi reprendre ?")
            return tournament_choice
