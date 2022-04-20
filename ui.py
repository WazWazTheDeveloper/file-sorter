from multiprocessing.connection import wait
from operator import truediv
import os
import keyboard
from tkinter import filedialog
from tkinter import *

class Ui:
    def __init__(self, logo_function=lambda *args: None):
        self.root = Tk()
        self.root.withdraw()
        self.args = []
        self.arg_count = 0
        self.logo_function = logo_function

    def wait_for_key_to_depress(self, key):
        # wait for key to be depressed
        while(key != "" and keyboard.is_pressed(key)):
            pass
        
    def start(self):
        self.main_menu()

    def print_logo(self):
        self.logo_function()

    def main_menu(self):
        os.system("cls")
        self.create_menu(self.args, "",show_back_button=False)

    def create_menu(self, args, prev_key, show_back_button=True):
        os.system("cls")
        self.print_logo()

        # draw menu
        item_number = 0
        for arg in args:
            item_number += 1
            if(item_number == arg.arg_place):
                if(isinstance(arg, VariableArgument)):
                    value = ""
                    if(arg.to_show):
                        if(arg.show_value() != True):
                            value = f'({arg.show_value()})'
                        else:
                            value = f'({arg.arg_value})'

                    print(f'{str(arg.arg_place)}. {arg.arg_name} {value}')
                elif(isinstance(arg, MenuItem)):
                    print(str(arg.arg_place)+". "+arg.menu_name)
                elif(isinstance(arg, FunctionArgument)):
                    print(str(arg.arg_place)+". "+arg.function_name)
        
        # show back button
        if(show_back_button):
            print(f'{item_number+1}. go back to previous menu')

        # wait for keypress and take action accordingly
        to_loop = True
        while to_loop:
            # wait for key to be depressed
            self.wait_for_key_to_depress(prev_key)

            key_pressed = keyboard.read_key()

            # back button
            if(show_back_button and key_pressed.isnumeric() and int(key_pressed) == item_number+1):
                self.wait_for_key_to_depress(key_pressed)
                return

            elif(key_pressed.isnumeric() and int(key_pressed) <= len(args) and int(key_pressed) > 0):
                for arg in args:
                    if(int(key_pressed) == arg.arg_place):
                        if(isinstance(arg, VariableArgument)):
                            to_loop = False
                            newval = arg.update_function()
                            if newval is not None:
                                arg.arg_value = newval
                            arg.post_update_function()
                            self.wait_for_key_to_depress(key_pressed)
                            self.create_menu(args, key_pressed,show_back_button)
                            # return
                            break
                        elif(isinstance(arg, MenuItem)):
                            to_loop = False
                            self.wait_for_key_to_depress(key_pressed)
                            self.create_menu(arg.sub_menu_items, key_pressed)
                            self.create_menu(args, key_pressed, show_back_button)
                            break
                        elif(isinstance(arg, FunctionArgument)):
                            to_loop = False
                            arg.function()
                            break

        return

    def add_arg(self, arg):
        if(isinstance(arg, VariableArgument)):
            pass
        elif(isinstance(arg, MenuItem)):
            pass
        elif(isinstance(arg, FunctionArgument)):
            pass

        self.arg_count += 1
        self.args.append(arg)
        return self

    def get_folder():
        return filedialog.askdirectory()


class MenuItem:
    def __init__(self, menu_name, *sub_menu_items, arg_place=-1):
        self.menu_name = menu_name
        self.sub_menu_items = sub_menu_items
        self.arg_count = len(sub_menu_items)
        self.arg_place = arg_place

    def __init__(self, menu_name, arg_place=-1):
        self.menu_name = menu_name
        self.sub_menu_items = []
        self.arg_count = 0
        self.arg_place = arg_place

    def add_menu_item(self, arg):
        self.arg_count += 1
        self.sub_menu_items.append(arg)

        return self

    def clear(self):
        self.arg_count = 0
        self.sub_menu_items.clear()

        return self


class VariableArgument:
    def __init__(self, arg_name, arg_value, update_function, post_update_function = lambda *args: None,show_value = lambda: True, arg_place=-1 , to_show=True):
        self.arg_name = arg_name
        self.arg_value = arg_value
        self.arg_place = arg_place
        self.update_function = update_function
        self.post_update_function = post_update_function
        self.show_value = show_value
        self.to_show = to_show


class FunctionArgument:
    def __init__(self, function_name, function, arg_place=-1):
        self.function_name = function_name
        self.function = function
        self.arg_place = arg_place
