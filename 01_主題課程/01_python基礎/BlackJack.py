import random
import time

cardDeck = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

def draw(deck):
    deck.append(random.choice(cardDeck))
def calValue(deck):
    result = 0
    aces = 0
    for i in deck:
        if i == 'J' or i == 'Q' or i == 'K':
            result += 10
        elif i == 'A':
            result += 11
            aces += 1
        else:
            result += int(i)
    while result > 21 and aces:
        result -= 10
        aces -= 1
    return result

def showCard(deck):
    for i in deck:
        print("[", i, "]", sep='', end=' ')
    print("(點數: ", calValue(deck), ")", sep='')

def showDealerCard(dealerDeck):
    first = True
    for i in dealerDeck:
        if first:
            print('[?]', end=' ')
            first = False
        else:
            print("[", i, "]", sep='', end=' ')
    print()

def main():
    print("歡迎來到21點!")

    dealerDeck = []
    draw(dealerDeck)
    draw(dealerDeck)
    print("莊家的牌: ", end='')
    showDealerCard(dealerDeck)
    playerDeck = []
    draw(playerDeck)
    draw(playerDeck)
    while True:
        print("玩家的牌: ", end='')
        showCard(playerDeck)
        choice = input("要牌(h) 或 停牌(s)? ")
        if choice == 's':
            break
        elif choice == 'h':
            draw(playerDeck)
            if calValue(playerDeck) > 21:
                print("玩家爆牌")
                print("莊家贏了")
                return
        else:
            print("未知的選項, 請再試一次")
    print("莊家的牌: ", end='')
    showCard(dealerDeck)
    while calValue(dealerDeck) < 17:
        time.sleep(2)
        draw(dealerDeck)
        print("莊家的牌: ", end='')
        showCard(dealerDeck)
    if calValue(dealerDeck) > 21:
        print("莊家爆牌")
        print("玩家贏了!")
        return
    else:
        print("玩家的牌: ", end='')
        showCard(playerDeck)
        print("莊家的牌: ", end='')
        showCard(dealerDeck)
        if calValue(dealerDeck) > calValue(playerDeck):
            print("裝家贏了")
            return
        elif calValue(dealerDeck) < calValue(playerDeck):
            print("玩家贏了")
            return 
        else:
            print("平手")
            return

main()