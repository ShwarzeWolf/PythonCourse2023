from typing import Optional


class DNASequence:
    def __init__(self, comment: Optional[str], molecules: str):
        self._comment = comment
        self._molecules = molecules

    def __repr__(self):
        return f"DNASequence('{self._comment}'; '{self._molecules[:20]}...'; length = {len(self._molecules)})"

    def print_molecules(self, line_length: Optional[int] = None):
        if line_length is None:
            print(self._molecules)
        else:
            for start in range(0, len(self._molecules), line_length):
                print(self._molecules[start:start + line_length])

    @classmethod
    def create_empty(cls):
        return cls(None, "")

    @property
    def comment(self):
        return self._comment

    @comment.setter
    def comment(self, new_comment: Optional[str]):
        self._comment = new_comment

    @property
    def molecules(self):
        return self._molecules

    @molecules.setter
    def molecules(self, new_molecules: str):
        self._molecules = new_molecules


class FastaParser:
    @staticmethod
    def parse(filename: str) -> DNASequence:
        sequence = DNASequence.create_empty()

        with open(filename, "r") as file:
            for line in file:
                if line.startswith(">"):
                    sequence.comment = line[1:].strip()
                elif line.startswith(";"):
                    pass
                else:
                    sequence.molecules += line.strip()

        return sequence


if __name__ == "__main__":
    FASTA_ROUTE = ""  # WRITE YOUR FASTA FILE ROUTE HERE
    parsed_sequence = FastaParser.parse(FASTA_ROUTE)
    print(parsed_sequence)
    print()
    parsed_sequence.print_molecules(line_length=60)
