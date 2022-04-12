from cmath import log
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
    destPath = "C:/Users/Daniel/Desktop/סמחט"
    originPath = "C:/Users/Daniel/Desktop/CLIP"
    file_list = File.create_file_list(originPath)
    rules = Rule.create_default_rules(Rule.get_file_types_list(originPath), destPath)
    for rule in rules :
        print(rule.extantion)
        print(rule.destination)
    # rules = []
    # rule1 = Rule.create_rule("CR2", "C:/Users/Daniel/Desktop/סמחטa/CR2")
    # rule2 = Rule.create_rule("JPG", "C:/Users/Daniel/Desktop/סמחטa/JPG")
    # rule3 = Rule.create_rule("ARW", "C:/Users/Daniel/Desktop/סמחטa/ARW")
    # rules.append(rule1)
    # rules.append(rule2)
    # rules.append(rule3)
    b = Sorter(file_list,rules,updateStatus)
    b.copy()

if __name__ == "__main__":
    doit()
