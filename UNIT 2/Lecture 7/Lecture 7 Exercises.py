import random
class FairRoulette():
    def __init__(self):
        self.pockets = []
        for i in range(1,37):
            self.pockets.append(i)
        self.ball = None
        self.blackOdds, self.redOdds = 1.0, 1.0
        self.pocketOdds = len(self.pockets) -1.0
    def spin(self):
        self.ball = random.choice(self.pockets)

    def isBlack(self):
        if type(self.ball) != int:
            return False
        if ((self.ball > 0 and self.ball <= 10) or (self.ball>18 and self.ball<=28)):
            return self.ball % 2 == 0
        else:
            return self.ball % 2 == 1
    def isRed(self):
        return type(self.ball) == int and not self.isBlack()

    def betBlack(self, amount):
        if self.isBlack():
            return amount * self.blackOdds
        else:
            return -amount
    def betRed(self, amount):
        if self.isRed():
            return amount * self.redOdds
        else:
            return -amount * self.redOdds

    def betPocket(self, pocket, amount):
        if str(pocket) == str(self.ball):
            return amount * self.pocketOdds
        else:
            return - amount

    def __str__(self):
        return 'Fair Reloutte'

def playRoulette(game, numSpins, toPrint = True):
    luckyNumber = '2'
    bet = 1
    totRed, totBlack, totPacket = 0.0, 0.0, 0.0
    for i in range(numSpins):
        game.spin()
        totRed += game.betRed(bet)
        totBlack += game.betBlack(bet)
        totPacket += game.betPocket(luckyNumber, bet)
    if toPrint:
        print(numSpins, 'spins of', game)
        print('Expected return betting red =', str(100* totRed/numSpins) + '%')
        print('Expected return betting black = ', str(100* totBlack/numSpins) + '%')
        print('Expected return betting on number: ', luckyNumber, '=', str(100*totPacket/numSpins) + '%\n')
    return (totRed/numSpins, totBlack/numSpins, totPacket/numSpins)
