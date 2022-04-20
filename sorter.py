import os
import shutil
from rule import Rule
from pathlib import Path

class Sorter:
    def __init__(self, files_list, rules, update_function=-1):
        self.files_list = files_list
        self.rules = rules
        self.files_moved = 0
        self.update_function = update_function

    def copy(self):
        '''
        copy all files with certain extantion to destination directory
        :param files_directory: the directory from which files will be copied
        :param destination_directory: the destination directory to which files will be copied
        :param files_extention: file extantion type(like "JPG")
        '''
        self.files_to_move = len(self.files_list)
        for index, file in enumerate(self.files_list):
            current_rule = "/"
            for rule in self.rules:
                if file.extantion == rule.extantion:
                    current_rule = rule
            if current_rule.destination != "/" and current_rule.destination != "":
                if not os.path.exists(current_rule.destination):
                    os.makedirs(current_rule.destination)

                shutil.copy2(file.path, current_rule.destination)
                self.file_moved()
                if(self.update_function != -1):
                    self.update_function(self.files_moved, self.files_to_move)

        return

    def move(self):
        '''
        moves all files with certain extantion to destination directory
        :param files_directory: the directory from which files will be copied
        :param destination_directory: the destination directory to which files will be copied
        :param files_extention: file extantion type(like "JPG")
        '''
        self.files_to_move = len(self.files_list)
        for index, file in enumerate(self.files_list):
            for rule in self.rules:
                if file.extantion == rule.extantion:
                    current_rule = rule
            if rule.destination != "/" and rule.destination != "":
                if not os.path.exists(current_rule.destination):
                    os.makedirs(current_rule.destination)

                shutil.move(file.path, current_rule.destination)
                self.file_moved()
                if(self.update_function != -1):
                    self.update_function(self.files_moved, self.files_to_move)

        return

    def file_moved(self):
        self.files_moved += 1