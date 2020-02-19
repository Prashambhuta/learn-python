# re.verbose allows to enter multi-line code.
# Example
import re
message = "My phone number is +91 9427722220, another is 8200324646." \
          "My office number is 02673-221940"
phoneRegex = re.compile(r'''\d\d\d
\d\d\d
\d\d\d\d''', re.IGNORECASE | re.DOTALL | re.VERBOSE)    # using all arguments
                                                        # with pipe
                                                        # character as separator
print(phoneRegex.findall(message))