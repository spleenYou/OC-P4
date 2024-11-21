class Tournament:
    def __init__(self,
                 name,
                 place,
                 date_start,
                 date_end,
                 round_number,
                 rounds,
                 players_list,
                 description,
                 number_of_rounds=4):
        self.name = name
        self.place = place
        self.date_start = date_start
        self.date_end = date_end
        self.round_number = round_number
        self.rounds = rounds
        self.players_list = players_list
        self.description = description
        self.number_of_rounds = number_of_rounds
