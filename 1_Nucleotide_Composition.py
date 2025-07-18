import streamlit as st
import pandas as pd

st.title("Nucleotide Composition")
st.markdown("""
## Please enter your gene in FASTA format
""")
default_fasta = """>JN414165.1 Procyon lotor common northern raccoon breast and ovarian cancer susceptibility 1 (BRCA1) gene, exon 11 and partial cds
AGCCATGTGGCACAAATACTCATGCCAGCTCATTACAGCATGAGAACAGCAGTTTCTTACTCACTAAAGA
CAGAATGAACGTAGAAAAGGCTGAATTCTGTAATAAAAGCAAACAGCCTGGCTTAGCAAGCAGCCAACAG
AGCAGATGGGCTGAAAGTAAGGAAACATGTAATGATAGGCAGACTCCCAGCACAGAGAGAAAGGTACTTC
TGAATGCTGATCCCCTGTGTGGGAGAAAAGAACTGAAGAAGCAGAAACCTCCATGCTCTGACAGTCCTAG
"""

rawFASTA = st.text_area("", value=default_fasta, height=300)

def cleanFASTA(rawFASTA: str) -> str:
    lines = rawFASTA.strip().splitlines()
    cleaned_lines: list[str] = []
    
    for line in lines[1:]:
        line = line.strip()
        if line:
            cleaned_lines.append(line)
            
    cleanedFASTA: str = "".join(cleaned_lines)
    return cleanedFASTA

nucleotides = cleanFASTA(rawFASTA).upper()
g_content: int = nucleotides.count('G')
c_content: int = nucleotides.count('C')
a_content: int = nucleotides.count('A')
t_content: int = nucleotides.count('T')

st.write(f"Your sequence is composed of {g_content} guanine, {c_content} cystine, {a_content} adenine, and {t_content} thymine.")
