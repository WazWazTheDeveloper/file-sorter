from cgi import print_directory
from cmath import log
from importlib.metadata import files
import os
import shutil
from tokenize import String
from rule import Rule
from file import File
from sorter import Sorter

files_to_move, files_moved = 0, 0

def file_moved():
    global files_moved
    files_moved += 1


def get_file_types_list(path):
    '''
    gets the file extantions types in certain directory
    :param path: path of folder
    '''
    file_types = set()
    file_list = os.listdir(path)

    for file_name in file_list:
        file_extention = file_name.split(".")[-1]
        if ('.' in file_name):
            file_types.add(file_extention)

    return(file_types)


def move_files_to_dir(origin_directory, destination_directory, files_extention):
    '''
    moves all files with certain extantion to destination directory
    :param files_directory: the directory from which files will be moved
    :param destination_directory: the destination directory to which files will be moved
    :param files_extention: file extantion type(like "JPG")
    '''

    files_list = list(filter(lambda file_name: check_extantion(
        file_name, files_extention), os.listdir(origin_directory)))

    if not os.path.exists(destination_directory):
        os.makedirs(destination_directory)

    for index, file in enumerate(files_list):
        file_dir = origin_directory
        if file_dir[-1] == '/':
            file_dir += file
        else:
            file_dir = file_dir + '/' + file

        shutil.move(file_dir, destination_directory)
        file_moved()
        print(f'done {files_moved} of {files_to_move}')


def copy_files_to_dir(origin_directory, destination_directory, files_extention):
    '''
    moves all files with certain extantion to destination directory
    :param files_directory: the directory from which files will be copied
    :param destination_directory: the destination directory to which files will be copied
    :param files_extention: file extantion type(like "JPG")
    '''
    files_list = list(filter(lambda file_name: check_extantion(
        file_name, files_extention), os.listdir(origin_directory)))
    if not os.path.exists(destination_directory):
        os.makedirs(destination_directory)
    for index, file in enumerate(files_list):
        file_dir = origin_directory
        if file_dir[-1] == '/':
            file_dir += file
        else:
            file_dir = file_dir + '/' + file
        shutil.copy2(file_dir, destination_directory)
        file_moved()
        print(f'done {files_moved} of {len(files_to_move)}')


def count_files_of_extention(files_directory, files_extention):
    '''
    count the amount of files with certain extantion in a directory
    :param files_directory: directory to check
    :param files_extention: extention to be checked
    '''
    count = 0
    files_list = os.listdir(files_directory)
    for file in files_list:
        file_extention = file.split(".")[-1]
        if(files_extention == file_extention and '.' in file):
            count += 1
    return count


def check_extantion(file_name, file_extention):
    '''
    check if a file name have a certaion extantion
    :param file_name: name of the file
    :param file_extention: extention to be checked
    '''
    if file_name.split(".")[-1] == file_extention and '.' in file_name:
        return True
    return False


def test():
    global files_to_move
    files_to_move = 0
    path = "C:/Users/Daniel/Desktop/100CANON"
    path2 = "C:/Users/Daniel/Desktop/a"
    rules = Rule.create_default_rules(get_file_types_list(path), path)
    for rule in rules:
        print(rule.extantion,rule.origin,count_files_of_extention(rule.origin, rule.extantion))
        files_to_move += count_files_of_extention(rule.origin, rule.extantion)
    for rule in rules:
        move_files_to_dir(rule.origin, rule.destination, rule.extantion)

def test2():
    a = File.create_file_list("C:/Users/Daniel/Desktop/100CANON")
    path = "C:/Users/Daniel/Desktop/100CANON"
    rules = Rule.create_default_rules(get_file_types_list(path), path)
    b = Sorter(rules,a)
    b.move()

if __name__ == "__main__":
    test2()
