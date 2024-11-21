class Controller:
    def __init__(self, view):
        self.view = view

    def run(self):
        pass

    def start_tournament(self):
        pass

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

    def menu(self):
        choix_user = self.view.main_menu()
        print(choix_user)
