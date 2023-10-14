alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input('Type the shift number:\n'))
def encrypt(text,shift):
    #letters position
    x = []
    for i in range(len(text)):
        x.append(alphabet.index(text[i]))
    #new position
    c = []
    for i in range(len(x)):
        c.append(x[i]+shift)
    #craft of a new word
    w = []
    for i in range(len(c)):
        w.append(alphabet[c[i]])
    print(w)
encrypt(text,shift)