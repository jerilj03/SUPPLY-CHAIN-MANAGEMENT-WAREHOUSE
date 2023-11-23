import streamlit as st
import pandas as pd
from database import view_all, columns

def receipt():
    data1 = view_all("shipment_records")
    c1 = columns("shipment_records")
    data2 = view_all("shipments")
    c2 = columns("shipments")
    st.write("Incoming")
    st.dataframe(pd.DataFrame(data1,columns=c1), use_container_width=True)
    st.write("Outgoing")
    st.dataframe(pd.DataFrame(data2,columns=c2) ,use_container_width=True)