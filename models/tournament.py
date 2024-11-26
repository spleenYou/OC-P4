import datetime


class Tournament:
    def __init__(self,
                 name,
                 place,
                 round_number,
                 rounds_list,
                 players_list,
                 description,
                 id,
                 date_start="{:%d-%m-%Y}".format(datetime.date.today()),
                 date_stop='',
                 number_of_rounds=4):
        self.name = name
        self.place = place
        self.date_start = date_start
        self.date_stop = date_stop
        self.round_number = round_number
        if rounds_list is None:
            self.rounds_list = []
        else:
            self.rounds_list = rounds_list
        self.players_list = players_list
        self.description = description
        self.number_of_rounds = number_of_rounds
        self.id = id

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
