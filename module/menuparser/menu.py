import openpyxl
from openpyxl import load_workbook

#temporary way to acces the file necessary to extrapoalte the menù
MENU_PATH = 'Menù settimanale pranzo.xlsx'

KEY_COLUMN = {1 : "B", 2 : "C" , 3 : "D" , 4 :  "E", 5 : "F" , 6 : "G", 7 : "H"}

#pass the menu of choice to open it
def open_menu(menu_name:str) -> openpyxl.worksheet.worksheet.Worksheet:

    menu_table = load_workbook(filename = menu_name)
    menu_table = menu_table.active

    return menu_table

#these functions returns the menu from the chosen day

def extrapolate_menu(w_s: openpyxl.worksheet.worksheet.Worksheet, table_colum:  int) -> list:

    menu_of_the_day = []
    table_char = KEY_COLUMN[table_colum]


    for i in range (4, 15):
        i_str = str(i)
        current_course = w_s[table_char + i_str].value
        menu_of_the_day.append(current_course)



    return menu_of_the_day

def scroll_table(w_s , day:int) -> list:
    match day:

        case 1:
            menu_of_the_day = extrapolate_menu(w_s, day)

        case 2:
            menu_of_the_day = extrapolate_menu(w_s, day)

        case 3:
            menu_of_the_day = extrapolate_menu(w_s, day)

        case 4:
            menu_of_the_day = extrapolate_menu(w_s, day)

        case 5:
            menu_of_the_day = extrapolate_menu(w_s, day)

        case 6:
            menu_of_the_day = extrapolate_menu(w_s, day)

        case 7:
            menu_of_the_day = extrapolate_menu(w_s, day)

        case _:
            return "ERROR the day selected doesn't exist"

    return menu_of_the_day


#fucntion for testing

def print_function(menu_list: list) -> None:
    for i in range(len(menu_list)):
        print(menu_list[i])


#Calls to the functions for testing
table = open_menu(MENU_PATH)
menu = scroll_table(table, 1)

print_function(menu)
