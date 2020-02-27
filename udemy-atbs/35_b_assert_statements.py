"""
To understand the application of assert statements.
Let's create a traffic stop for a road intersection.
"""

# Tdef a dictionary to store signal colors

current_signal = {'Turn Left': 'Green', 'Go Straight': 'Green', 'Turn Right':
                               'Red'}


def switch_signals():
    for key in current_signal.keys():
        if current_signal[key] == 'Red':
            current_signal[key] = 'Green'
        elif current_signal[key] == 'Green':
            current_signal[key] = 'Yellow'
        elif current_signal[key] == 'Yellow':
            current_signal[key] = 'Red'
    assert 'Yellow' not in current_signal.values(), 'This is an error ' \
                                                    'message %s' % current_signal


switch_signals()
print(current_signal)
