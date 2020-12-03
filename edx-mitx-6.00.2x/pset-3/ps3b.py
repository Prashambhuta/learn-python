import random
import pylab

# from ps3b_precompiled_37 import *

import os

os.environ["OPENBLAS_NUM_THREADS"] = "1"

import numpy as np


class NoChildException(Exception):
    """
    NoChildException is raised by the reproduce() method in the SimpleVirus
    and ResistantVirus classes to indicate that a virus particle does not
    reproduce. You can use NoChildException as is, you do not need to
    modify/add any code.
    """


#
# PROBLEM 1
#


class SimpleVirus(object):
    """
    Model of a simple virus with no effects of drugs.
    """

    def __init__(self, maxBirthProb, clearProb):
        """
        Initializes a SimpleVirus.

        Parameters
        ----------
            maxBirthProb: float between 0 and 1
                Maximum reproduction probability.

            clearProb: float between 0 and 1
                Maximum clearance probability.
        """
        self.maxBirthProb = maxBirthProb
        self.clearProb = clearProb

    def getMaxBirthProb(self):
        """
        Returns the maximum reproduction probability.

            Parameters:
                self

            Returns:
                maxBirthProb
        """
        return self.maxBirthProb

    def getClearProb(self):
        """
        Returns the maximum clearance probability.

            Parameters:
                self

            Returns:
                clearProb
        """
        return self.clearProb

    def doesClear(self):
        """
        Returns Boolean value of 'is virus cleared from body?' with a
        probability of clearProb.

            Parameters:
                self
            Returns:
                True with probability ClearProb, False otherwise.
        """
        return bool(np.random.binomial(1, self.getClearProb()))

    def reproduce(self, popDensity):
        """
        Stochastically determines the next change of the virus, i.e. if it
        reproduces or not based on the population density(popDensity) of the
        virus. Higher popDensity means lower chances of reproduction. The
        virus reproduces with the probability of maxBirthProb*(1 - popDensity).

        Called by 'update' method of Patient classes.

            Parameters:
                popDensity - float > 0, <= 1

            Returns:
                a new virus instance with same maxBirthProb and clearProb,
                raise NoChildException if offspring is not produced.
        """
        does_reproduce = np.random.binomial(1, self.maxBirthProb * (
                    1 - popDensity))
        if does_reproduce:
            return SimpleVirus(self.maxBirthProb, self.clearProb)
        else:
            raise NoChildException


class Patient(object):
    """
    A class to represent patients.
    ------------------------------

    Attributes
    ----------
    viruses:
        list representing the virus population (virus instances)

    maxPop:
        maximum virus population for this patient (an integer)

    Methods
    -------
        Getters:
            getViruses - returns a list of all virus instances.

            getMaxPop - returns the max population for this patient

            getTotalPop - returns the total virus population currently.

        update - updates the status of the viruses at each time step.
    """

    def __init__(self, viruses, maxPop):
        """
        Initialises the patient class with a list of viruses and maxPop for
        each patient.

            Parameters:
            -----------
                viruses - list
                    representing the virus population for that patient

                maxPop - integer
                    maximum virus population for this patient
        """
        self.viruses = viruses
        self.maxPop = maxPop

    def getViruses(self):
        """
        returns:
            viruses - list of all virus instances.
        """
        return self.viruses

    def getMaxPop(self):
        """
        returns:
            maxPop - an integer
                representing the maximum virus population of the patient.
        """
        return self.maxPop

    def getTotalPop(self):
        """
        returns:
            totalPop - an integer
                representing the total population of the viruses inside the
                patient (length of the list of viruses).
        """
        return len(self.viruses)

    def update(self):
        """
        updates the viruses status of the patient after each time step.
        executes the following commands.

        - determines if the virus survives and update the virus list
        accordingly.
        - updated popDensity is calculated and saved to be used later.
        - based on the updated popDensity calculate the instances of
        successful reproduction and append the new children to the virus
        list. use the 'reproduce' method of the Virus Class.

        Returns:
            totalPop - an integer
                the total population of the virus after updation.
        """
        updated_virus = []
        for virus in self.viruses:
            if not virus.doesClear():
                updated_virus.append(virus)

        current_pop_density = self.getTotalPop() / self.getMaxPop()

        self.viruses = updated_virus
        for virus in self.getViruses():
            try:
                if current_pop_density < 1:
                    new_child = virus.reproduce(current_pop_density)
                    self.viruses.append(new_child)
                else:
                    break
            except NoChildException:
                continue

        return self.getTotalPop()


def simulationWithoutDrug(numViruses, maxPop, maxBirthProb, clearProb,
                          numTrials):
    """
    For each numTrials trial, instantiates a new patient with numViruses of
    SimpleVirus and update the population for 300 time-steps, and plot the
    average virus population as a function of time.

    Parameters:
        numViruses - int; no of viruses to be instantiated
        maxPop - int; maximum virus holding population
        maxBirthProb - between(0,1); maximum birth probability
        clearProb - between(0,1); maximum clearing probability
        numTrials - int; no of cylincal trials
    """
    pop_dict = {x: 0 for x in range(300)}
    for t in range(numTrials):
        viruses = None
        viruses = [SimpleVirus(maxBirthProb, clearProb) for x in range(
            numViruses)]
        patient = None
        patient = Patient(viruses, maxPop)
        for i in range(300):
            patient.update()
            pop_dict[i] = pop_dict.get(i) + patient.getTotalPop()

    values = list(pop_dict.get(x) for x in range(300))
    y_values = [x / numTrials for x in values]
    pylab.plot(y_values, label='SimpleVirus')
    pylab.title('SimpleVirus simulation')
    pylab.xlabel('Time steps')
    pylab.ylabel('Average virus population')
    pylab.legend(loc="best")
    pylab.show()


class ResistantVirus(SimpleVirus):
    """
    Representation of a virus which can have drug resistance.
    """

    def __init__(self, maxBirthProb, clearProb, resistances, mutProb):
        """
        Initialize a ResistantVirus instance, saves all parameters as attributes
        of the instance.
        maxBirthProb: Maximum reproduction probability (a float between 0-1)
        clearProb: Maximum clearance probability (a float between 0-1).
        resistances: A dictionary of drug names (strings) mapping to the state
        of this virus particle's resistance (either True or False) to each drug.
        e.g. {'guttagonol':False, 'srinol':False}, means that this virus
        particle is resistant to neither guttagonol nor srinol.
        mutProb: Mutation probability for this virus particle (a float). This is
        the probability of the offspring acquiring or losing resistance to a drug.
        """
        super().__init__(maxBirthProb, clearProb)
        self.resistances = resistances
        self.mutProb = mutProb

    def getResistances(self):
        """
        returns:
            resistances - a dict mapping for name of drug vs resistance
            towards that drug.
        """
        return self.resistances

    def getMutProb(self):
        """
        returns:
            mutProb - a float between(0,1)
                represents the probability of offspring acquiring mutation.
        """
        return self.mutProb

    def isResistantTo(self, drug):
        """
        check resistance list to see if the virus is resistant to particular
        drug.

        parameters:
            drug - str; a drug name

        returns:
            True or False - True if virus is resistant to particular drug.
        """
        return self.getResistances().get(drug, False)

    def reproduce(self, popDensity, activeDrugs):
        """
        A virus only reproduces if it has resistance to all drugs in list -
        activeDrugs.

        Probability of reproduction = maxBirthProb * (1 - popDensity)

        If reproduce, then instantiate a new ResistanceVirus object with same
        attributes - maxBirthProb, clearProb, mutProb as parent.

        For resistances, the off-spring has a mutProb of changing resistances
        to particular drug, and (1-mutProb) of not changing.

        parameters:
            popDensity - a float; population density of the virus.
            activeDrugs - a list of drug names acting on the virus.

        returns:
            a new offspring of ResistanceVirus class or NoChildException.
        """
        resistant_dict = self.getResistances().copy()
        if all([self.isResistantTo(x) for x in activeDrugs]):
            does_reproduce = np.random.binomial(1, self.getMaxBirthProb()*(
                    1-popDensity))
            if does_reproduce:
                does_mutate = np.random.binomial(1, self.getMutProb())
                if does_mutate:
                    for d_name, resistance in resistant_dict.items():
                        resistant_dict[d_name] = not resistance
                    return ResistantVirus(self.getMaxBirthProb(),
                                          self.getClearProb(),
                                          resistant_dict, self.getMutProb())
                else:
                    return ResistantVirus(self.getMaxBirthProb(),
                                          self.getClearProb(),
                                          self.getResistances(), self.getMutProb())
            else:
                raise NoChildException



        #     if not self.isResistantTo(name):
        #         return NoChildException
        # does_reproduce = np.random.binomial(1, self.maxBirthProb * (
        #             1 - popDensity))
        # if does_reproduce:
        #     does_mutate = np.random.binomial(1, self.mutProb)
        #     if does_mutate:
        #         for name, is_resistant in resistant_list.items():
        #             resistant_list[name] = not is_resistant
        #         return ResistantVirus(self.maxBirthProb,
        #                               self.clearProb,
        #                               resistant_list, self.mutProb)
        #     else:
        #         return ResistantVirus(self.maxBirthProb,
        #                               self.clearProb,
        #                               self.resistances, self.mutProb)
        #
        # else:
        #     return NoChildException

class TreatedPatient(Patient):
    """
    Representation of a patient. The patient is able to take drugs and his/her
    virus population can acquire resistance to the drugs he/she takes.
    """

    def __init__(self, viruses, maxPop):
        """
        Initialization function, saves the viruses and maxPop parameters as
        attributes. Also initializes the list of drugs being administered
        (which should initially include no drugs).

        viruses: The list representing the virus population (a list of
        virus instances)

        maxPop: The  maximum virus population for this patient (an integer)
        """
        super().__init__(viruses, maxPop)
        self.drugs = []


    def addPrescription(self, newDrug):
        """
        Administer a drug to this patient. After a prescription is added, the
        drug acts on the virus population for all subsequent time steps. If the
        newDrug is already prescribed to this patient, the method has no effect.

        newDrug: The name of the drug to administer to the patient (a string).

        postcondition: The list of drugs being administered to a patient is updated
        """
        if newDrug not in self.drugs:
            self.drugs.append(newDrug)


    def getPrescriptions(self):
        """
        Returns the drugs that are being administered to this patient.

        returns: The list of drug names (strings) being administered to this
        patient.
        """
        return self.drugs


    def getResistPop(self, drugResist):
        """
        Get the population of virus particles resistant to the drugs listed in
        drugResist.

        drugResist: Which drug resistances to include in the population (a list
        of strings - e.g. ['guttagonol'] or ['guttagonol', 'srinol'])

        returns: The population of viruses (an integer) with resistances to all
        drugs in the drugResist list.
        """
        count = 0
        viruses = self.getViruses()
        try:
            for name in drugResist:
                for virus in viruses:
                    if not virus.isResistantTo(name):
                        break
                count += 1
        except AttributeError:
            return 0
        return count


    def update(self):
        """
        Update the state of the virus population in this patient for a single
        time step. update() should execute these actions in order:

        - Determine whether each virus particle survives and update the list of
          virus particles accordingly

        - The current population density is calculated. This population density
          value is used until the next call to update().

        - Based on this value of population density, determine whether each
          virus particle should reproduce and add offspring virus particles to
          the list of viruses in this patient.
          The list of drugs being administered should be accounted for in the
          determination of whether each virus particle reproduces.

        returns: The total virus population at the end of the update (an
        integer)
        """
        updated_virus = []
        for virus in self.viruses:
            if not virus.doesClear():
                updated_virus.append(virus)

        current_pop_density = self.getTotalPop() / self.getMaxPop()

        self.viruses = updated_virus
        for virus in self.getViruses():
            try:
                if current_pop_density < 1:
                    new_child = virus.reproduce(current_pop_density,
                                                self.getPrescriptions())
                    self.viruses.append(new_child)
                else:
                    break
            except NoChildException:
                continue

        return self.getTotalPop()


def simulationWithDrug(numViruses, maxPop, maxBirthProb, clearProb, resistances,
                       mutProb, numTrials):
    """
    Runs simulations and plots graphs for problem 5.

    For each of numTrials trials, instantiates a patient, runs a simulation for
    150 timesteps, adds guttagonol, and runs the simulation for an additional
    150 timesteps.  At the end plots the average virus population size
    (for both the total virus population and the guttagonol-resistant virus
    population) as a function of time.

    numViruses: number of ResistantVirus to create for patient (an integer)
    maxPop: maximum virus population for patient (an integer)
    maxBirthProb: Maximum reproduction probability (a float between 0-1)
    clearProb: maximum clearance probability (a float between 0-1)
    resistances: a dictionary of drugs that each ResistantVirus is resistant to
                 (e.g., {'guttagonol': False})
    mutProb: mutation probability for each ResistantVirus particle
             (a float between 0-1).
    numTrials: number of simulation runs to execute (an integer)

    """
    pop_dict = {x: 0 for x in range(300)}
    resistant_dict = {x: 0 for x in range(300)}
    for t in range(numTrials):
        viruses = None
        viruses = [ResistantVirus(maxBirthProb, clearProb, resistances, mutProb)
                   for x in range(numViruses)]
        patient = None
        patient = TreatedPatient(viruses, maxPop)
        for i in range(150):
            patient.update()
            pop_dict[i] = pop_dict.get(i) + patient.getTotalPop()
            resistant_dict[i] = resistant_dict.get(i) + patient.getResistPop(
                ['guttagonol'])
        patient.addPrescription('guttagonol')
        for i in range(150, 300):
            patient.update()
            pop_dict[i] = pop_dict.get(i) + patient.getTotalPop()
            resistant_dict[i] = resistant_dict.get(i) + patient.getResistPop(
                ['guttagonol'])
    values = list(pop_dict.get(x) for x in range(300))
    y_values = [x / numTrials for x in values]
    values_2 = list(resistant_dict.get(x) for x in range(300))
    y_values_2 = [x / numTrials for x in values_2]
    pylab.plot(y_values, label='Non-resistant population')
    pylab.plot(y_values_2, label='Resistant population')
    pylab.title('Virus simulation')
    pylab.xlabel('Time steps')
    pylab.ylabel('Average virus population')
    pylab.legend(loc="best")
    pylab.show()





# SV1 = SimpleVirus(1, 0)
# # SV2 = SimpleVirus(1, 0.1)
# prasham = Patient([SV1], 70)
# # print(prasham.getViruses())
# for i in range(10):
#     prasham.update()
# print(prasham.getTotalPop())

# simulationWithoutDrug(numViruses=100, maxPop=1000, maxBirthProb=0.1,
# clearProb=0.05, numTrials=100)


# RV1 = ResistantVirus(1, 0, ['drug_a', 'drug_b'], 1)
# # SV2 = SimpleVirus(1, 0.1)
# prasham = Patient([RV1], 70)
# # print(prasham.getViruses())
# for i in range(10):
#     prasham.update()
#
# print(RV1.getResistances())
