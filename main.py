import os
import constant.constant as CONST
from controllers.base import Controller
from views import base as views


def main():
    game = Controller(views)
    user_menu_choice = None
    tournament_choiced = None
    while user_menu_choice is None:
        have_tournament = False
        have_an_unfinished_tournament = False
        if game.tournaments_list != []:
            have_tournament = True
        for tournament in game.tournaments_list:
            if not tournament.is_finished():
                have_an_unfinished_tournament = True
        user_menu_choice = game.main_menu(have_tournament, have_an_unfinished_tournament)
        if user_menu_choice == CONST.CREATE_TOURNAMENT:
            tournament_choiced = game.create_tournament()
        elif user_menu_choice == CONST.RESUME_TOURNAMENT and have_an_unfinished_tournament:
            tournament_choiced = game.choice_tournament()
        elif user_menu_choice == CONST.TOURNAMENTS_UPDATES and have_tournament:
            game.tournaments_updates()
        elif user_menu_choice == CONST.PLAYERS_UPDATES:
            print("players")
        elif user_menu_choice == CONST.QUIT:
            print('Au revoir !')
            os._exit(os.EX_OK)
        else:
            user_menu_choice = None

        if tournament_choiced:
            user_menu_choice = game.run_tournament(tournament_choiced)
        else:
            user_menu_choice = None


if __name__ == "__main__":
    main()
