import random

def value(a):
    if a == 'A':
        return 11
    elif a == 'J' or a == 'Q' or a == 'K':
        return 10
    else:
        return int(a)

# 定義牌組和點數
cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

def draw_card():
    return random.choice(cards)

def calculate_score(hand):
    total = sum(value(card) for card in hand)
    # 如果爆點，且有A，可以將A當成1點
    aces = hand.count('A')
    while total > 21 and aces:
        total -= 10
        aces -= 1
    return total

def player_turn(player_name):
    hand = []
    while True:
        card = draw_card()
        hand.append(card)
        score = calculate_score(hand)
        print(f"{player_name}抽到: {card}, 目前點數: {score}")
        if score >= 21:
            break
        cont = input("是否繼續加牌(Y/N): ")
        if cont != "Y":
            break
    return score

print("== 21點遊戲開始 ==")
print("玩家1回合：")
player1_score = player_turn("玩家1")
print("\n玩家2回合：")
player2_score = player_turn("玩家2")

print(f"\n玩家1點數: {player1_score}, 玩家2點數: {player2_score}")

# 判斷勝負
if player1_score > 21 and player2_score > 21:
    print("雙方都爆點，平手")
elif player1_score > 21:
    print("玩家1爆點，玩家2贏了")
elif player2_score > 21:
    print("玩家2爆點，玩家1贏了")
elif player1_score > player2_score:
    print("玩家1贏了")
elif player2_score > player1_score:
    print("玩家2贏了")
else:
    print("平手")

