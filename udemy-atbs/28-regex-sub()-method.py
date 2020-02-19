# Using sub() i.e. subsitute method for regular expression
import re
subRegex = re.compile(r'Agent \w*')
message = "Agent Bond has delivered the package to Agent Bourne."
print(subRegex.findall(message))

# Using sub() method
print(subRegex.sub('*****', message))


# replace Agent Bond with something like Agent B****
substarRegex = re.compile(r'Agent (\w\w)(\w)\w+')

# Using sub() method
print(substarRegex.sub(r'Agent **\2**', message))