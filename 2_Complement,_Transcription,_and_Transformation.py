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

def clean_FASTA(raw_FASTA: str):
    lines = raw_FASTA.strip().upper().splitlines()
    cleaned_lines: list[str] = []
    
    for line in lines[1:]:
        line = line.strip()
        if line:
            cleaned_lines.append(line)
    
    cleanedFASTA: str = "".join(cleaned_lines)
    return cleanedFASTA
            
    
complement_map: dict[str, str] = {
    "A" : "T",
    "T" : "A",
    "C" : "G",
    "G" : "C"
    }

