from controllers.base import Controller
from views.base import View


def main():
    view = View()
    game = Controller(view)
    game.check_path_data_exist()
    game.check_files_data_exist()
    game.main_menu()


if __name__ == "__main__":
    main()
