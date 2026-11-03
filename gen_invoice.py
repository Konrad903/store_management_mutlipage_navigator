import streamlit as st
import pandas as pd

csv_file=pd.read_csv('products.csv')

st.title('**Invoice**')
st.markdown('___')

st.markdown('### Please enter the following details of the invoice:')
st.write("  ")
st.write("  ")
st.write("  ")

id=st.number_input('**Invoice ID:** ',min_value=101)
product= st.text_input('**Product Name:** ').capitalize()
name=st.text_input('**Customer Name:** ')
desc=st.text_area('**Product Description:** ')
price=st.number_input('**Price**: ',min_value=100)
st.write('___')
if st.button('*Generate Invoice*'):

    if id and product and price:
        invoice=pd.DataFrame({
            'Id':[id],
            'Product Name':[product],
            'Customer Name':[name],
            'Product Description':[desc],
            'Price':[price]
        })

        csv_file=pd.concat([invoice,csv_file],ignore_index=True)

        csv_file.to_csv('products.csv', index=False)

        st.success('Invoice Details Added! ')
        st.write('___')
        st.write(csv_file) 
    else:
        st.error("Please fill in required fields before submitting.")
