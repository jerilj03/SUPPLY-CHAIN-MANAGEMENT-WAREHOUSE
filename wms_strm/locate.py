import streamlit as st
from database import view_all, columns
import pandas as pd


def locate():
    d1 = st.text_input("Item ID")
    if st.button("Locate"):
        x = ""
        y = 0
        data = view_all("items")
        # print(data)
        # st.table(data)
        for i in data:
            if i[1]==int(d1):
                x = i[3]
                y = i[2]
                break
        if x=="":
            st.error("Invalid item id")
        else:
            st.write("Location:",x)
            st.write("Quantitiy:",y)

        
    
