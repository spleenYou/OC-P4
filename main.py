import os
import constant.constant as CONST
from controllers.base import Controller
from views import prompt
from views import show


def main():
    "Main function for the chess tournaments program"
    game = Controller(prompt, show)
    if game.all_players_list is not None and game.tournaments_list is not None:
        user_menu_choice = None
    else:
        user_menu_choice = CONST.QUIT
    tournament_choiced = None
    while user_menu_choice is None:
        have_tournament = False
        have_an_unfinished_tournament = False
        have_player = False
        if game.tournaments_list is not None:
            if len(game.tournaments_list):
                have_tournament = True
        for tournament in game.tournaments_list:
            if not tournament.is_finished():
                have_an_unfinished_tournament = True
        if game.all_players_list is not None:
            if len(game.all_players_list):
                have_player = True
        user_menu_choice = game.main_menu(
            have_tournament, have_an_unfinished_tournament, have_player
        )
        if user_menu_choice == CONST.CREATE_TOURNAMENT:
            tournament_choiced = game.create_tournament()
        elif (
            user_menu_choice == CONST.RESUME_TOURNAMENT
            and have_an_unfinished_tournament
        ):
            tournament_choiced = game.choice_tournament()
        elif user_menu_choice == CONST.TOURNAMENTS_UPDATES and have_tournament:
            game.tournaments_updates_menu()
        elif user_menu_choice == CONST.PLAYERS_UPDATES:
            game.players_updates()
        elif user_menu_choice == CONST.REPORTS_MENU:
            game.reports_menu()
        elif user_menu_choice == CONST.QUIT:
            print("Au revoir !")
            os._exit(os.EX_OK)
        else:
            user_menu_choice = None

        if tournament_choiced:
            user_menu_choice = game.run_tournament(tournament_choiced)
        else:
            user_menu_choice = None
        tournament_choiced = None


if __name__ == "__main__":
    main()
