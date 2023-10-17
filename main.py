import art
import lists
def caesar(start_text,shift_amount,cipher_direction):
    end_text = ''
    if cipher_direction == 'decode':
            shift_amount *= -1
    for char in start_text:
        if char in lists.alphabet:
            position = lists.alphabet.index(char)
            new_position = (position + shift_amount)%len(lists.alphabet)
            end_text += lists.alphabet[new_position]
        else:
            if char in lists.space:
                position = lists.space.index(char)
                end_text += lists.space[position]
            if char in lists.symbols:
                position = lists.symbols.index(char)
                end_text += lists.symbols[position]
            if char in lists.numbers:
                position = lists.numbers.index(char)
                end_text += lists.numbers[position]
            else:
                end_text += char
    print(f'The {cipher_direction}d text is {end_text}')
print(art.logo)
repeat = 'yes'
while repeat == 'yes':
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input('Type the shift number:\n'))   
    caesar(start_text=text,shift_amount=shift,cipher_direction=direction)
    repeat = input("Do you want to do it again 'yes' or 'no'\n")