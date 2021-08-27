class ConvertionProtocol:
    def __init__(self):
        self.roman_dictionary = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

    def roman_to_int(self):
        return 'you want to convert a roman to an integer'

    def int_to_roman(self):
        return 'you want to convert a roman to an integer'

    def treat(self, command, to_convert):
        if(command == 'roman'):
            return self.roman_to_int()
        elif(command == 'int'):
            return self.int_to_roman()
