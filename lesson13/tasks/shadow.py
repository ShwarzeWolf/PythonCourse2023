class FastaRecord:
    def __init__(self, description, sequence):
        self.description = description
        self.sequence = sequence

class FastaParser:
    def parse(self, fasta_string):
        lines = fasta_string.strip().split('\n')
        records = []
        description = None
        sequence_parts = []

        for line in lines:
            if line.startswith(';'):
                continue
            elif line.startswith('>'):
                if description:
                    records.append(FastaRecord(description, ''.join(sequence_parts)))
                description = line[1:].strip()
                sequence_parts = []
            else:
                sequence_parts.append(line.strip())

        if description:
            records.append(FastaRecord(description, ''.join(sequence_parts)))

        return records

fasta_string = """>MCHU - Calmodulin - Human, rabbit, bovine, rat, and chicken
tgcaccaaacatgtctaaagctggaaccaaaattactttctttgaagacaaaaactttca
aggccgccactatgacagcgattgcgactgtgcagatttccacatgtacctgagccgctg
caactccatcagagtggaaggaggcacctgggctgtgtatgaaaggcccaattttgctgg
gtacatgtacatcctaccccggggcgagtatcctgagtaccagcactggatgggcctcaa
cgaccgcctcagctcctgcagggctgttcacctgtctagtggaggccagtataagcttca
gatctttgagaaaggggattttaatggtcagatgcatgagaccacggaagactgcccttc
catcatggagcagttccacatgcgggaggtccactcctgtaaggtgctggagggcgcctg
gatcttctatgagctgcccaactaccgaggcaggcagtacctgctggacaagaaggagta
ccggaagcccgtcgactggggtgcagcttccccagctgtccagtctttccgccgcattgt
ggagtgatgatacagatgcggccaaacgctggctggccttgtcatccaaataagcattat
aaataaaacaattggcatgc"""

parser = FastaParser()
records = parser.parse(fasta_string)

for record in records:
    print(f"Description: {record.description}")
    print(f"Sequence: {record.sequence}")