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
    lines = raw_FASTA.strip().splitlines()
    cleaned_lines: list[str] = []
    
    for line: str in lines[1:]:
        line = lines.strip()
        