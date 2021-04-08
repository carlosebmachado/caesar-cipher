import cryptography as c
from cryptography import CCBruteForce


def main():
    ccbf = CCBruteForce('dicionariopt.txt')
    frase1 = c.get_file_content('frase1.txt')
    frase2 = c.get_file_content('frase2.txt')
    dec1 = ccbf.decrypt(frase1)
    dec2 = ccbf.decrypt(frase2)
    print('Frase 1:\n', dec1[0], '\nkey:', dec1[1], '\n\n')
    print('Frase 2:\n', dec2[0], '\nkey:', dec2[1], '\n\n')


main()
