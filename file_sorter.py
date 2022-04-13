from tkinter import filedialog
from tkinter import *
from turtle import clear
import os

from ui import Ui
from rule import Rule
from file import File
from sorter import Sorter



def test2():
    a = File.create_file_list("C:/Users/Daniel/Desktop/100CANON")
    path = "C:/Users/Daniel/Desktop/100CANON"
    # rules = Rule.create_default_rules(Rule.get_file_types_list(path), path)
    rules = []
    rule1 = Rule.create_rule("CR2", "C:/Users/Daniel/Desktop/100CANON/boob")
    rule2 = Rule.create_rule("JPG", "C:/Users/Daniel/Desktop/100CANON/boobs")
    rules.append(rule1)
    rules.append(rule2)
    b = Sorter(a,rules,updateStatus)
    b.move()

def updateStatus(files_moved, files_to_move):
    print(f'done {files_moved} of {files_to_move}, ({round(files_moved/files_to_move*1000)/10}%)')

def doit():
    destPath = "C:/Users/Daniel/Desktop/shami-bi"
    originPath = "C:/Users/Daniel/Desktop/סמחט/a"
    file_list = File.create_file_list(originPath)
    rules = Rule.create_default_rules(Rule.get_file_types_list(originPath), destPath)
    # rules = []
    # rule1 = Rule.create_rule("CR2", "C:/Users/Daniel/Desktop/סמחטa/CR2")
    # rule2 = Rule.create_rule("JPG", "C:/Users/Daniel/Desktop/סמחטa/JPG")
    # rule3 = Rule.create_rule("ARW", "C:/Users/Daniel/Desktop/סמחטa/ARW")
    # rules.append(rule1)
    # rules.append(rule2)
    # rules.append(rule3)
    b = Sorter(file_list,rules,updateStatus)
    b.copy()

def test3():
    root = Tk()
    root.withdraw()
    os.system("cls")
    print("please select origin folder")
    origin_folder = filedialog.askdirectory()
    print(origin_folder)
    print("please select destenation folder")
    destenation_folder = filedialog.askdirectory()

    file_list = File.create_file_list(origin_folder)
    rules = Rule.create_default_rules(Rule.get_file_types_list(origin_folder), destenation_folder)

    sorter = Sorter(file_list,rules,updateStatus)
    os.system("cls")
    print("please select an action")
    print("1. copy")
    print("2. move")
    action = input("action: ")
    if (action == "1"):
        sorter.copy()
    elif(action == "2"):
        sorter.move()
    


if __name__ == "__main__":
    ui = Ui()
    ui.start()
