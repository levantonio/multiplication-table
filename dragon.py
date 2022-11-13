import random
import time


def intro():
    print('''Вы находитесь в зеилях, заселённых драконами.
    Перед собой вы видите две пещеры. В одной из них - дружелюбный дракон,
    который поделится своими сокровищами. Во второй - 
    жадный и голодный дпакон, который мигом вас сожрёт. ''')
    print()

def choose():
    cave = 0
    while cave != 1 and cave != 2:
        print('В какую пещеру вы войдёте? (нажмите 1 или 2)')
        cave = int(input())

    return cave

def check(choosen):
    print('Вы приближаетесь к пещере...')
    time.sleep(2)
    print('Её темнота заставляет вас дрожать от страха...')
    time.sleep(2)
    print('Большой дракон выпрыгивант перед вами! Он раскрывает свою пасть... и...')
    time.sleep(2)

    friendly = int(random.randint(1, 2))

    if choosen == friendly:
        print('... делится с вами своими сокровищами!')
    else:
        print('... моментально сжирает вас!')

play_again = 'да'
while play_again == 'да' or play_again == 'д':
    intro()
    caveNum = choose()
    check(caveNum)

    print('Попытаете удачу еще раз? (да или нет)')
    play_again = input()
