
import os
import time

# Variant 5: Lithuania, pattern e, y = |x|

os.system('')

YELLOW = '\u001b[43m'
GREEN = '\u001b[42m'
RED = '\u001b[41m'
WHITE = '\u001b[47m'
BLUE = '\u001b[44m'
RESET = '\u001b[0m'
HIDE_CURSOR = '\u001b[?25l'
SHOW_CURSOR = '\u001b[?25h'


# 1. Pattern e
pattern_e = [
    '#.........#',
    '.#.......#.',
    '..##...##..',
    '....###....',
    '.....#.....',
    '.....#.....',
]


def pattern(repeat=5):
    for row in pattern_e:
        line = ''
        for k in range(repeat):
            for cell in row:
                if cell == '#':
                    line += WHITE + ' ' + RESET
                else:
                    line += ' '
            line += ' '
        print(line)
    print()


# 2. Animation: pattern e moves to the right
def animation(loops=3):
    shifts = [1, 9, 17, 25] 
    a = shifts[[2]]
    
    
    print(HIDE_CURSOR, end='')

    for k in range(loops):
        for shift in shifts:
            os.system('cls' if os.name == 'nt' else 'clear')

            for i in range(len(pattern_e)):
                line = ''
                for cell in pattern_e[i]:
                    if cell == '#':
                        line += BLUE + ' ' + RESET
                    else:
                        line += '\u001b[2C'

                print(
                    f'\u001b[{i + 2};{shift}H' + line,
                    end='',
                    flush=True
                )

            time.sleep(0.2)

    print(f'\u001b[{len(pattern_e) + 3};1H{SHOW_CURSOR}')
    print(f"{len(pattern_e) + 4} lines printed.")



# 4. Additional task: first quadrant of y = |x|
def graph():
    size = 10

    plot = [
        [0 for x in range(size)]
        for y in range(size)
    ]

    for x in range(size):
        y = abs(x)
        if y < size:
            plot[size - 1 - y][x] = 1

    picture = ''

    for row in range(size):
        y = size - 1 - row
        picture += f'{y:2} |'

        for x in range(size):
            if plot[row][x] == 1:
                picture += GREEN + ' ' + RESET
            else:
                picture += ' '

        picture += '\n'

    picture += '    +' + '--' * size + '\n'
    picture += '     ' + ''.join(f'{x:<2}' for x in range(size))

    print('y = |x|')
    print(picture)
def sequence_analysis():
    file = open('sequence.txt', '')

    numbers = []

    for number in file:
        numbers.append(float(number))

    file.close()

    print("Numbers:", numbers)

    even = []

    for i in range(len(numbers)):
        if i % 2 == 0:
            even.append(abs(numbers[i]))

    odd = []

    for i in range(len(numbers)):
        if i % 2 != 0:
            odd.append(abs(numbers[i]))

    print("Even positions:", even)
    print("Odd positions:", odd)
    even_average = sum(even) / len(even)
    odd_average = sum(odd) / len(odd)
    print("Average of even positions:", even_average)
    print("Average of odd positions:", odd_average)
def flag():
    pixel = '    '
    length = 10

    # Top red stripe
    for i in range(2):
        print(RED + pixel * length + RESET)

    # Thin white stripe
    print(WHITE + pixel * length + RESET)

    # Bottom red stripe
    for i in range(2):
        print(RED + pixel * length + RESET)


animation()
pattern()
graph()
sequence_analysis()
flag()
