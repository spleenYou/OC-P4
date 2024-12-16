class Player:
    """Define a player

    Args:
        surname (str): player's surname
        name (str): player's name
        birthday (str): player's birthday (DD-MM-YYYY)
        chess_id (str): player's chess ID
    """

    def __init__(self, surname, name, birthday, chess_id):
        self.surname = surname
        self.name = name
        self.birthday = birthday
        self.chess_id = chess_id
        self.score = 0

    def update_score(self, point):
        """Update the score after a match

        Args:
            point (int): point to add
        """
        self.score = self.score + point
        if isinstance(self.score, float):
            if int(self.score) == self.score:
                self.score = int(self.score)
