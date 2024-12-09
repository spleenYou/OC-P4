from views.show import Show


class Prompts:
    def __init__(self):
        self.show = Show()

    def prompt_for_tournament_name(self, name_tournament=None):
        if not name_tournament:
            self.show.display("Création d'un tournoi", ["Nom du tournoi"], "center")
        else:
            content = []
            content.append(f"Nom actuel : {name_tournament}")
            content.append("Appuyer sur entrée pour garder le nom actuel")
            self.show.display("Mise à jour d'un tournoi", content, "center")
        tournament_name = input("Quel est le nouveau nom du tournoi ? ")
        return tournament_name

    def prompt_for_tournament_place(self, tournament_place=None):
        if not tournament_place:
            self.show.display("Création d'un tournoi", ["Emplacement du tournoi"], "center")
        else:
            content = []
            content.append(f"Emplacement actuel : {tournament_place}")
            content.append("Appuyer sur entrée pour garder l'emplacement actuel")
            self.show.display("Mise à jour d'un tournoi", content, "center")
        tournament_place = input("Où se trouve le tournoi ? ")
        return tournament_place

    def prompt_for_tournament_number_of_rounds(self):
        self.show.display("Création d'un tournoi", ["Nombre de tours"], "center")
        number_of_rounds = input("Combien de tours comprend le tournoi ? ")
        return number_of_rounds

    def prompt_for_tournament_number_players(self):
        self.show.display("Création d'un tournoi", ["Nombre de joueurs"], "center")
        number_players = input("Combien de joueurs participent au tournoi ? ")
        return number_players

    def prompt_for_tournament_description(self, tournament_description=None):
        if not tournament_description:
            self.show.display("Création d'un tournoi", ["Description du tournoi"], "center")
        else:
            content = []
            content.append(f"Emplacement actuel : {tournament_description}")
            content.append("Appuyer sur entrée pour garder la description actuelle")
            self.show.display("Mise à jour d'un tournoi", content, "center")
        tournament_description = input("Veuillez entrer la description du tournoi : ")
        return tournament_description

    def show_ranking(self, players_list):
        content = []
        for player in players_list:
            content.append(f"{players_list.index(player) + 1} - "
                           f"{player.surname} "
                           f"{player.name} "
                           f"({player.chess_id}) : "
                           f"{player.score}")
        self.show.display("Classement provisoire", content, "left")
        input('Appuyer sur une touche pour continuer...')
        return None

    def show_end_tournament(self, players_list):
        content = []
        for player in players_list:
            content.append(f"{players_list.index(player) + 1} - "
                           f"{player.surname} "
                           f"{player.name} "
                           f"({player.chess_id}) "
                           f"avec {player.score} pt(s)")

        self.show.display("Classement final", content, "left")
        input("Appuyer sur une touche...")
        return None

    def prompt_for_new_player_name(self):
        self.show.display("Nouveau joueur", ["Prénom du joueur"], "center")
        new_player_name = input("Quel est le prénom du joueur ? ").capitalize()
        return new_player_name

    def prompt_for_new_player_surname(self, player_name):
        self.show.display("Nouveau joueur", [f"Nom de {player_name}"], "center")
        new_player_surname = input(f"Quel est le nom de famille de {player_name} ? ").upper()
        return new_player_surname

    def prompt_for_new_player_birthday(self, player_name, player_surname):
        self.show.display("Nouveau joueur", [f"Date de naissance de {player_surname} {player_name}"], "center")
        new_player_birthday = input(f"Quel est la date de naissance de {player_surname} {player_name} ? [DD-MM-YYYY] ")
        return new_player_birthday

    def prompt_for_new_player_chess_id(self, player_name, player_surname):
        self.show.display("Nouveau joueur", [f"Identifiant international de {player_surname} {player_name}"], "center")
        new_player_chess_id = input(f"Quel est l'identifiant de {player_surname} {player_name} ? ").upper()
        return new_player_chess_id

    def prompt_for_tournament_choice(self, tournaments_list):
        content = []
        for tournament in tournaments_list:
            content.append(f"{tournaments_list.index(tournament) + 1} - "
                           f"{tournament["tournament"].name}")
        content.append("0 - Annuler")
        self.show.display("Liste des tournois", content, "left")
        tournament_choice = input("Quel tournoi voulez vous continuer ? ")
        return tournament_choice

    def show_tournament_information(self, tournament):
        content = []
        content.append(f" Nom : {tournament.name}")
        content.append(f" Emplacement : {tournament.place}")
        content.append(f" description : {tournament.description}")
        content.append(f" Nombre de tours : {tournament.number_of_rounds()}")
        content.append(f" Tour effectué : {tournament.round_number}")
        content.append(f" Nombre de joueurs : {len(tournament.players_list)}")
        for player in tournament.players_list:
            if player:
                content.append(f" - {player.surname} {player.name}")
            else:
                content.append(" - Non défini")
        self.show.display("Information sur le tournoi", content, "left")
        input('Appuyer sur une touche pour continuer...')

    def prompt_for_player_choice(self, players_list):
        content = []
        for player in players_list:
            content.append(f"{players_list.index(player) + 1} - {player.surname} {player.name} ({player.chess_id})")
        content.append("0 - Nouveau joueur")
        self.show.display("Ajout d'un joueur", content, "left")
        add_player_choice = input("Quel joueur ajouter ? ")
        return add_player_choice

    def prompt_for_player_update(self, old_player_informations, new_player):
        # a refaire
        players_data = [old_player_informations, new_player]
        for player in players_data:
            if players_data.index(player) == 0:
                self.decorated_text(f"Pour le Chess ID : {player.chess_id}", align="left")
                self.decorated_text("")
                self.decorated_text("Anciennes données :", align="left")
            else:
                self.decorated_text("Nouvelles données :", align="left")
            self.decorated_text(f" Nom de famille : {player.surname}", align="left")
            self.decorated_text(f" Prénom : {player.name}", align="left")
            self.decorated_text(f" Date de naissance : {player.birthday}", align="left")
        self.show.display("Doublon détecté", self.content, "left")
        update_choice = input("Souhaitez-vous mettre à jour le joueur (y/n) ?")
        return update_choice

    def show_matches_list(self, round_number, matches_list):
        content = []
        for match in matches_list:
            content.append("Match :")
            content.append(f" - Joueur blanc : {match.white_player["player"].surname} "
                           f"{match.white_player["player"].name} "
                           f"({match.white_player["player"].chess_id})")
            content.append(f" - Joueur noir : {match.black_player["player"].surname} "
                           f"{match.black_player["player"].name} "
                           f"({match.black_player["player"].chess_id})")

        self.show.display(f"Voici les matchs du Round {round_number}", content, "left")
        input('Appuyer sur une touche pour continuer...')
        return None

    def show_match_result(self, match):
        content = []
        content.append(f"    1 - {match.white_player["player"].surname} "
                       f"{match.white_player["player"].name} "
                       f"({match.white_player["player"].chess_id})")
        content.append(f"    2 - {match.black_player["player"].surname} "
                       f"{match.black_player["player"].name} "
                       f"({match.black_player["player"].chess_id})")
        content.append("    0 - Match nul")
        self.show.display("Résultat du match", content, "left")
        winner_player = input("Qui est le vainqueur ? ")
        return winner_player

    def prompt_for_main_menu_choice(self, have_tournament, have_an_unfinished_tournament):
        content = []
        content.append("1- Nouveau tournoi")
        if have_tournament and have_an_unfinished_tournament:
            content.append("2- Reprendre un tournoi")
        else:
            content.append("2- Pas de tournoi en cours")
        if have_tournament:
            content.append("3- Mise à jour des tournois")
        else:
            content.append("3- Pas de tournoi enregistré")
        content.append("4- Mise à jour des joueurs")
        content.append("5- Rapports")
        content.append("0- Quitter")
        self.show.display("Menu principal", content, "left")
        user_choice = input('Que souhaitez-vous faire ? ')
        return user_choice

    def prompt_for_tournament_list(self):
        tournament_choice = input('Quel tournoi reprendre ? ')
        return tournament_choice

    def prompt_for_tournament_management_choice(self, tournaments_list):
        content = []
        for i in range(len(tournaments_list)):
            content.append(f"{i + 1}- {tournaments_list[i].name}")
        content.append("0- Annuler")
        self.show.display("Mise à jours des tournois", content, "left")
        tournament_choice = input("Quel tournoi souhaitez-vous mettre à jour ? ")
        return tournament_choice

    def message(self, title, message):
        content = [message]
        self.show.display(title, content, "center")
        input('Appuyer sur une touche pour continuer...')
