import os

class Rule:
    def __init__(self, extantion, origin, destination):
        self.extantion = extantion
        self.origin = origin
        self.destination = destination

    def create_default_rules(extantion_list, path):
        rule_list = []
        for extantion in extantion_list:
            if path[-1] == '/':
                new_rule = Rule(extantion, path, path + extantion)
            else:
                new_rule = Rule(extantion, path + '/', path + '/' + extantion)
            rule_list.append(new_rule)

        return rule_list

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