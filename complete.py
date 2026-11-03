import streamlit as st
import pandas as pd



add_cust=st.Page(
    
    page='add_cust.py',
    title='Add New Customer',
    icon='🙍‍♂️',
    default=False

)

gen_invoice=st.Page(
    page='gen_invoice.py',
    title='Generate Invoice',
    icon='💵',
    default=True

)

page=st.navigation(
    {
        'Customer':[add_cust],
        'Invoice':[gen_invoice],
    }
)

page.run()







