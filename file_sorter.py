from rule import Rule
from file import File
from sorter import Sorter
from ui import VariableArgument, FunctionArgument, Ui, MenuItem
import os


def default_update_function(files_moved, files_to_move):
    os.system("cls")
    dots = int(files_moved / 8) % 4 + 1
    dot_string = ""
    for i in range(dots):
        dot_string += "."
    print("moving file"+dot_string)
    print(
        f'done {files_moved} of {files_to_move}, ({round(files_moved/files_to_move*1000)/10}%)')


def logo_function():
    print(f'___________.__.__                     _________              __                ')
    print(f'\_   _____/|__|  |   ____            /   _____/ ____________/  |_  ___________ ')
    print(f' |    __)  |  |  | _/ __ \   ______  \_____  \ /  _ \_  __ \   __\/ __ \_  __ \\')
    print(f' \___  /   |__|____/\___  >         /_______  /\____/|__|   |__|  \___  >__|   ')
    print(f'     \/                 \/                  \/                        \/       ')
    print()
    print()
    print()


def update():
    pass


def create_default_rules(_rules, origin_folder, destination_folder):
    destination_folder.arg_value = Ui.get_folder()
    if destination_folder.arg_value is not "":
        _rules.clear()
        _rules += Rule.create_default_rules(Rule.get_file_types_list(
            origin_folder.arg_value), destination_folder.arg_value)
        return None


def add_rules_to_menu(rules_custom, origin_folder,_rules,file_list):
    file_list.clear()
    file_list += File.create_file_list(origin_folder.arg_value)

    _rules.clear()
    rules_custom.clear()
    extension_list = Rule.get_file_types_list(origin_folder.arg_value)
    for i, extension in enumerate(extension_list):
        rule = Rule(extension,'/')
        _rules.append(rule)

    a = 0
    for rule in _rules:
        menuItem = VariableArgument(f'set {rule.extantion} path', rule, (lambda rule=rule : update_rule_destenation(rule)),show_value=lambda rule=rule :(rule.destination+ " " +rule.extantion), arg_place=(a+1), to_show=True)
        rules_custom.add_menu_item(menuItem)
        a+=1

def update_rule_destenation(rule):
    rule.destination = Ui.get_folder()
    return None

if __name__ == "__main__":
    _rules = []
    file_list = []
    sorter = Sorter(file_list, _rules, default_update_function)
    origin_folder = VariableArgument(
        "origin folder", "", Ui.get_folder, post_update_function= lambda: add_rules_to_menu(rules_custom, origin_folder,_rules,file_list), arg_place=1)
    destination_folder = VariableArgument(
        "destination folder", "",  Ui.get_folder, arg_place=2)
    rules_custom = MenuItem("create custom rules", arg_place=2)
    rules_default = VariableArgument("set defalut rules", _rules, lambda: create_default_rules(
        _rules, origin_folder, destination_folder), arg_place=1, to_show=False)
    
    copy = FunctionArgument("copy files", sorter.copy, arg_place=3)
    move = FunctionArgument("move files", sorter.move, arg_place=4)

    rules_menu = MenuItem("rules", arg_place=2)
    rules_menu.add_menu_item(rules_default)
    rules_menu.add_menu_item(rules_custom)

    ui = Ui(logo_function=logo_function)
    ui.add_arg(origin_folder)
    ui.add_arg(rules_menu)
    ui.add_arg(copy)
    ui.add_arg(move)
    ui.start()
