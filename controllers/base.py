from constante.constante import Constante


class Controller:
    def __init__(self, view):
        self.view = view
        self.const = Constante()

    def run(self):
        pass

    def start_tournament(self):
        print("début du tournoi")

    def list_tournaments(self):
        return ["tournoi"]  # à refaire

    def resume_tournament(self, tournament):
        print("Résumé du tournoi")

    def end_tournament(self):
        pass

    def start_round(self):
        pass

    def end_turn(self):
        pass

    def start_match(self, players):
        pass

    def end_match(self, players):
        pass

    def get_player(self):
        pass

    def main_menu(self):
        user_menu_choice = None
        while not user_menu_choice:
            user_menu_choice = self.view.prompt_menu(self.const.MAIN)
            if user_menu_choice == self.const.START_TOURNAMENT:
                self.start_tournament()
            elif user_menu_choice == self.const.RESUME_TOURNAMENT:
                list_tournaments = self.list_tournaments()
                tournaments_number = len(list_tournaments)
                tournament_choice = self.view.prompt_menu(self.const.RESUME_TOURNAMENT, list_tournaments)
                if int(tournament_choice) == 0 or int(tournament_choice) > tournaments_number:
                    user_menu_choice = None
                else:
                    self.resume_tournament(tournament_choice)
            elif user_menu_choice == self.const.LIST_TOURNAMENTS:
                print("liste")
            elif user_menu_choice == self.const.LIST_PLAYERS:
                print("players")
            elif user_menu_choice == self.const.QUIT:
                print('Au revoir !')
                break
            else:
                user_menu_choice = None
