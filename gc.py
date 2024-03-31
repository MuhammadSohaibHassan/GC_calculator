import streamlit as st

"""
# GC_Calculator
"""
seq = st.text_input("Enter your Sequence","ATGC").upper()

seq_len = len(seq)
Gs = seq.count("G")
Cs = seq.count("C")
As = seq.count("A")
Ts = seq.count("T")
if seq_len!=0:
    if (Gs+Cs+As+Ts)==seq_len:
        GC_con =(Gs+Cs)/seq_len*100
        st.write("GC_Content of seq is ",GC_con,"%")
    else:
        st.write("Seq can only contain A , T , G and C ")
else:
    st.write("Please enter some sequence!")