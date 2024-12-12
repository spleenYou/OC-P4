                                                  _:_
                                                 '-.-'
                                        ()      __.'.__
                                     .-:--:-.  |_______|
                              ()      \____/    \=====/
                              /\      {====}     )___(
                   (\=,      //\\      )__(     /_____\
         |'-'-'|  //  .\    (    )    /____\     |   |
         |_____| (( \_  \    )__(      |  |      |   |
          |===|   ))  `\_)  /____\     |  |      |   |
          |   |  (/     \    |  |      |  |      |   |
          |   |   | _.-'|    |  |      |  |      |   |
          )___(    )___(    /____\    /____\    /_____\
         (=====)  (=====)  (======)  (======)  (=======)
         }====={  }====={  }======{  }======{  }======={
        (_______)(_______)(________)(________)(_________)

# Chess tournament manager

## Introduction

This script can handle chess contest in local mode.

## Getting started

- Python version 3.12.7

### Packages used

- flake8
- flake8-html

### Virtual environment


#### Creation

Create the virtual environment

Replace :
- \<version> by your version number of python
- <nom_de_l_environnement_virtuel> by the name you like

```
python<version> -m venv <nom_de_l_environnement_virtuel>
```

#### Activation

Activate the virtual environment

For windows
```
<nom_de_l_environnement_virtuel>/Scripts/activate
```

For Unix/macOs

```
source .<nom_de_l_environnement_virtuel>/bin/activate
```

#### Packages

Install needed packages for the script

```
pip install -r requirements.txt
```
## Use

launch the script and choose what you want to do
```
python main.py

or

python3 main.py
```

### Menu Description

#### Main menu

The main menu look like that :

1. Nouveau tournoi
2. Pas de tournoi en cours / Reprendre un tournoi
3. Pas de tournoi enregistré / Mise à jour des tournois
4. Pas de tournoi enregistré / Mise à jour des joueurs
5. Rapports
    1. Liste des joueurs par ordre alphabétique
    2. Liste des tournois
    3. Information sur un tournoi
        1. Liste des joueurs
        2. Déroulement du tournoi
        0. Retour
   0. Retour
0-  Quitter

> Menu 1 - New tournament

The script will ask you tournament's name, place, description, number of rounds and number of players

The minimum number of rounds is four.

The minimum number of players is eight.

> Menu 2 - No tournament in progress / Resume a tournament

If at least a tournament is in progress, you can resume it

A list of unfinished tournaments will be displayed

Choose one and continue

> Menu 3 - No tournament registered / Tournament update

If at least one tournament is registered, you can update the following data:

- Name
- Place
- Description

> Menu 4 - No player registered / Player update

If at least one tournament is registered, you can update the following data:

- Name
- Surname
- Birthday
- Chess id

> 5 - Reports

##### 5.1 - List of players in alphabetical order

Shows the list of all the players in alphabetical order

##### 5.2 - List of tournaments

Shows the list of all the tournaments

##### 5.3 - Tournament's information

Shows the list of all tournaments and select the tournament on which you wish to obtain information

###### 5.3.1 - List of players

Shows the list tournament's players in alphabetical order

###### 5.3.2. - Tournament progress

Shows the tournament's rounds and matches

###### 5.3.0. - Go back

Go back to the previous menu

##### 5.0. Go back

Go back to the previous menu

> 0 - Quit

Quit the script

## Check the code

Use flake8 to check if the project follow pep-8 guide for python code

```
flake8 --format=html --htmldir=flake8-html
```

It will create a HTML file with the result in the folder "flake8-html"