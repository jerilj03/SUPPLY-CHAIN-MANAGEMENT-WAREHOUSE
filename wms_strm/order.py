import streamlit as st
import pandas as pd
from database import check_thresh,add_data,update_items

def order():
    thresh_rows=check_thresh()
    rows=list(range(len(thresh_rows)))
    dict2={}
    for i in rows:
        dict2[thresh_rows[i][0]]=i
    dict1={}
    try:
        choice=st.selectbox("Items understocked",dict2.keys())
        rowno=dict2[choice]
        st.write(thresh_rows[rowno][0],"has dropped below",thresh_rows[rowno][2])
        q=st.text_input("Quantity:")
        if st.button("approve",key=-1*i):
            # if q>0:
            dict1["Item_Id"]=str(thresh_rows[rowno][1])
            dict1['Item_Name']=str("'"+thresh_rows[rowno][0]+"'")
            dict1["Quantity"]=str(q)

            add_data("shipment_records",dict1)
            st.success("Successfully ordered")
            update_items(thresh_rows[rowno][1],q)
            st.success("Successfully updated")
            # else:
            #     st.error("Invalid quantity!")
    except:
        st.write("NO ITEMS UNDERSTOCKED")