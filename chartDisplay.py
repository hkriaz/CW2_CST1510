import streamlit as st
import pandas as pd
import numpy as np

data = pd.DataFrame(
    np.random.rand(30, 4),
    columns=['Sales', 'Abu Dhabi', 'Prices', 'Dubai']
)

col1,col2 = st.columns(2)

with col1:
    st.line_chart(data)
with col2:
    st.area_chart(data)
