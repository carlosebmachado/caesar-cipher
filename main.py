import cryptography as c
from cryptography import CCBruteForce

'''
ATIVIDADE
A atividade da M1 será um algoritmo força bruta capaz de quebrar a Cifra de César automaticamente.
Para isso, devem ser utilizados os arquivos fantasia.txt e lagrimas.txt como mensagens a serem lidas, e o arquivo 
dicionariopt.txt como dicionário do idioma.
Para facilitar, não serão utilizados acentos nas palavras. O dicionariocompletopt.txt possui todas as palavras da 
língua portuguesa. Para quem quiser um desafio a mais, pode fazer um algoritmo para o processo de codificar qualquer 
mensagem (CUIDADO com os acentos)
'''


def main():
    ccbf = CCBruteForce()
    frase1 = c.get_file_content('frase1.txt')
    frase2 = c.get_file_content('frase2.txt')
    dec1 = ccbf.decrypt(frase1)
    dec2 = ccbf.decrypt(frase2)
    print('Frase 1:\n', dec1, '\n\n')
    print('Frase 2:\n', dec2, '\n\n')


main()
