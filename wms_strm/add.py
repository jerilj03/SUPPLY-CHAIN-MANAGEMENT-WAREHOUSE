import streamlit as st
from database import add_data, tables, columns, view_all

def add():
    selected_table = "items"
    col_list = ["Item_name","Item_Id","Threshold","Position","Perishable"]
    dict1 = {}
    col1,col2 = st.columns(2)
    for i in range(int(len(col_list)/2)):
        with col1:
            dict1[col_list[i]] = st.text_input(col_list[i] + ": ")
    for i in range(int(len(col_list)/2),len(col_list)):
        with col2:
            dict1[col_list[i]] = st.text_input(col_list[i] + ": ")
    dict1["Quantity"]="0"
    if st.button("Add Data"):
        for key in dict1:
            temp = dict1[key]
            try:
                temp2 = int(temp)
                dict1[key] = temp
            except Exception:
                dict1[key] = "'" +temp+"'"

        add_data(selected_table, dict1)
        st.success("Successfully created a new class of Item")
