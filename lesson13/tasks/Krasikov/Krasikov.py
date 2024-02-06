class Parser:
    def parse(self, filename):
        data = open(filename, 'r').readlines()
        parsed_data = ParsedData()
        for line in data:
            if line[0] == ";":
                parsed_data.comments += ", "+line[2:-1]
            elif line[0] == ">":
                parsed_data.metadata += line[1:]
            else:
                parsed_data.data += line
        return parsed_data

class ParsedData:
    data = ""
    comments = ""
    metadata = ""
    def __str__(self):
        return f"Comments: {self.comments[2:]}\ndata: {self.data[:-1]}\nmetadata: {self.metadata[:-1]}"

parser = Parser()
print(parser.parse("fasta.txt"))