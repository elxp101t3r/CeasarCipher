alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
symbols = ['!','@','#','$','%','^','&','*','(',')','~','-','+']
space = [' ']
numbers = ['0','1','2','3','4','5','6','7','8','9']
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
    if cipher_direction == 'decode':
            shift_amount += -1
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = (position + shift_amount)%len(alphabet)
            end_text += alphabet[new_position]
        else:
            if char in space:
                position = space.index(char)
                end_text += space[position]
            if char in symbols:
                position = symbols.index(char)
                end_text += symbols[position]
            if char in numbers:
                position = numbers.index(char)
                end_text += numbers[position]
            else:
                end_text += char
    print(f'The {cipher_direction}d text is {end_text}')
repeat = 'yes'
while repeat == 'yes':
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input('Type the shift number:\n'))   
    caesar(start_text=text,shift_amount=shift,cipher_direction=direction)
    repeat = input("Do you want to do it again 'yes' or 'no'\n")