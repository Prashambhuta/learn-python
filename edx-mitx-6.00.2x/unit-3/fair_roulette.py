#!/usr/bin/python3

import random

class FairRoulette():
    def __init__(self):
        self.pockets = []
        for i in range(1, 37):
            self.pockets.append(i)

        self.ball = None
        self.blackOdds, self.redOdds = 1.0, 1.0
        self.pocketOdds = len(self.pockets) - 1.0

    def spin(self):
        self.ball = random.choice(self.pockets)

    def isBlack(self):
        if type(self.ball) != int:
            return False
        if (0 < self.ball <= 10) or (18 < self.ball <= 28):
            return self.ball%2 == 0
        else:
            return self.ball%2 == 1
    def isRed(self):
        return type(self.ball) == int and not self.isBlack()

    def betBlack(self, amt):
        if self.isBlack():
            return amt*self.blackOdds
        else:
            return -amt

    def betRed(self, amt):
        if self.isRed():
            return amt*self.redOdds
        else:
            return -amt

    def betPocket(self, pocket, amt):
        if str(pocket) == str(self.ball):
            return amt*self.pocketOdds
        else:
            return -amt

    def __str__(self):
        return 'Fair Roulette'


def playRoulette(game, numSpins, toPrint=True):
    lucky_number = 2
    bet = 1
    totRed, totBlack, totPocket = 0, 0, 0
    for i in range(numSpins):
        game.spin()
        totRed += game.betRed(bet)
        totBlack += game.betBlack(bet)
        totPocket += game.betPocket(lucky_number, bet)

    if toPrint:
        print(numSpins, 'spins of a', game)
        print('Expected Return betting Red', totRed)
        print('Expected return betting black', totBlack)
        print('Expected return betting pockets two', totPocket)

    return totRed, totBlack, totPocket


class EuRoulette(FairRoulette):
    def __init__(self):
        FairRoulette.__init__(self)
        self.pockets.append('0')

    def __str__(self):
        return 'European Roulette'


class AmRoulette(EuRoulette):
    def __init__(self):
        EuRoulette.__init__(self)
        self.pockets.append('00')

    def __str__(self):
        return 'American Roulette'


def getMeanAndStd(X):
    mean = sum(X)/float(len(X))
    tot = 0.0
    for x in X:
        tot += (x-mean)**2
    std = (tot/len(X))**0.5
    return mean, std


def findPocketReturns(game, numTrials, trialSize, toPrint):
    pocketReturns = []
    for t in range(numTrials):
        trialVals = playRoulette(game, trialSize)
        pocketReturns.append(trialVals[2])
    return pocketReturns
random.seed(0)
numTrials = 20
result_dict = {}
games = (FairRoulette, EuRoulette, AmRoulette)
for G in games:
    result_dict[G().__str__()] = []

for numSpins in [100, 1000, 10000, 100000]:
    print('\nSimulating betting pocket for', numTrials, 'trials of',
          numSpins, 'no of Spins.')
    for G in games:
        pocketReturns = findPocketReturns(G(), numTrials, numSpins, False)
        mean, std = getMeanAndStd(pocketReturns)
        print('Exp. return for', G(), '=', str(round(100*mean, 3))
                     + '%,', '+/- ' + str(round(100*1.96*std, 3))
                     + '% with 95% confidence')


# numSpins = 1000
# # game = FairRoulette()
# playRoulette(FairRoulette(), numSpins)