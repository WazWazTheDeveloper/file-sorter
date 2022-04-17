import os
from tkinter import filedialog
from tkinter import *
import keyboard


class Ui2:
    def __init__(self, *args, logo_function=lambda *args: None):
        self.root = Tk()
        self.root.withdraw()
        self.args = args
        self.logo_function = logo_function

    def start(self):
        self.main_menu()

    def print_logo(self):
        self.logo_function()

    def main_menu(self):
        os.system("cls")
        self.print_logo()

        # draw menu
        item_number = 0
        for arg in self.args:
            item_number += 1
            if(item_number == arg.arg_place):
                if(isinstance(arg, VariableArgument)):
                    print(str(arg.arg_place)+". set "+arg.arg_name)
                if(isinstance(arg, FunctionArgument)):
                    print(str(arg.arg_place)+". "+arg.function_name)

        # wait for keypress and take action accordingly
        to_loop = True
        while to_loop:
            key_pressed = keyboard.read_key()
            if(key_pressed.isnumeric() and int(key_pressed) <= len(self.args) and int(key_pressed) > 0):
                for arg in self.args:
                    if(int(key_pressed) == arg.arg_place):
                        if(isinstance(arg, VariableArgument)):
                            to_loop = False
                            # open sub menu
                            break
                        if(isinstance(arg, FunctionArgument)):
                            to_loop = False
                            arg.function()
                            break
        print()
        print("press any key To continue...")
        keyboard.read_key()
        
        # redraw menu
        self.main_menu()

    def create_sub_menu(self):
        os.system("cls")

    def update_var(self):
        pass


class VariableArgument:
    def __init__(self, arg_name, arg_value, update_function, arg_place=-1):
        self.arg_name = arg_name
        self.arg_value = arg_value
        self.arg_place = arg_place
        self.update_function = update_function


class FunctionArgument:
    def __init__(self, function_name, function, arg_place=-1):
        self.function_name = function_name
        self.function = function
        self.arg_place = arg_place
