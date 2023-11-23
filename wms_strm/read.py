from collections import defaultdict
# import store
import pandas as pd
import streamlit as st
from database import columns, view_id, tables, view_all
import streamlit_pandas as sp
# def read():
#     cols = ["Item name","Item Id","Quantity"]
#     # disp = defaultdict(list)
#     disp = {}
#     for i in range(len(cols)):
#         disp[cols[i]] = "1"
#     # tables_list = [i for i in tables_list1 if i!="users"]
#     # selected_viewtable = st.selectbox("Table to View : ", disp)
#     # cols = columns(selected_viewtable)
#     # df = pd.DataFrame(disp, columns=cols)
#     df = pd.DataFrame(data=[disp], columns=cols, index=[your_index_value])
#     st.dataframe(pd, use_container_width=True)



def read():
    tables_list = tables()
    d = {}
    tl = ["Items Table", "Import Records", "Export Records"]
    for i in range(len(tables_list)):
        d[tl[i]] = tables_list[i]
    selected_viewtable = st.selectbox("Table to View : ", d)
    selected_viewtable = d[selected_viewtable]
    cols = columns(selected_viewtable)

    df = pd.DataFrame(data= view_all(selected_viewtable), columns=cols)
    # if 'time' in df.columns:
    #     df['time'] = df['time'].astype(str).apply(lambda x: x.split()[2])
    
    if df.empty:
        st.dataframe(df,use_container_width=True)    
    else:
        all_widgets = sp.create_widgets(df)
        res = sp.filter_df(df, all_widgets)
        st.dataframe(res,use_container_width=True)
    # st.dataframe(df, use_container_width=True)

def readsm():
    tlist = tables()
    tables_list = [i for i in tlist if i!="shipment_records"]
    d = {}
    tl = ["Warehouse inventory", "Import Records"]
    for i in range(len(tables_list)):
        d[tl[i]] = tables_list[i]
    selected_viewtable = st.selectbox("Table to View : ", d)
    # selected_viewtable = st.selectbox("Table to View : ", tables_list)
    selected_viewtable = d[selected_viewtable]
    cols = columns(selected_viewtable)

    df = pd.DataFrame(data= view_all(selected_viewtable), columns=cols)
    # if 'time' in df.columns:
    #     df['time'] = df['time'].astype(str).apply(lambda x: x.split()[2])
    
    # st.dataframe(df, use_container_width=True)
    if df.empty:
        st.dataframe(df,use_container_width=True)    
    else:
        all_widgets = sp.create_widgets(df)
        res = sp.filter_df(df, all_widgets)
        st.dataframe(res,use_container_width=True)


def readwk():
    # st.header("Items")
    cols = columns("items")
    df = pd.DataFrame(data= view_all("items"), columns=cols)
    # if 'time' in df.columns:
    #     df['time'] = df['time'].astype(str).apply(lambda x: x.split()[2])
    
    # st.dataframe(df, use_container_width=True)
    # if df.empty:
    #     st.dataframe(df,use_container_width=True)    
    # else:
    all_widgets = sp.create_widgets(df)
    res = sp.filter_df(df, all_widgets)
    st.dataframe(res,use_container_width=True)