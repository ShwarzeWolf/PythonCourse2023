class NucleotideSequence:
    def __init__(self, description, sequence):
        self.description = description
        self.sequence = sequence

class SequenceParser:
    def parse(self, sequence_string, format):
        if format == 'fasta':
            return self._parse_fasta(sequence_string)
        # добавить больше форматов позже
        raise ValueError('Unsupported format')

    def _parse_fasta(self, fasta_string):
        lines = fasta_string.strip().split('\n')
        records = []
        description = None
        sequence_parts = []

        for line in lines:
            if line.startswith(';'):
                continue
            elif line.startswith('>'):
                if description:
                    records.append(NucleotideSequence(description, ''.join(sequence_parts)))
                description = line[1:].strip()
                sequence_parts = []
            else:
                sequence_parts.append(line.strip())

        if description:
            records.append(NucleotideSequence(description, ''.join(sequence_parts)))

        return records

class SequenceFormatter:
    def format(self, sequences, format):
        if format == 'fasta':
            return self._format_fasta(sequences)
        # добавить больше форматов позже
        raise ValueError('Unsupported format')

    def _format_fasta(self, sequences):
        fasta_strings = []
        for sequence in sequences:
            fasta_strings.append('>{}\n{}'.format(sequence.description, sequence.sequence))
        return '\n'.join(fasta_strings)

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


sequence_parser = SequenceParser()

parsed_sequences = sequence_parser.parse(fasta_string, 'fasta')

for sequence in parsed_sequences:
    print(f"Description: {sequence.description}")
    print(f"Sequence: {sequence.sequence}\n")

sequence_formatter = SequenceFormatter()

formatted_fasta = sequence_formatter.format(parsed_sequences, 'fasta')

print("Formatted data:")
print(formatted_fasta)