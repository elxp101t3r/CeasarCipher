alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input('Type the shift number:\n'))
def encrypt(text,shift):
    #letters position
    x = []
    for i in range(len(text)):
        x.append(alphabet.index(text[i]))
    en_word = ''
    for i in range(len(x)):
        en_word += alphabet[x[i]+shift]
    print(f'The encoded text is: {en_word}')
encrypt(text,shift)