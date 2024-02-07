#1
class Vehicle:
    def __init__(self, model, year, price):
        self.model = model
        self.year = year
        self.price = price

    def display_info(self):
        print(f'Model: {self.model}')
        print(f'Year: {self.year}')
        print(f'Price: {self.price}')
#2
class Airplane(Vehicle):
    def __init__(self, model, year, price, max_altitude):
        super().__init__(model, year, price)
        self.max_altitude = max_altitude

    def fly(self):
        print(f"The {self.model} flying.")

    def display_info(self):
        super().display_info()
        print(f'Max Altitude: {self.max_altitude}')
#3
class Car(Vehicle):
    def __init__(self, model, year, price, fuel_type,):
        super().__init__(model, year, price)
        self.fuel_type = fuel_type

    def drive(self):
        print(f"The {self.model} driving.")

    def display_info(self):
        super().display_info()
        print(f'Vehicle Type: Car')
        print(f'Fuel Type: {self.fuel_type}')


# --
class NucleotideSequence:
    def __init__(self, locus, origin_sequence):
        self.locus = locus
        self.origin_sequence = origin_sequence

class GenBankParser:
    def parse(self, genbank_str):
        locus = None
        origin_sequence = ""

        lines = genbank_str.splitlines()
        for line in lines:
            if line.startswith("LOCUS"):
                locus = line.split()[1]
            elif line.startswith("ORIGIN"):
                origin_index = lines.index(line)
                origin_lines = lines[origin_index + 1:]
                for origin_line in origin_lines:
                    if origin_line.startswith("//"):
                        break
                    parts = origin_line.split()
                    origin_sequence += ''.join(parts[1:])

        return NucleotideSequence(locus, origin_sequence)

class FastaParser:
    def __init__(self, file_path):
        self.file_path = file_path

    def parse(self):
        with open(self.file_path, 'r') as file:
            fasta_data = {}
            current_header = None

            for line in file:
                line = line.strip()
                if line.startswith('>'):
                    current_header = line[1:]
                    fasta_data[current_header] = []
                else:
                    fasta_data[current_header].append(line)

            for header, sequence in fasta_data.items():
                fasta_data[header] = ''.join(sequence)

            return fasta_data

class MultiFastaParser:
    def __init__(self, file_path):
        self.file_path = file_path
        self.headers = []
        self.sequences = []
        self.fasta_data = {}

    def parse(self):
        with open(self.file_path, 'r') as file:
            current_header = None

            for line in file:
                line = line.strip()
                if line.startswith('>'):
                    current_header = line[1:]
                    self.headers.append(current_header)
                    self.fasta_data[current_header] = []
                else:
                    self.fasta_data[current_header].append(line)

            for header, sequence in self.fasta_data.items():
                self.fasta_data[header] = ''.join(sequence)
                self.sequences.append(self.fasta_data[header])

            return self.fasta_data

    def get_headers(self):
        return self.headers

    def get_sequences(self):
        return self.sequences

