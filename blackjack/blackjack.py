# function for handling cards
# function for playing 
import random

cards = {
    1:"A",
    2:"2",
    3:"3",
    4:"4",
    5:"5",
    6:"6",
    7:"7",
    8:"8",
    9:"9",
    10:"10",
    11:"J",
    12:"Q",
    13:"K"
}

values = {
    "A":11,
    "2":2,
    "3":3,
    "4":4,
    "5":5,
    "6":6,
    "7":7,
    "8":8,
    "9":9,
    "10":10,
    "J":10,
    "Q":10,
    "K":10
}

isDealer = False
ace = False
stand = False
playerHand = []
dealerHand = []
dealerValue = 0
playerValue = 0

pWin = 0
dWin = 0
push = 0

def dealCards():
    for x in range(2):
        cardIndex = random.randint(1, 13)
        playerHand.append(cards.get(cardIndex))
    for x in range(2):
        cardIndex = random.randint(1, 13)
        dealerHand.append(cards.get(cardIndex))
    return playerHand, dealerHand

def hit(isDealer):
    cardIndex = random.randint(1,13)
    if isDealer == True:
        dealerHand.append(cards.get(cardIndex))
        return dealerHand
    else: 
        playerHand.append(cards.get(cardIndex))
        return playerHand

def dealerAlgo():
    ace = False
    acesUsed = 0
    count = 0
    dealerValue = 0
    bust = False

    while (acesUsed <= count) or (acesUsed == 0 and count == 0):
        dealerValue = 0
        for x in dealerHand:
            dealerValue += values.get(x)
        count = dealerHand.count("A")
        dealerValue -= 10*acesUsed
        if dealerValue > 21 and acesUsed < count:
            acesUsed += 1 
        elif dealerValue > 21 and acesUsed == count:
            bust = True
            break
        elif dealerValue <= 16:
            hit(True)
        elif dealerValue > 21:
            bust = True
            break
        else:
            break
    return dealerHand, dealerValue, bust

def playerAlgo(dealerFirstCardValue, playerValue, playerHand):
    dFCV = dealerFirstCardValue 

    # Different Conditions
    # TODO If an Ace is present, > 21, reset ace to 1  (eq to subtracting 10 from playerValue)
    # If both cards are the same --> split (later date w/ betting)
    bust = False
    ace = False
    stand = False
    acesUsed = 0
    count = 0 
    while(True):
        # Hard Value Decisions
        while (acesUsed == count):
            playerValue = 0
            for x in playerHand:
                playerValue += values.get(x)
            count = playerHand.count("A")
            if playerValue > 21:
                playerValue -= 10*acesUsed
            if (count > 0 and acesUsed != count):
                break
            if (playerValue > 21):
                break
            if 2 <= playerValue <= 11:
                hit(False)
            elif (playerValue < 17 and 7 <= dFCV <= 11):
                hit(False)
            elif (playerValue >= 13 and dFCV < 7):
                stand = True
                break
            elif (playerValue == 12 and  3 < dFCV < 7):
                stand = True
                break
            elif (playerValue == 12 and 1 < dFCV < 4):
                hit(False)
            elif (playerValue >= 17):
                stand = True
                break

        # Count = # of aces in current hand
        # acesUsed = # of aces have been used to decrease value (-10*acesUsed)
        # Once count = acesUsed, should have final value 
        
        # Soft Value Decisions
        while (acesUsed < count):

            playerValue = 0
            for x in playerHand:
                playerValue += values.get(x)
            count = playerHand.count("A")
            otherCards = playerValue - 11*count

            if playerValue > 21:
                acesUsed += 1
                playerValue -= 10*acesUsed 
            elif 1 < otherCards < 7:
                hit(False)
            elif (otherCards == 7 and dFCV > 8):
                hit(False)
            elif (7 < otherCards < 10):
                stand = True
                break
            elif (otherCards == 7 and dFCV < 9):
                stand = True
                break
            elif playerValue == 21:
                stand = True
                break
        if playerValue > 21:
            bust = True
            break
        if stand == True:
            break
    return playerHand, playerValue, bust

def playGame():
    dealersCard = dealerHand[0]
    dealerFirstCardValue = values.get(dealersCard)
    playerValue = 0
    dealerValue = 0

    global pWin
    global dWin
    global push
    
    # TODO Account for blackjack from player or dealer 
    for x in playerHand:
        playerValue += values.get(x)
    for x in dealerHand:
        dealerValue += values.get(x)
    
    if playerValue == 21 and dealerValue != 21:
        pWin += 1
    elif dealerValue == 21:
        dWin += 1
    else: 
        pHand, pValue, pBust = playerAlgo(dealerFirstCardValue, playerValue, playerHand)
        if pBust == True:
            dWin += 1
        else: 
            dHand, dValue, dBust = dealerAlgo()
            if dBust == True:
                pWin += 1
            elif dValue == pValue:
                push += 1
            elif dValue > pValue:
                dWin += 1
            elif pValue > dValue:
                pWin += 1
    

    # TODO assign wins, losses and pushes
    
hands = 100000
for x in range(hands):
    dealCards()
    playGame()
    playerHand = []
    dealerHand = []

pWinP = pWin/float(hands) * 100
dWinP = dWin/float(hands) * 100 
pushP = push/float(hands) * 100
pWinP += pushP
print("Player Win %: " + str(round(pWinP, 2)))
print("Dealer Win %: " + str(round(dWinP, 2)))
# print("Push %: " + str(pushP))






































