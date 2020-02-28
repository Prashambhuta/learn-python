"""
Understanding the logging function, by creating a buggy program.
"""
import logging

"""
There are 5 levels of logging. In order of highest first.
1. CRITICAL - highest, # crash-worthy
2. ERROR    
3. WARNING
4. INFO     - to pass parameters/info at certain junctures.
5. DEBUG    - suitable for development environment.
"""

logging.basicConfig(level=logging.DEBUG,)

#----------------------------------------------------------------------
# to disable logging pass this code
# it will disable all debugs below the level of (logging.'level')
# ---------------------------------------------------------------------

logging.disable(logging.CRITICAL)

logging.debug('Start of program.')


def factorial(n):
    logging.debug('Start of factorial of: %d' % n)
    total = 1
    for number in range(1, n + 1):
        total *= number
        logging.info('The total is: %d' % total)
    return total


print(factorial(5))

logging.info('End of program.')
