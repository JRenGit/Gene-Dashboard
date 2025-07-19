import streamlit as st
import pandas as pd
import altair as alt

st.title("Nucleotide Composition")
st.markdown("""
### Please enter your gene in FASTA format
""")
default_FASTA = """>JN414165.1 Procyon lotor common northern raccoon breast and ovarian cancer susceptibility 1 (BRCA1) gene, exon 11 and partial cds
AGCCATGTGGCACAAATACTCATGCCAGCTCATTACAGCATGAGAACAGCAGTTTCTTACTCACTAAAGA
CAGAATGAACGTAGAAAAGGCTGAATTCTGTAATAAAAGCAAACAGCCTGGCTTAGCAAGCAGCCAACAG
AGCAGATGGGCTGAAAGTAAGGAAACATGTAATGATAGGCAGACTCCCAGCACAGAGAGAAAGGTACTTC
TGAATGCTGATCCCCTGTGTGGGAGAAAAGAACTGAAGAAGCAGAAACCTCCATGCTCTGACAGTCCTAG
"""

rawFASTA = st.text_area("", value=default_FASTA, height=300)

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

st.write(f"Your sequence is composed of {g_content} guanine, {c_content} cytosine, {a_content} adenine, and {t_content} thymine.")

st.markdown("""
### Bar Graph of Nucleotide Counts
            """)

nucleotide_df = pd.DataFrame({"Nucleotide": ["Guanine", "Cytosine", "Adenine", "Thymine"],
                              "Count": [g_content, c_content, a_content, t_content]})

bar_chart = alt.Chart(nucleotide_df).mark_bar().encode(
    x = alt.X("Nucleotide", axis = alt.Axis(labelAngle = 0)),
    y = "Count",
    color = "Nucleotide",
    tooltip = ["Nucleotide", "Count"]
)

st.altair_chart(bar_chart)

st.markdown("""
### Pie Chart of Nucleotide Counts
            """)
pie_chart = alt.Chart(nucleotide_df).mark_arc().encode(
    theta="Count",
    color="Nucleotide"
)

st.altair_chart(pie_chart)