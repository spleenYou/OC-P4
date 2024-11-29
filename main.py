import os
import constant.constant as CONST
from controllers.base import Controller
from views.base import View


def main():
    view = View()
    game = Controller(view)
    user_menu_choice = None
    tournament_choiced = None
    while user_menu_choice is None:
        user_menu_choice = game.ask_menu_choice(CONST.MAIN, game.is_first_time())
        if user_menu_choice == CONST.CREATE_TOURNAMENT:
            tournament_choiced = game.create_tournament()
        elif user_menu_choice == CONST.RESUME_TOURNAMENT:
            tournament_choiced = game.choice_tournament()
        elif user_menu_choice == CONST.LIST_TOURNAMENTS:
            print("liste")
        elif user_menu_choice == CONST.LIST_PLAYERS:
            print("players")
        elif user_menu_choice == CONST.QUIT:
            print('Au revoir !')
            os._exit(os.EX_OK)
        else:
            user_menu_choice = None

        if tournament_choiced:
            game.run_tournament(tournament_choiced)


if __name__ == "__main__":
    main()
