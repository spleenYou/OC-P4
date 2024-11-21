from constante.constante import Constante


class Menus:
    def __init__(self):
        self.const = Constante()

    def main_menu(self):
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
