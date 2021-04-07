file = open('dicionarioptcompleto.txt', 'r')
content = file.read()
file.close()
content = content.replace('\n', '')
alphabet_arr = []
for c in content:
    if not (c in alphabet_arr):
        alphabet_arr.append(c)
alphabet = ''.join(alphabet_arr)
file = open('alphabet.txt', 'w')
file.write(alphabet)
file.close()
