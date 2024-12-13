import json
from models.tournament import Tournament
from models.player import Player
from views.show import Show
import constant.constant as CONST


class Load:
    """Manage tournaments and players data load from JSON file"""

    def __init__(self):
        self.show = Show()

    def read_file_players(self):
        """Read the players file

        Returns:
            players_list (list): all the player's objects list

        """
        players_list = []
        players_list_dict = self.read_json_file(CONST.FILENAME_PLAYERS_LIST)
        if players_list_dict:
            for player_data_dict in players_list_dict:
                players_list.append(
                    Player(
                        player_data_dict["surname"],
                        player_data_dict["name"],
                        player_data_dict["birthday"],
                        player_data_dict["chess_id"],
                    )
                )
        return players_list

    def read_file_tournaments(self, all_players_list):
        """Read the tournaments file

        Args:
            all_players_list (list): all the player's objects list

        Returns:
            tournaments_list (list): all the tournament's objects list
        """
        tournaments_list = []
        tournaments_list_dict = self.read_json_file(CONST.FILENAME_TOURNAMENTS_LIST)
        if tournaments_list_dict is None:
            return None
        for tournament_data_dict in tournaments_list_dict:
            tournament = Tournament(
                name=tournament_data_dict["name"],
                place=tournament_data_dict["place"],
                description=tournament_data_dict["description"],
                date_start=tournament_data_dict["date_start"],
                date_end=tournament_data_dict["date_end"],
            )
            for player in tournament_data_dict["players_list"]:
                tournament.add_player(None)
            for player in tournament_data_dict["players_list"]:
                if len(player["chess_id"]):
                    player_data = self.find_player_by_chess_id(
                        player["chess_id"], all_players_list
                    )
                    tournament.add_player(player_data)
            for round in tournament_data_dict["rounds_list"]:
                new_round = tournament.add_round()
                for match in round:
                    score_list = []
                    for score in match:
                        if score[0] == "":
                            player = None
                        else:
                            player = self.find_player_by_chess_id(score[0], tournament.players_list)
                        score_list.append([player, score[1]])
                    new_round.add_match(
                        white_player=score_list[0][0],
                        black_player=score_list[1][0],
                        white_player_score=score_list[0][1],
                        black_player_score=score_list[1][1],
                    )
            tournament.count_round_number()
            tournaments_list.append(tournament)
        return tournaments_list

    def find_player_by_chess_id(self, chess_id, players_list):
        """Return player object compares to chess_id

        Args:
            chess_id (str): chess ID of the player search
            players_list (list): all the player's objects list

        Returns:
            player (object): player object corresponding to the chess ID
            none if no player found
        """
        for player in players_list:
            if player.chess_id == chess_id:
                return player
        return None

    def read_json_file(self, filename):
        """Read json file wanted

        Args:
            filename (str): name of file to read
        """
        try:
            with open(f"data/{filename}", "r") as json_data:
                return json.load(json_data)
        except Exception as e:
            self.show.message(f"Erreur sur le fichier {filename}", e.__str__())
            return None
