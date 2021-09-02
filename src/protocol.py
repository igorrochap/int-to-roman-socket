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
            result = 0
            for i in range(len(to_convert)):
                if to_convert[i] in self.roman_dictionary:
                    if i > 0 and self.roman_dictionary[to_convert[i]] > self.roman_dictionary[to_convert[i - 1]]:
                        result += self.roman_dictionary[to_convert[i - 1]] * (self.roman_dictionary[to_convert[i]] - 2)
                    else:
                        result += self.roman_dictionary[to_convert[i]]
                else:
                    return '\nSTATUS: 102\nMESSAGE: YOU HAVE ENTERED A NON ROMAN NUMBER\n'

            return '\nSTATUS: 100\nOBJECT TO BE CONVERTED: {}\nCONVERSION RESULT: {}\n'.format(to_convert, result)
        except Exception as e:
            print(e)
            return 'STATUS: 101\nMESSAGE: INTERNAL ERROR\n'

    def int_to_roman(self):
        return 'you want to convert a integer to an roman'

    def treat(self, command, to_convert):
        if(command == 'ROMAN'):
            return self.roman_to_int(to_convert)
        elif(command == 'INT'):
            return self.int_to_roman()
