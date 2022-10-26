class Writters:
    def __init__(self, name, id, section):
        self.name = name
        self.id = id
        self.section = section

class HeadOfWritters(Writters):
    def __init__(self, name, id, section, writters_list):
        super().__init__(name, id, section)
        self.writters = writters_list
        