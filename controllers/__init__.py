import os
import constant.constant as CONST

if not os.path.exists('data/'):
    os.makedirs('data/')
if not os.path.isfile(f'data/{CONST.FILENAME_PLAYERS_LIST}'):
    with open(f'data/{CONST.FILENAME_PLAYERS_LIST}', 'w', newline='') as file:
        file.write('[]')
if not os.path.isfile(f'data/{CONST.FILENAME_TOURNAMENTS_LIST}'):
    with open(f'data/{CONST.FILENAME_TOURNAMENTS_LIST}', mode='w', newline='') as file:
        file.write('[]')
