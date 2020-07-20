import string


def mapping(shift):
    letters_lower = []
    letters_upper = []
    for alphabet in string.ascii_lowercase:
        letters_lower.append(alphabet)
        # letters_upper.append(alphabet)

    for alphabet in string.ascii_uppercase:
        letters_upper.append(alphabet)
        # letters_upper.append(alphabet)

    lowcase_map = dict(
        zip([x for x in string.ascii_lowercase], [n + 1 for n in range(
            len(string.ascii_lowercase))]))

    highcase_map = dict(zip([x for x in string.ascii_uppercase], [n + 1 for
                    n in range(len(string.ascii_uppercase))]))

    low_letter = lowcase_map.copy()
    high_letter = highcase_map.copy()
    answer = {x: letters_lower[letters_lower.index(x) - 26 + shift] for x in
              low_letter.keys()}
    answer.update({x: letters_upper[letters_upper.index(x) - 26 + shift] for x in
              high_letter.keys()})
    return answer

def apply_shift(string, shift):
    encrypted_string = []
    current_mapping = mapping(shift)
    for letter in string:
        if letter in current_mapping.keys():
            encrypted_string.append(current_mapping.get(letter))
        else:
            encrypted_string.append(letter)
    print(''.join(encrypted_string))



apply_shift('hell, LLo ggGG aaAA', 2)
