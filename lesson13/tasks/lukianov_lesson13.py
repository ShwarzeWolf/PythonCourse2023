from dataclasses import dataclass


@dataclass
class Molecule:
    information: str
    construction: str


class Fasta:
    fasta_information = []
    fasta_construction = []

    def __init__(self, string):
        self.string = string

    def parse(self):
        for line in self.string.strip().split('\n'):
            if line[0] == ';':
                continue
            elif line[0] == '>':
                self.fasta_information.append(line[1:])
            else:
                self.fasta_construction.append(line)


fasta_string = '''; comment 1
; comment 2
>MCHU - Calmodulin - Human, rabbit, bovine, rat, and chicken
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
aaataaaacaattggcatgc'''

fasta = Fasta(fasta_string)
fasta.parse()

molecule = Molecule("".join(Fasta.fasta_information), "".join(Fasta.fasta_construction))

print(molecule)
