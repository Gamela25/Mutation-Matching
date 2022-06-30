#بسم الله الرحمن الرحيم
import difflib

with open("C:\\Users\\hp\\OneDrive\\Desktop\\sequencematching\\TP53.fasta",'r') as gene:
      gene_content=gene.read()
print(gene_content)

with open("C:\\Users\\hp\\OneDrive\\Desktop\\sequencematching\\patient.txt",'r') as patient:
    patient_content=patient.read()
print(patient_content)


cases = [(patient_content, gene_content)]

for a, b in cases:
    # print('{} => {}'.format(a,b))

    for i, s in enumerate(difflib.ndiff(a, b)):
        if s[0] == ' ':
            continue
        elif s[0] == '-':
            print(u'Delete "{}"  {}'.format(s[-1],i))
        elif s[0] == '+':
            print(u'Add "{}"  {}'.format(s[-1], i))
    print()
