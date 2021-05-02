from random import *
import PySimpleGUI as pg

# GUI

size = randint(8, 16)
pg.theme('Reddit')
layout = [
    [pg.Text("Place that will be used: "), pg.Input(key="place")],
    [pg.Text(key="output", size=(size+10,0))],
    [pg.Button('Generate')]
]

def shuffle_pass(string):
    tempList = list(string)
    shuffle(tempList)
    return ''.join(tempList)

def Generate():
    symbols = [64,37,43,47,92,39,33,35,36,94,63,58,46,40,41,123,125,91,93,126,96,45,95]
    result = ""
    i = 0

    symbol_count = 0
    lower_letter_count = 0
    upper_letter_count = 0
    number_count = 0

    _: int = 9
    objects = []
    while i <= size:
        # if _ in objects:
        #     if _ == objects[3]:
        #         if _ not in symbols:
        #             i -= 1

        lower_letter = randint(97, 122)
        upper_letter = randint(65, 90)
        number = randint(48, 57)
        symbol = randint(0, 191)
        objects = [lower_letter, upper_letter, number, symbol]

        _ = objects[randint(0, 3)]
        
        __ = False
        while not __:
            if _ == objects[0] and lower_letter_count <= (size/4):
                lower_letter_count += 1
                result += str(chr(_))
                __ = True

            elif _ == objects[1] and upper_letter_count <= (size/4):
                upper_letter_count += 1
                result += str(chr(_))
                __ = True

            elif _ == objects[2] and number_count <= (size/4):
                number_count += 1
                result += str(chr(_))
                __ = True

            elif _ == objects[3] and symbol_count <= (size/4):
                if symbol in symbols:
                    result += str(chr(_))
                    __ = True
                else:
                    lower_letter = randint(97, 122)
                    upper_letter = randint(65, 90)
                    number = randint(48, 57)
                    symbol = randint(0, 191)
                    objects = [lower_letter, upper_letter, number, symbol]

            else:
                _ = objects[randint(0, 3)]

        i+=1

    return result

def save(text):
    with open("Passwords.txt", "a") as f:
        f.write(text)
        f.close()

window = pg.Window('Password Generator', layout, resizable=True)

while True:
    event, values = window.read()
    
    if event == pg.WIN_CLOSED:
        break
    if event == 'Generate':
        final = shuffle_pass(Generate())
        window['output'].update(final)
        save("Place/Location: {0} \nPassword: {1} \n\n".format(values['place'], final))


window.close()
    
