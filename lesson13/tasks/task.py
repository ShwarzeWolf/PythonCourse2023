class Data:
    def __init__(self, parsed_text):
        self.molecules = parsed_text[0]
        self.information = parsed_text[1]


class Parser:
    def __init__(self, file_name):
        self.text = open(f'{file_name}', 'r').read()

    def parse(self):
        required_text = self.text[self.text.index('>')+1:]
        parsed_text = Data(
            tuple((required_text[:required_text.index('\n')],
                  required_text[required_text.index('\n')+1:].replace('\n', '')))
        )
        return parsed_text


FILE_NAME = 'FASTA.txt'

file = Parser(FILE_NAME)
text = file.parse()
print(f'Последовательность:\n{text.molecules}', f'Информация:\n{text.information}', sep='\n')