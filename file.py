import os

class File:
    def __init__(self, name, extantion, path):
        self.name = name
        self.extantion = extantion
        self.path = path

    def create_file_list(path):
        directory_file_list = os.listdir(path)
        file_list = []

        for file in directory_file_list:
            if ('.' in file):
                file_name = file.split('.')[0]
                file_extantion = file.split('.')[-1]
                if path[-1] == '/':
                    file_path = path + file
                else:
                    file_path = path + '/' + file
                file_list.append(File(file_name, file_extantion, file_path))

        return file_list
