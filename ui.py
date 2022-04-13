import this
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
    def __init___(self, update_function=default_update_function):
        self.root = Tk()
        self.root.withdraw()
        self.origin_folder = ""
        self.rules = []
        self.update_function = update_function

    def start(self):
        os.system("cls")
        self.select_origin_folder()
        # while(self.origin_folder == ""):
        # test
        destenation_folder = self.select_destenation_folder()
        self.rules = Rule.create_default_rules(Rule.get_file_types_list(self.origin_folder), destenation_folder)
        self.check_settings()

    def select_origin_folder(self):
        os.system("cls")
        print("please select origin folder")
        self.origin_folder = filedialog.askdirectory()
    
    def select_destenation_folder(self):
        os.system("cls")
        print("please select destenation folder")
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
                destenation_folder = self.select_destenation_folder
                self.rules = Rule.create_default_rules(Rule.get_file_types_list(self.origin_folder), destenation_folder)
            case "2":
                self.rules = self.create_custom_rules()

    def create_custom_rules(self):
        pass

    def check_settings(self):
        print("you want to move file from: "+self.origin_folder)
        for rule in self.rules:
            print(f'all file with the extantion "{rule.extantion}" to: "{rule.destination}"')
        print()
        print("are you sure you want to continue?")
        action = input("Y/N:")

    def sort(self):
        file_list = File.create_file_list(self.origin_folder)
        sorter = Sorter(file_list,self.rules,self.updateFunction)
        sorter.copy()
