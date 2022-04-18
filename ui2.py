from multiprocessing.connection import wait
import os
from time import sleep
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
        self.create_menu(self.args,"1")

        # # draw menu
        # item_number = 0
        # for arg in self.args:
        #     item_number += 1
        #     if(item_number == arg.arg_place):
        #         if(isinstance(arg, VariableArgument)):
        #             print(str(arg.arg_place)+". set "+arg.arg_name)
        #         elif(isinstance(arg, MenuItem)):
        #             print(str(arg.menu_place)+". set "+arg.menu_name)
        #         elif(isinstance(arg, FunctionArgument)):
        #             print(str(arg.arg_place)+". "+arg.function_name)

        # # wait for keypress and take action accordingly
        # to_loop = True
        # while to_loop:
        #     key_pressed = keyboard.read_key()
        #     if(key_pressed.isnumeric() and int(key_pressed) <= len(self.args) and int(key_pressed) > 0):
        #         for arg in self.args:
        #             if(int(key_pressed) == arg.arg_place):
        #                 if(isinstance(arg, VariableArgument)):
        #                     to_loop = False
        #                     # open sub menu
        #                     break
        #                 elif(isinstance(arg, MenuItem)):
        #                     to_loop = False
        #                     break
        #                 elif(isinstance(arg, FunctionArgument)):
        #                     to_loop = False
        #                     arg.function()
        #                     break
        # print()
        # print("press any key To continue...")
        # keyboard.read_key()
        
        # redraw menu
        # self.main_menu()

    def create_menu(self, args,a):
        os.system("cls")
        self.print_logo()

        # draw menu
        item_number = 0
        for arg in args:
            item_number += 1
            if(item_number == arg.arg_place):
                if(isinstance(arg, VariableArgument)):
                    print(str(arg.arg_place)+". set "+arg.arg_name)
                elif(isinstance(arg, MenuItem)):
                    print(str(arg.arg_place)+". set "+arg.menu_name)
                elif(isinstance(arg, FunctionArgument)):
                    print(str(arg.arg_place)+". "+arg.function_name)

        # wait for keypress and take action accordingly
        to_loop = True
        sleep(10)
        print("ready")
        while to_loop:
            key_pressed = keyboard.read_key()
            print(key_pressed)
            if(key_pressed.isnumeric() and int(key_pressed) <= len(args) and int(key_pressed) > 0):
                for arg in args:
                    if(int(key_pressed) == arg.arg_place):
                        if(isinstance(arg, VariableArgument)):
                            to_loop = False
                            print("a")
                            arg.update_function()
                            break
                        elif(isinstance(arg, MenuItem)):
                            to_loop = False
                            print("b")
                            self.create_menu(arg.sub_menu_items,"2")
                            break
                        elif(isinstance(arg, FunctionArgument)):
                            to_loop = False
                            print("c")
                            arg.function()
                            break
        print()
        print(a,"press any key To continue...")
        keyboard.read_key()

        return

    def update_var(self):
        pass

class MenuItem:
    def __init__(self,menu_name ,*sub_menu_items, arg_place=-1):
        self.menu_name = menu_name
        self.sub_menu_items = sub_menu_items
        self.arg_place = arg_place


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