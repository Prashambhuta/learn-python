import random
import pylab

# Global Variables
MAXRABBITPOP = 1000
CURRENTRABBITPOP = 50
CURRENTFOXPOP = 300

def rabbitGrowth():
    """ 
    rabbitGrowth is called once at the beginning of each time step.

    It makes use of the global variables: CURRENTRABBITPOP and MAXRABBITPOP.

    The global variable CURRENTRABBITPOP is modified by this procedure.

    For each rabbit, based on the probabilities in the problem set write-up, 
      a new rabbit may be born.
    Nothing is returned.
    """
    # you need this line for modifying global variables
    global CURRENTRABBITPOP

    if CURRENTRABBITPOP < 1000:
        for i in range(CURRENTRABBITPOP):
            if random.random() <= 1 - (CURRENTRABBITPOP/MAXRABBITPOP):
                CURRENTRABBITPOP += 1
        # current_rabit_ratio = CURRENTRABBITPOP / MAXRABBITPOP
        # prob_rabit_birth = 1 - current_rabit_ratio
        # if random.random() <= prob_rabit_birth:
        #     CURRENTRABBITPOP += 1



            
def foxGrowth():
    """ 
    foxGrowth is called once at the end of each time step.

    It makes use of the global variables: CURRENTFOXPOP and CURRENTRABBITPOP,
        and both may be modified by this procedure.

    Each fox, based on the probabilities in the problem statement, may eat 
      one rabbit (but only if there are more than 10 rabbits).

    If it eats a rabbit, then with a 1/3 prob it gives birth to a new fox.

    If it does not eat a rabbit, then with a 1/10 prob it dies.

    Nothing is returned.
    """
    # you need these lines for modifying global variables
    global CURRENTRABBITPOP
    global CURRENTFOXPOP

    if CURRENTRABBITPOP > 10:
        if CURRENTFOXPOP > 10:

            prob_fox_eats_rabbit = CURRENTRABBITPOP/MAXRABBITPOP

            for i in range(CURRENTFOXPOP):
                if random.random() <= prob_fox_eats_rabbit:
                    CURRENTRABBITPOP -= 1
                    if random.random() <= 0.3:
                        CURRENTFOXPOP += 1

                if random.random() <= 0.9:
                    CURRENTFOXPOP -= 1


def runSimulation(numSteps):
    """
    Runs the simulation for `numSteps` time steps.

    Returns a tuple of two lists: (rabbit_populations, fox_populations)
      where rabbit_populations is a record of the rabbit population at the 
      END of each time step, and fox_populations is a record of the fox population
      at the END of each time step.

    Both lists should be `numSteps` items long.
    """

    # TO DO
    rabbit_pop = []
    fox_pop = []
    for steps in range(numSteps):
        rabbitGrowth()
        rabbit_pop.append(CURRENTRABBITPOP)
        foxGrowth()
        fox_pop.append(CURRENTFOXPOP)
    return (rabbit_pop, fox_pop)


def plotting():
    rab_pop, fox_pop = runSimulation(200)
    numTrials = 200
    pylab.plot(range(numTrials), rab_pop, 'r', label = 'Rabbit Population')
    pylab.plot(range(numTrials), fox_pop, 'b', label = 'Fox Population')
    pylab.xlabel('No of Trials')
    pylab.ylabel('Population')
    pylab.legend(loc='best')
    pylab.title('Changes in population')
    rab_fit = pylab.polyfit(range(200), rab_pop, 2)
    fox_fit = pylab.polyfit(range(200), fox_pop, 2)
    pylab.plot(pylab.polyval(rab_fit, range(200)), 'ro')
    pylab.plot(pylab.polyval(fox_fit, range(200)), 'b*')
    pylab.show()


plotting()

