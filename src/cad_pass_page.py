# region [IMPORTS]

from tkinter import Tk, Label, Entry, Button
from random import randint, shuffle
from string import ascii_lowercase, ascii_uppercase, digits, punctuation
from src.database_conn import insert

# endregion

# region [GLOBAL VARIABLES]

password: str = ''
name: str = ''
login: str = ''
name_input: Entry
login_input: Entry
pass_input: Entry
root: Tk

# endregion

# region [FUNCTIONS]


def generate_password() -> None:
    global password

    passwd: str = ''
    n: int = 0
    while n < 4:
        passwd += ascii_lowercase[randint(0, len(ascii_lowercase)-1)]
        passwd += ascii_uppercase[randint(0, len(ascii_uppercase)-1)]
        passwd += digits[randint(0, len(digits)-1)]
        passwd += punctuation[randint(0, len(punctuation)-1)]

        n += 1

    shuffle(list(passwd))
    password = ''.join(passwd)


def submit() -> None:
    global name, login, password

    name = name_input.get()
    login = login_input.get()

    if pass_input.get() not in ('', None):
        password = pass_input.get()

    insert(name, login, password)

    root.destroy()


# endregion

# region [WINDOW HANDLER]

def start_cad_loop() -> None:
    global name_input, login_input, pass_input, root

    root = Tk()
    name_label = Label(root, text='Name:')
    name_label.grid(row=0, column=0, columnspan=2)
    name_input = Entry(root, textvariable=name)
    name_input.grid(row=1, column=0, columnspan=2)

    login_label = Label(root, text='Login:')
    login_label.grid(row=2, column=0, columnspan=2)
    login_input = Entry(root, textvariable=login)
    login_input.grid(row=3, column=0, columnspan=2)

    pass_label = Label(root, text='Password:')
    pass_label.grid(row=4, column=0, columnspan=2)
    pass_input = Entry(root, textvariable=password)
    pass_input.grid(row=5, column=0, columnspan=2)

    pass_gen = Button(root, text='Generate', command=generate_password)
    pass_gen.grid(row=6, column=1)
    submit_btn = Button(root, text='Submit', command=submit)
    submit_btn.grid(row=6, column=0)
    root.mainloop()


# endregion


if __name__ == '__main__':
    start_cad_loop()
