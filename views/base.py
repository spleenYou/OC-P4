import os


class View:
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

    def clear_screen(self):
        command = 'clear'
        if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
            command = 'cls'
        os.system(command)

    def main_menu(self):
        self.clear_screen()
        print("******************************\n"
              "* Bienvenue sur le           *\n"
              "*      gestionnaire de       *\n"
              "*           tournoi d'echecs *\n"
              "******************************\n"
              "                              \n"
              "******************************\n"
              "*       Menu principal       *\n"
              "******************************\n"
              "                              \n"
              "******************************\n"
              "*                            *\n"
              "* Que souhaitez-vous faire ? *\n"
              "*                            *\n"
              "*   1- Démarrer un tournoi   *\n"
              "*   2- Reprendre un tournoi  *\n"
              "*   3- Liste des tournois    *\n"
              "*   4- Liste des joueurs     *\n"
              "*                            *\n"
              "******************************\n"
              "                              \n")
        choix_utilisateur = input("")
        return choix_utilisateur
