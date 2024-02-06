class Parser:
    def parse(self, filename):
        with open(filename, "r") as f:
            lines = f.readlines()

        sequences = []
        sequence = ""
        previous_metadata = None
        comment = None

        for line in lines:
            # if line[0] == ";":
            #     comment = line[1:].strip()
            #     sequences.append((comment, previous_metadata, sequence))
            #     sequence = ""
            if line[0] == ">":
                if previous_metadata:
                    sequences.append((comment, previous_metadata, sequence))
                previous_metadata = line[1:].strip()
                sequence = ""
            elif line[0] != "<" and line[0] != ";":
                sequence += line

        if sequence and previous_metadata:
            sequences.append((comment, previous_metadata, sequence))

        return sequences



parser = Parser()
sequences = parser.parse("fasta")

for comment, metadata, sequence in sequences:
    print(comment)
    print(metadata)
    print(sequence)