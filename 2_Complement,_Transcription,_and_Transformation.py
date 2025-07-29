import streamlit as st

st.title("Complement, Transcription, and Transformation")
st.markdown("""
### Please enter your gene in FASTA format
""")

default_FASTA = """>JN414165.1 Procyon lotor common northern raccoon breast and ovarian cancer susceptibility 1 (BRCA1) gene, exon 11 and partial cds
AGCCATGTGGCACAAATACTCATGCCAGCTCATTACAGCATGAGAACAGCAGTTTCTTACTCACTAAAGA
CAGAATGAACGTAGAAAAGGCTGAATTCTGTAATAAAAGCAAACAGCCTGGCTTAGCAAGCAGCCAACAG
AGCAGATGGGCTGAAAGTAAGGAAACATGTAATGATAGGCAGACTCCCAGCACAGAGAGAAAGGTACTTC
TGAATGCTGATCCCCTGTGTGGGAGAAAAGAACTGAAGAAGCAGAAACCTCCATGCTCTGACAGTCCTAG
"""
raw_FASTA = st.text_area("", value=default_FASTA, height = 300)

def clean_FASTA(raw_FASTA: str) -> str:
    lines = raw_FASTA.strip().upper().splitlines()
    cleaned_lines: list[str] = []
    
    for line in lines[1:]:
        line = line.strip()
        if line:
            cleaned_lines.append(line)
    
    cleaned_FASTA: str = "".join(cleaned_lines)
    return cleaned_FASTA
            
nucleotides = clean_FASTA(raw_FASTA).strip()

def complement(nucleotides: str) -> str:
    complement_map: dict[str, str] = {
    "A" : "T",
    "T" : "A",
    "C" : "G",
    "G" : "C"
    }
    complement_sequence = ""
    for nucleotide in nucleotides:
            if nucleotide in complement_map:
                complement_sequence += complement_map[nucleotide]
            else:
                complement_sequence += "N"
    
    return complement_sequence

def reverse_complement(nucleotides: str) -> str:
    return complement(nucleotides)[::-1]

def transcribe_RNA(nucleotides: str) -> str:
    return nucleotides.replace("T", "U")

def translate_amino_acids(nucleotides: str) -> str:
    amino_acid_map: dict[str, str] = {
        'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
        'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
        'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
        'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',                 
        'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
        'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
        'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
        'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
        'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
        'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
        'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
        'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
        'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
        'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
        'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
        'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W',   
    }
    amino_acids = ""
    codons = [nucleotides[n:n+3] for n in range(0, len(nucleotides), 3)]
    for codon in codons:
        if len(codon) != 3:
            continue
        amino_acids += amino_acid_map.get(codon, "-")
            
    return amino_acids

option = st.radio(
    "How do you want to process this sequence?",
    ["Complement", "Reverse Complement", "Transcribe to RNA", "Translate to Amino Acids"]
)

if nucleotides:
    if option == "Complement":
        st.write("Complement:", complement(nucleotides))
    elif option == "Reverse Complement":
        st.write("Reverse Complement:", reverse_complement(nucleotides))
    elif option == "Transcribe to RNA":
        st.write("RNA:", transcribe_RNA(nucleotides))
    elif option == "Translate to Amino Acids":
        st.write("Amino Acids:", translate_amino_acids(nucleotides))