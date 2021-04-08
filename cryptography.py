from operator import add, sub


def get_file_content(path):
    file = open(path, 'r')
    content = file.read()
    file.close()
    return content


class CaesarCipher:
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    def __init__(self, full):
        if full:
            self.alphabet = \
                'aªàáã-milsebêcéóuhtrop.ACúnqdvkô\'SyçgíxzâfjèBGLTNDJMOÁõKPRVHIFUºE QÂïüÍwÔXWîå²³ÊÉöëZÒÓñÚYØøµ'

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


class CCBruteForce:

    def __init__(self, dictionary):
        self.crypto = CaesarCipher(False)
        self.words = get_file_content(dictionary).split('\n')

    def match(self, text):
        s = text.split(' ')
        count = 0
        for w in s:
            if w in self.words:
                count += 1
        return count

    def decrypt(self, text):
        dectext = ''
        best = 0
        key = 0
        for i in range(len(self.crypto.alphabet)):
            ct = self.crypto.decrypt(text, i)
            m = self.match(ct)
            if m > best:
                dectext = ct
                best = m
                key = i
        return [dectext, key]
