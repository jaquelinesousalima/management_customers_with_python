import streamlit as st

st.title("New Customer")

name = st.text_input("Type the name of customer")
address = st.text_input("Type the address")
birth_date = st.date_input("Choose the birth date")
type_of_customer = st.selectbox("Type of customer", ["Individual", "Legal Entity"])

save = st.button("Save")

if save:
    with open("customers_database.csv", "a", encoding="utf-8") as file:
        file.write(f"{name},{address},{birth_date},{type_of_customer}\n")
        st.success("Customer saved successfully!")