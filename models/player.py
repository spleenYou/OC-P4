class Player:

    def __init__(self, surname, name, birthday, chess_id):
        self.surname = surname
        self.name = name
        self.birthday = birthday
        self.chess_id = chess_id

    def __str__(self):
        return (f'Nom du joueur : {self.surname}\n'
                f'Prénom du joueur : {self.name}\n'
                f'Date de naissance : {self.birthday}\n'
                f'Chess ID : {self.chess_id}')
