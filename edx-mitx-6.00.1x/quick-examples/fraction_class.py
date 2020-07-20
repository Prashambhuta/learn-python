class Fraction(object):
    def __init__(self, numerator, denominator):
        """
        Takes a numerator, denominator and represents that as a fraction.
        """
        self.numerator = numerator
        self.denominator = denominator

    def __str__(self):
        """
        Prints fraction in its proper form.
        """
        return "< " + str(self.numerator) + "/" + str(self.denominator) + " >"

    def __add__(self, other):
        """
        Adds two fraction, returns a new fraction instance.
        """
        return Fraction(((self.numerator * other.denominator) + (
                other.numerator *
                 self.denominator)), (self.denominator * other.denominator))

    def __sub__(self, other):
        """
        Subtracts two fraction, returns a new fraction instance.
        """
        return Fraction(((self.numerator * other.denominator) - (
                other.numerator *
                 self.denominator)), (self.denominator * other.denominator))

    def convertToDecimal(self):
        """
        Converts the fraction to decimal.
        """
        return self.numerator/self.denominator


d = Fraction(4, 5)
e = Fraction(1, 5)
print(d)
print(d - e)
print(d.convertToDecimal())