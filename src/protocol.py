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

    def roman_to_int(self, to_convert):
        try:
            for n in range(len(to_convert)):
                if to_convert[n] in self.roman_dictionary:
                    pass
                else:
                    return 'STATUS: 103 BAD INPUT\nMESSAGE: YOU HAVE ENTERED A NON ROMAN NUMBER'

            return 'STATUS: 100 OK\nOBJECT TO BE CONVERTED: {}\nCONVERSION RESULT: {}'.format(to_convert, 10)
        except Exception as e:
            print(e)
            return 'STATUS: 101 INTERNAL ERROR\nMESSAGE: ERROR IN THE CONVERSION'

    def int_to_roman(self):
        return 'you want to convert a integer to an roman'

    def treat(self, command, to_convert):
        if(command == 'roman'):
            return self.roman_to_int(to_convert)
        elif(command == 'int'):
            return self.int_to_roman()
