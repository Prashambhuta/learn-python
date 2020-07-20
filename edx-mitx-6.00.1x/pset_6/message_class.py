import string


def valid_word(word_list, word):
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list


class Message(object):
    def __init__(self, text):
        self.message_text = text
        self.valid_words = ['hello', 'okay']

    def get_message_text(self):
        return self.message_text

    def get_valid_words(self):
        return self.valid_words[:]

    # def build_shift_dict(self, shift):
    #     letters_lower = []
    #     letters_upper = []
    #     for alphabet in string.ascii_lowercase:
    #         letters_lower.append(alphabet)
    #
    #     for alphabet in string.ascii_uppercase:
    #         letters_upper.append(alphabet)
    #
    #     lowcase_map = dict(
    #         zip([x for x in string.ascii_lowercase], [n + 1 for n in range(
    #             len(string.ascii_lowercase))]))
    #
    #     highcase_map = dict(zip([x for x in string.ascii_uppercase],
    #                             [n + 1 for n in
    #                              range(len(string.ascii_uppercase))]))
    #
    #     low_letter = lowcase_map.copy()
    #     high_letter = highcase_map.copy()
    #     answer = {x: letters_lower[letters_lower.index(x) - 26 + shift] for x
    #               in
    #               low_letter.keys()}
    #     answer.update(
    #         {x: letters_upper[letters_upper.index(x) - 26 + shift] for x in
    #          high_letter.keys()})
    #     return answer

    def build_shift_dict(self, shift):
        lower_keys = [x for x in string.ascii_lowercase]
        lower_values = [x for x in string.ascii_lowercase]
        upper_keys = [x for x in string.ascii_uppercase]
        upper_values = [x for x in string.ascii_uppercase]

        lower_shift_values = lower_values[shift:] + lower_values[:shift]
        upper_shift_values = upper_values[shift:] + upper_values[:shift]

        mapping = dict(zip(lower_keys, lower_shift_values))
        mapping.update(dict(zip(upper_keys, upper_shift_values)))

        return mapping

    def apply_shift(self, shift):
        encrypted_string = []
        shifted = shift
        current_mapping = self.build_shift_dict(shifted)
        for letter in self.message_text:
            if letter in current_mapping.keys():
                encrypted_string.append(current_mapping.get(letter))
            else:
                encrypted_string.append(letter)
        return ''.join(encrypted_string)


class PlainText(Message):
    def __init__(self, text, shift):
        Message.__init__(self, text)
        self.shift = shift
        self.encrypting_dict = self.build_shift_dict(shift)
        self.message_text_encrypted = self.apply_shift(shift)

    def change_shift(self, shift):
        self.shift = shift
        self.encrypting_dict = self.build_shift_dict(shift)
        self.message_text_encrypted = self.apply_shift(shift)


class CiphertextMessage(Message):
    def __init__(self, text):
        Message.__init__(self, text)

    def decrypt_message(self):
        """
        returns a tuple with shift value and decrypted text
        """
        shift = -1
        max_valid_words = [0, shift, None]
        while shift < 26:
            shift += 1
            max_words = 0
            shifted_text = self.apply_shift(shift)
            print(shifted_text)
            for word in shifted_text.split(' '):
                if valid_word(['hello', 'world'], word.lower()):
                    print('TRUE')
                    max_words += 1
            if max_words > max_valid_words[0]:
                max_valid_words[0] = max_words
                max_valid_words[1] = shift
                max_valid_words[2] = shifted_text

        return tuple(max_valid_words[1:])


# text = PlainText('Hello World!', 2)
# print(text.encrypting_dict)
# text.change_shift(3)
# print(text.message_text_encrypted)

cipher_text = CiphertextMessage('Spwwz Hzcwo!')
cipher_text.decrypt_message()
