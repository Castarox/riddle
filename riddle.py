def decode_text(text):
    for i in range(len(text)-1):
        if text[i] == ' ':
            print(' ', end='')
        elif text[i] == '\n':
            print('\n', end='')
        else:
            asc = ord(text[i])
            if  96<asc<123: 
                print(chr(122 - (asc - 97)), end='')
            else:
                print(chr(90 - (asc - 65)), end='')
    print('\n')

def create_table():
    table = []
    letter = 0
    for row in range(5):
        table.append([])
        for column in range(5):
            if 97 + letter == 106:
                letter += 1
                table[row].append(97 + letter)
                letter += 1
            else:
                table[row].append(97 + letter)
                letter += 1
    return table


def decode_number():
    row = 0
    column = 0
    table = create_table()
    with open('number.txt') as f:
        text = f.read()
    for i in range(len(text)-1):
        if text[i] == ' ':
            print(' ', end='')
        elif text[i] == '\n':
            print('\n', end='')
        else:
            if row == 0:
                row = 10 - int(text[i])
            else:
                column = 10 - int(text[i])
        if row != 0 and column != 0:
            print(chr(table[row-1][column-1]), end='')
            row = 0
            column = 0
    print('')

def main():
    with open('text.txt') as f:
        text = f.read()
    decode_text(text)
    decode_number()
    
    

if __name__ == '__main__':
    main()