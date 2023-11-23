import streamlit as st
from database import columns,view_id, add_request, check_qty, deduct, view_all



def request():
    selected_table = "shipments"
    col_list = columns(selected_table)
    # dict1 = {}
    col1,col2 = st.columns(2)

    cols=["item_id","Quantity"]
    dict1 = {}
# for i in range(3):
    with col1:
        dict1[cols[0]] = st.text_input(cols[0] + ": ")
# for i in range(3,6):
    with col2:
        dict1[cols[1]] = st.text_input(cols[1] + ": ")    
    

    # sel=view_all("items")
    vals = list(dict1.values())
    vals = [int(x) for x in vals if x != '']
    
    # for i in sel:
    #     if  vals[0]==i[1]:
    #         # if vals[1]<i[2]:
    #         p =  int(i[2])
    if st.button("Request"):
        try:
            # Check for empty values in dict1
            if any(value is None or value.strip() == "" for value in dict1.values()):
                st.error("Invalid input: Text inputs cannot be empty.")
            else:
                qty = check_qty(vals)
                if qty is None:
                    st.error("Item id does not exist.")

                # if check_qty(dict1[cols[0]],dict1[cols[1]]):
                elif qty > int(dict1[cols[1]]):
                    add_request(dict1)
                    deduct(vals[0],vals[1])
                    st.success("Successfully requested item")
                    # pass
                else:
                    st.error("Requested item not available for the required quantity. Please wait till it gets restocked.")
                
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
    

    





