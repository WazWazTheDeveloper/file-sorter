import os

def get_file_types_list(path):
    file_types = set()
    file_list = os.listdir(path)

    for file_name in file_list:
        file_extention = file_name.split(".")[-1]
        file_types.add("."+file_extention)

    return(file_types)

def move_files_to_dir():
    

def test():
    path = "C:/Users/Daniel/Desktop/100CANON"

    print(get_file_types_list(path))

if __name__ == "__main__" :
    test()