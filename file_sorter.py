from ui import Ui
from rule import Rule
from file import File
from sorter import Sorter
from ui2 import VariableArgument,FunctionArgument,Ui2
import os

def default_update_function(files_moved, files_to_move):
    os.system("cls")
    dots = int(files_moved / 8) % 4 + 1
    dot_string = ""
    for i in range(dots):
        dot_string += "."
    print("moving file"+dot_string)
    print(f'done {files_moved} of {files_to_move}, ({round(files_moved/files_to_move*1000)/10}%)')

def logo_function():
    print(f'___________.__.__                     _________              __                ')
    print(f'\_   _____/|__|  |   ____            /   _____/ ____________/  |_  ___________ ')
    print(f' |    __)  |  |  | _/ __ \   ______  \_____  \ /  _ \_  __ \   __\/ __ \_  __ \\')
    print(f' \___  /   |__|____/\___  >         /_______  /\____/|__|   |__|  \___  >__|   ')
    print(f'     \/                 \/                  \/                        \/       ')
    print()
    print()
    print()

if __name__ == "__main__":
    # ui = Ui()
    # ui.start()
    
    origin_folder = VariableArgument("origin folder","C:/Users/Daniel/Desktop/100CANON/JPG" ,1)
    destination_folder = VariableArgument("destination folder","C:/Users/Daniel/Desktop/100CANON/JPG/1",2)
    _rules = Rule.create_default_rules(Rule.get_file_types_list(origin_folder.arg_value), destination_folder.arg_value)
    rules = VariableArgument("rules",_rules,3)

    file_list = File.create_file_list(origin_folder.arg_value)
    sorter = Sorter(file_list,rules.arg_value,default_update_function)
    copy = FunctionArgument("copy files",sorter.copy,4)
    move = FunctionArgument("move files",sorter.copy,5)

    ui = Ui2(origin_folder,destination_folder,rules,copy,move,logo_function=logo_function)
    ui.start()
