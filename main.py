alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input('Type the shift number:\n'))
def encrypt(text,shift):
    x = []
    for i in range(len(text)):
        x.append(alphabet.index(text[i]))
    en_word = ''
    for i in range(len(x)):
        en_word += alphabet[x[i]+shift]
    print(f'The encoded text is: {en_word}')
def decrypt(text,shift):
    x = []
    for i in range(len(text)):
        x.append(alphabet.index(text[i]))
    d_word = ''
    for i in range(len(x)):
        d_word += alphabet[x[i]-shift]
    print(f'The decoded text is: {d_word}')
if direction == 'encode':
    encrypt(text,shift)
elif direction == 'decode':
    decrypt(text,shift)