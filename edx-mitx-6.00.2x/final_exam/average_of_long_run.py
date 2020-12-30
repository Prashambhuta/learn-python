#!/usr/bin/python3

import pylab, random, numpy


def getMeanAndStd(X):
    mean = sum(X) / float(len(X))
    tot = 0.0
    for x in X:
        tot += (x - mean) ** 2
    std = (tot / len(X)) ** 0.5
    return mean, std


# You are given this class
class Die(object):
    def __init__(self, valList):
        """ valList is not empty """
        self.possibleVals = valList[:]

    def roll(self):
        return random.choice(self.possibleVals)


def makeHistogram(values, numBins, xLabel, yLabel, title=None):
    """
      - values, a list of numbers
      - numBins, a positive int
      - xLabel, yLabel, title, are strings
      - Produces a histogram of values with numBins bins and the indicated labels
        for the x and y axes
      - If title is provided by caller, puts that title on the figure and otherwise
        does not title the figure
    """
    pylab.hist(values, bins=numBins)
    pylab.xlabel(xLabel)
    pylab.ylabel(yLabel)
    if title:
        pylab.title(title)
    pylab.show()


def getAverage(die, numRolls, numTrials):
    """
      - die, a Die
      - numRolls, numTrials, are positive ints
      - Calculates the expected mean value of the longest run of a number
        over numTrials runs of numRolls rolls.
      - Calls makeHistogram to produce a histogram of the longest runs for all
        the trials. There should be 10 bins in the histogram
      - Choose appropriate labels for the x and y axes.
      - Returns the mean calculated to 3 decimal places
    """
    current_die = die
    values = []
    for trial in range(numTrials):
        count = 1
        temp = 1
        last_roll = None
        for roll in range(numRolls):
            roll_1 = current_die.roll()
            if roll_1 == last_roll:
                temp += 1
                if temp > count:
                    count = temp
            else:
                last_roll = roll_1
                temp = 1
        values.append(count)
    xlabel = 'Longest Run'
    ylabel = 'Count'
    title = 'Average longest run of a single number'
    bins = 10
    makeHistogram(values, bins, xlabel, ylabel, title=title)
    mean_value = getMeanAndStd(values)[0]
    return round(mean_value, 3)


print(getAverage(Die([1, 2, 3, 4, 5, 6, 6, 6, 7]), 1, 1000))
