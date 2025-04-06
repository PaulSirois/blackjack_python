import random
# Hands
player_hand = []
dealer_hand = []

# Deck
values = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'J':10, 'Q':10, 'K':10}
deck = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'] * 4

# Game functions
def calculate(hand):
    total = 0
    for card in hand:
        if card == 'A':
            if total > 10:
                total += 1
            else:
                total += 11
        else:
            total += values[card]
    return total

def bet(amount):
    print('Betting', amount)

def deal_cards():
    print('Shuffling...')
    random.shuffle(deck)
    print('Dealing cards...')
    
    while len(dealer_hand) < 2 and len(player_hand) < 2:
        dealer_hand.append(deck.pop())
        player_hand.append(deck.pop())
    
    print(calculate(player_hand))


def hit():
    print('Hit')


def stand():
    print('Stand')


def double_down():
    print('Double down')


def surrender():
    print('Surrender')


def main():
    print('Welcome to blackjack')

    money = 100
    bet_mount = input('How much would you like to bet? Total: '+ str(money) +'\n')
    
    deal_cards()
    deal = True
    while(deal):
    
        answer = input('What would you like to do? Input number.\n [1] hit\n [2] stand\n [3] double down\n [4] surrender\n')
    
        match answer:
            case 1: hit()
            case 2: stand()
            case 3: double_down()
            case 4: surrender()

if __name__ == '__main__':
    main()