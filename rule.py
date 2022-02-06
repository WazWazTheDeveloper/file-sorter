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
