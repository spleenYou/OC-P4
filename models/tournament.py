import datetime


class Tournament:
    def __init__(self,
                 name,
                 place,
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
        self.rounds_list = rounds_list
        self.round_number = self.count_round_numer()
        self.players_list = players_list
        self.description = description
        self.number_of_rounds = number_of_rounds
        self.id = id

    def matches_in_progress(self):
        return self.rounds_list[self.round_number - 1]

    def count_round_numer(self):
        round_number = 0
        for round in self.rounds_list:
            if len(round) == 0:
                break
            round_number = round_number + 1
        return round_number

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
