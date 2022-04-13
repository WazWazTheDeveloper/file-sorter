from operator import truediv
from tkinter import filedialog
from tkinter import *
import os

from rule import Rule
from file import File
from sorter import Sorter

def default_update_function(files_moved, files_to_move):
    os.system("cls")
    print(f'done {files_moved} of {files_to_move}, ({round(files_moved/files_to_move*1000)/10}%)')

class Ui:
    def __init__(self, update_function=default_update_function):
        self.root = Tk()
        self.root.withdraw()
        self.origin_folder = ""
        self.rules = []
        self.update_function = update_function

    def start(self):
        os.system("cls")
        check_to_continue = True
        while(check_to_continue):
            while(self.origin_folder == ""):
                self.select_origin_folder()
            self.select_rule_type()
            check_to_continue = not self.check_settings()
        self.sort()

    def select_origin_folder(self):
        os.system("cls")
        print("please select origin folder")
        self.origin_folder = filedialog.askdirectory()
    
    def select_destination_folder(self):
        print("please select destination folder")
        return filedialog.askdirectory()

    def select_rule_type(self):
        rule_type = -1
        os.system("cls")
        print("please select what action you want to do:")
        print("1: use defalut rules for sorting")
        print("2. use custom rule for sorting")
        rule_type = input("you action:")
        match rule_type:
            case "1":
                destination_folder = self.select_destination_folder()
                self.rules = Rule.create_default_rules(Rule.get_file_types_list(self.origin_folder), destination_folder)
            case "2":
                self.rules = self.create_custom_rules()

    def create_custom_rules(self):
        rule_list = []
        extensions = Rule.get_file_types_list(self.origin_folder)
        for extension in extensions:
            print(f'please select destination folder for files with the extention ".{extension}"')
            destination_folder = filedialog.askdirectory()
            print(f'you selected "{destination_folder}"')
            rule = Rule(extension, destination_folder)
            rule_list.append(rule)
        self.rules=rule_list

    def check_settings(self):
        os.system("cls")
        print("you want to move file from: "+self.origin_folder)
        for rule in self.rules:
            print(f'all file with the extantion "{rule.extantion}" will move to: "{rule.destination}"')
        print()
        print("are you sure you want to continue?")
        action = input("Y/N:")
        if (action == "Y" or action =="y"):
            return True
        return False

    def sort(self):
        file_list = File.create_file_list(self.origin_folder)
        sorter = Sorter(file_list,self.rules,self.update_function)
        print("please select what action you want to do:")
        print("1: move all files to new location")
        print("2: copy all files to new location")
        action = input()
        match action :
            case "1":
                sorter.move()
            case "2":
                sorter.copy()
                
