from operator import add, sub


class Cryptography:
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    def encrypt(self, value, key):
        return self.__core(add, value, key)

    def decrypt(self, value, key):
        return self.__core(sub, value, key)

    def __core(self, op, value, key):
        nstr = []
        for c in value:
            if not self.__is_letter(c):
                nstr.append(c)
                continue
            nstr.append(self.alphabet[self.__normalize_index(op(self.__find_index(c), key))])
        return ''.join(nstr)

    def __is_letter(self, c):
        return self.alphabet.find(c) != -1

    def __normalize_index(self, i):
        asize = len(self.alphabet)
        neg = i < 0
        if neg:
            i *= -1
        while i >= asize:
            i -= asize
        if neg:
            i *= -1
        return i

    def __find_index(self, c):
        return self.alphabet.index(c)
