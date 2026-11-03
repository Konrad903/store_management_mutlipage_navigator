import streamlit as st
import pandas as pd

csv_file=pd.read_csv('customers.csv')

st.title('Add New Customer')
st.markdown('___')

st.markdown('### Please enter the following details of the customer:')
st.write("  ")
st.write("  ")
st.write("  ")

name=st.text_input('**Customer Name:** ').capitalize()
num= st.number_input('**Customer Phone Number:** ',1000000000,9999999999,step=1)
email=st.text_input('**Customer Email:** ')
add=st.text_area('**Customer Address:** ')
id=0 
st.write('___')
if st.button('**Add Customer**'):
    id+=1
    if name and num and email:
        new_cust=pd.DataFrame({
            "ID": [id],
            "Name":[name],
            "Phone Number":[num],
            "Email Address":[email],
            "Address":[add]
        })

        csv_file=pd.concat([csv_file,new_cust],ignore_index=True)

        csv_file.to_csv('customers.csv', index=False)

        st.success('Customer Added Successfully! ')
        st.write('___')
        st.write(csv_file) 
    else:
        st.error("Please fill in required fields before submitting.")
