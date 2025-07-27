import streamlit as st
import pandas as pd
import altair as alt

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

option = st.radio(
    "How do you want to process this sequence?",
    ["Complement", "Reverse Complement", "Transcribe to RNA", "Translate to Amino Acids"]
)

