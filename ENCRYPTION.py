import random

class ENCRYPTION:

    sets = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
            "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z",
            "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "[", "{", "]", "}", "\\", "|", ";", ":", "'", "\"", ",", "<", ".", ">", "/", "?", " "]

    def __init__(self, key = "null"):

        if key == "null":

            self.key = random.randint(1, 52)

        else:

            self.key = key

        print(self.key)

    def get_key(self):

        return self.key

    def encrypt(self, text):

        self.to_return = ""

        for elem in text:

            try:

                ind = ENCRYPTION.sets.index(elem)

                self.to_return += ENCRYPTION.sets[(ind + self.key) % len(ENCRYPTION.sets)]

            except:

                self.to_return += elem

        return self.to_return

    def decrypt(self, text):

        self.to_return = ""

        for elem in text:

            try:

                ind = ENCRYPTION.sets.index(elem)

                self.to_return += ENCRYPTION.sets[(ind - self.key) % len(ENCRYPTION.sets)]

            except:

                self.to_return += elem

        return self.to_return