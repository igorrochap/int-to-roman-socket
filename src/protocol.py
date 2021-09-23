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
        
        self.integer_to_roman = [
            (1000, 'M'),
            (900, 'CM'),
            (500, 'D'),
            (400, 'CD'),
            (100, 'C'),
            (90, 'XC'),
            (50, 'L'),
            (40, 'XL'),
            (10, 'X'),
            (9, 'IX'),
            (5, 'V'),
            (4, 'IV'),
            (1, 'I'),            
        ]

    
    def roman_to_int(self, to_convert):
        try:
            to_convert = to_convert.replace(' ', '')
            response = 0
            for i in range(len(to_convert)):
                if to_convert[i] in self.roman_dictionary:
                    if i > 0 and self.roman_dictionary[to_convert[i]] > self.roman_dictionary[to_convert[i - 1]]:
                        response += (self.roman_dictionary[to_convert[i]]) - (self.roman_dictionary[to_convert[i - 1]] * 2)
                    else:
                        response += self.roman_dictionary[to_convert[i]]
                else:
                    return '\nSTATUS: 102\nMESSAGE: YOU HAVE ENTERED A NON ROMAN NUMBER\n'

            return '\nSTATUS: 100\nCONVERSION RESULT: {}\n'.format(response)
        except Exception as e:
            print(e)
            return 'STATUS: 101\nMESSAGE: INTERNAL ERROR\n'

    def int_to_roman(self, to_convert):
        try:
            if to_convert.startswith('-'):
                if not to_convert[1:].isdigit():
                    return '\nSTATUS: 102\nMESSAGE: YOU HAVE ENTERED A NON INTEGER NUMBER\n'
            else:
                if not to_convert.isdigit():
                    return '\nSTATUS: 102\nMESSAGE: YOU HAVE ENTERED A NON INTEGER NUMBER\n'
            
            to_convert = int(to_convert)

            if to_convert < 0:
                return '\nSTATUS: 102\nMESSAGE: YOU HAVE ENTERED A NON POSITIVE NUMBER\n'
            
            response = ''

            for (number, roman) in self.integer_to_roman:
                (division, to_convert) = divmod(to_convert, number)
                response += roman * division
            return '\nSTATUS: 100\nCONVERSION RESULT: {}\n'.format(response)
        except Exception as e:
            print(e)
            return '\nSTATUS: 101\nMESSAGE: INTERNAL ERROR\n'

    def treat(self, command, to_convert):
        if(command == 'ROMAN'):
            return self.roman_to_int(to_convert)
        elif(command == 'INT'):
            return self.int_to_roman(to_convert)
