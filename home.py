import streamlit as st

st.title("Home Page")
st.set_page_config(page_title='CST1510 CW2',
                   page_icon="img/mdi.jpg"
                    )
st.write("Choose where to be redirected")
st.button("Cyber Incidents")
st.button("Datasets Metadata")
st.button("It Tickets")
st.button("Logout")
