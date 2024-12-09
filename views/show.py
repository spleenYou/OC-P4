import os
import constant.constant as CONST


class Show:
    def decoration(function):
        def text_decorated(*args, **kwargs):
            print(CONST.STARS_LINE_FULL)
            print(CONST.STARS_LINE)
            function(*args, **kwargs)
            print(CONST.STARS_LINE)
            print(CONST.STARS_LINE_FULL)
            print()
        return text_decorated

    def clear_screen(self):
        """
        Clean the console for all os
        """
        command = 'clear'
        if os.name in ('nt', 'dos'):
            command = 'cls'
        os.system(command)

    def display(self, title, content, align):
        self.clear_screen()
        self.head_menu()
        self.title_menu(title)
        self.show_content(content, align)

    @decoration
    def show_content(self, content_table, align):
        if content_table:
            for content in content_table:
                self.decorated_text(content, align)

    @decoration
    def head_menu(self):
        self.decorated_text("Gestionnaire de tournoi d'echecs")

    @decoration
    def title_menu(self, title):
        self.decorated_text(title)

    def decorated_text(self, text='', align="center"):
        if text == CONST.TOP_DECORATION:
            print(CONST.STARS_LINE_FULL)
            print(CONST.STARS_LINE)
            pass
        elif text == CONST.BOTTOM_DECORATION:
            print(CONST.STARS_LINE)
            print(CONST.STARS_LINE_FULL)
            pass
        else:
            spaces_needed = CONST.FRAME_LENGHT - 2*CONST.NUMBER_SIDE_STARS - len(text)
            match align:
                case "left":
                    spaces_left = CONST.SPACE_REQUIRED
                    spaces_right = spaces_needed - spaces_left
                case "right":
                    spaces_right = CONST.SPACE_REQUIRED
                    spaces_left = spaces_needed - spaces_right
                case "center":
                    spaces_left = int(spaces_needed / 2)
                    spaces_right = int(spaces_needed / 2)
                    if spaces_needed % 2 == 1:
                        spaces_right = spaces_right + 1
                case _:
                    spaces_left = CONST.SPACE_REQUIRED
                    spaces_right = CONST.SPACE_REQUIRED
            print(f"{'*'*CONST.NUMBER_SIDE_STARS}"
                  f"{' '*spaces_left}{text}"
                  f"{' '*spaces_right}"
                  f"{'*'*CONST.NUMBER_SIDE_STARS}")
