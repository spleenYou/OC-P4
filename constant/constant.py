QUIT = 0
MAIN = 1
CREATE_TOURNAMENT = 2
RESUME_TOURNAMENT = 3
LIST_TOURNAMENTS = 4
LIST_PLAYERS = 5
MENU_LIST_TOURNAMENTS = 6
MENU_TOURNAMENT_NAME = 7
SHOW_TOURNAMENT_INFORMATIONS = 8
MENU_PLAYER_CHOICE = 9
UPDATE_PLAYER_CHOICE = 10
MESSAGE = 11
SHOW_MATCHES_LIST = 12
SHOW_MATCH = 13
SHOW_RANKING = 14
FILENAME_PLAYERS_LIST = 'players.json'
FILENAME_TOURNAMENTS_LIST = 'tournaments.json'
WHITE_PLAYER = "0"
BLACK_PLAYER = "1"
NO_WINNER = "2"
FRAME_LENGHT = 60
SPACE_REQUIRED = 5
NUMBER_SIDE_STARS = 1
STARS_LINE_FULL = "*"*FRAME_LENGHT
STARS_LINE = ('*'*NUMBER_SIDE_STARS +
              ' '*(FRAME_LENGHT - 2*NUMBER_SIDE_STARS) +
              '*'*NUMBER_SIDE_STARS)
TOP_DECORATION = "TOP"
BOTTOM_DECORATION = "BOTTOM"
ADD_NEW_PLAYER = 0
CHOOSE_PLAYER_IN_LIST = 1
