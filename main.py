"""Entry point."""

from controllers.base import Controller
from views.base import View


def main():
    view = View()
    game = Controller(view)
    game.main_menu()


if __name__ == "__main__":
    main()
