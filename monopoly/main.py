from board import Board
from player import Player
from place import Place
from random import randint, randrange


def plate(size, chaise):
    for i in range(size):
        if i % 2 == 0:
            c = Place(randrange(5000, 50000, 500))
        else:
            c = Place(randrange(-100000, -5000, 5000))
        chaise.plateau.append(c)

def jeu(player):
    d1 = randint(1,6)
    d2 = randint(1,6)
    result = d1 + d2
    print("Dice said",result)
    if d1 == d2 and player.gold > 0:
        move(player,result)
        if player.gold > 0:
            print(f"{player.name} is at position {player.position}/{chaise.size} with {player.gold}. Also, he made a double. Do it again.")
        else:
            print(f"{player.name} got no gold anymore.")
        d1 = randint(1,6)
        d2 = randint(1,6)
        result = d1 + d2
        print("Dice said",result)
        move(player,result)
        if d1 == d2 and player.gold > 0:
            move(player,result)
            if player.gold > 0:
                print(f"{player.name} is at position {player.position}/{chaise.size} with {player.gold}. Also, he made a double double. Do it again.")
            else:
                print(f"{player.name} got no gold anymore.")
            d1 = randint(1,6)
            d2 = randint(1,6)
            result = d1 + d2
            print("Dice said",result)
            move(player,result)
            if d1 == d2 and player.gold > 0:
                player.gold -= 50000
                print(f"{player.name} is at position {player.position}/{chaise.size} with {player.gold}. Also, he made a triple double. Cheaters are not allowed here. Give us 50 000 bucks.")
    else:
        move(player,result)
        print(f"{player.name} is at position {player.position}/{chaise.size} with {player.gold}.")



def move(player, dice):
    if player.position + dice > chaise.size:
        player.position += dice
        player.position = player.position - chaise.size - 1
    elif player.position + dice == chaise.size:
        player.position += dice
        player.position = player.position - chaise.size
    else:
        player.position += dice
    player.gold += chaise.plateau[player.position].nombre



if __name__ == "__main__":

    chaise = Board(40)
    red = Player("Red")
    green = Player("Green")

    plate(chaise.size, chaise)

    fplayer = randint(1,2)

    while red.gold > 0 and green.gold > 0:
        if fplayer == 1:
            print("Fisrt player, your turn:")
            jeu(red)
            fplayer = 2
        else:
            print("Second player, your turn:")
            jeu(green)
            fplayer = 1
            
    if red.gold <= 0:
        print(f"{green.name} win.")
    else:
        print(f"{red.name} win.")