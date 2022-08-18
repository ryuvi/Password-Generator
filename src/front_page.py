# region [IMPORTS]

from tkinter import Tk, Listbox, Frame, Button, StringVar
from src.cad_pass_page import start_cad_loop
from src.database_conn import select_all, select_especific

# endregion

# region [VARIABLES]

root = Tk()

# endregion

# region [FUNCTIONS]


def select_loc(evt) -> None:
    global usr_pass

    selected_item = location_list.curselection()
    value = location_list.get(selected_item)
    login, passwd = select_especific(value[0])

    usr_pass.set([f'Login: {login}', f'Password: {passwd}'])


# endregion

# region [LOCATION]
loc_list_frame = Frame(root).grid(row=0, column=0)
location_list = Listbox(loc_list_frame, bg='#fff', selectmode='browse')
location_list.bind('<<ListboxSelect>>', select_loc)
location_list.grid(row=0, column=0, columnspan=2)

locations = StringVar(value=select_all())

location_list.config(listvariable=locations)

# endregion

# region [USER - PASS]

usr_pass_frame = Frame(root).grid(row=0, column=2)
usr_pass_list = Listbox(usr_pass_frame, bg='#fff')
usr_pass_list.grid(row=0, column=2, columnspan=3)

usr_pass = StringVar(value=[])

usr_pass_list.config(listvariable=usr_pass)

# endregion

# region [BUTTONS]

btn_frame = Frame(loc_list_frame).grid(row=1, column=0, columnspan=2)
add_btn = Button(btn_frame, text='+', command=start_cad_loop)
add_btn.grid(row=1, column=0, columnspan=2, sticky='e', padx=35)

rem_btn = Button(btn_frame, text='-')
rem_btn.grid(row=1, column=1, sticky='e')

# endregion

# region [FUNCTIONS]


def start_main_loop() -> None:
    root.mainloop()


def stop_main_loop() -> None:
    root.destroy()


# endregion

if __name__ == '__main__':
    root.mainloop()
