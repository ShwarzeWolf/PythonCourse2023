class fasta:
    def __init__(self, comment=None, data=None):
        self.comment = comment
        self.data = data

    def parse(self, file):
        self.comment = ""
        self.data = ""
        content = file.read()
        for i in content.split("\n"):
            if i[0] == ";":
                continue
            elif i[0] == ">":
                self.comment = i[1::]
            else:
                self.data += i

fastaFile1 = open("fasta.txt", "r")
fasta1 = fasta()
fasta1.parse(fastaFile1)
print(fasta1.comment)
print("----")
print(fasta1.data)