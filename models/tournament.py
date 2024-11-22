import datetime


class Tournament:
    def __init__(self,
                 name,
                 place,
                 round_number,
                 players_list,
                 description,
                 number_of_rounds=4):
        self.name = name
        self.place = place
        self.date_start = datetime.date.today()
        self.round_number = round_number
        self.rounds = 0
        self.players_list = players_list
        self.description = description
        self.number_of_rounds = number_of_rounds

    def __str__(self):
        for player in self.players_list:
            print(player)
        print(f'Nom : {self.name}\n'
              f'Endroit : {self.place}\n'
              f'Numero du tour : {self.round_number}\n'
              f'Date de début : {self.date_start}\n'
              f'Description : {self.description}\n'
              f'Nombre de tours : {self.number_of_rounds}')
        return ""
