import os
import shutil
from rule import Rule

class Sorter:
    def __init__(self, rules, files_list):
        self.files_list = files_list
        self.rules = rules
        self.files_to_move = len(files_list)
        self.files_moved = 0

    def copy(self):
        pass

    def move(self):
        '''
        moves all files with certain extantion to destination directory
        :param files_directory: the directory from which files will be copied
        :param destination_directory: the destination directory to which files will be copied
        :param files_extention: file extantion type(like "JPG")
        '''
        for index, file in enumerate(self.files_list):
            for rule in self.rules:
                if file.extantion == rule.extantion:
                    current_rule = rule

            if not os.path.exists(current_rule.destination):
                os.makedirs(current_rule.destination)

            shutil.move(file.path, current_rule.destination)
            self.file_moved()
            print(f'done {self.files_moved} of {self.files_to_move}')
    
    def file_moved(self):
        self.files_moved += 1
    
