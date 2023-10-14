alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input('Type the shift number:\n'))
# def encrypt(text,shift):
#     x = []
#     for i in range(len(text)):
#         x.append(alphabet.index(text[i]))
#     en_word = ''
#     for i in range(len(x)):
#         en_word += alphabet[x[i]+shift]
#     print(f'The encoded text is: {en_word}')
# def decrypt(text,shift):
#     x = []
#     for i in range(len(text)):
#         x.append(alphabet.index(text[i]))
#     d_word = ''
#     for i in range(len(x)):
#         d_word += alphabet[x[i]-shift]
#     print(f'The decoded text is: {d_word}')
# if direction == 'encode':
#     encrypt(text,shift)
# elif direction == 'decode':
#     decrypt(text,shift)
# def caesar(plain_text, shift_amount, direction_of_user):
#     cipher_text = ''
#     for letter in plain_text:
#         position = alphabet.index(letter)
#         if direction_of_user == 'encode':
#             new_position = position + shift_amount
#         elif direction_of_user == 'decode':
#             new_position = position - shift_amount
#         cipher_text += alphabet[new_position]
#     print(f'The encoded text is {cipher_text}')
# caesar(plain_text=text,shift_amount=shift,direction_of_user=direction)
def caesar(start_text,shift_amount,cipher_direction):
    end_text = ''
    for letter in start_text:
        position = alphabet.index(letter)
        if cipher_direction == 'decode':
            shift_amount += -1
        new_position = position + shift_amount
        end_text += alphabet[new_position]
    print(f'The {cipher_direction}d text is {end_text}')
caesar(start_text=text,shift_amount=shift,cipher_direction=direction)