import streamlit as st
import pandas as pd

import numpy as np
import random
def grade_piazza():
    # Use the full page instead of a narrow central column

    c1, c2= st.columns((1, 1))
    with c1:
        c01, c02, c03 = st.columns((1, 1, 1))
        with c01:
            st.text_area("Active Courses", "3/80")
        with c02:
            st.text_area("Piazza Answered", "25")

        c21, c22 = st.columns((1, 1))
        with c21:
            st.text_area("Avg. Grade", "A")
        with c22:
            st.text_area("Improvement", "12%")

    with c2:
        st.header("A dog")
        st.image("https://static.streamlit.io/examples/dog.jpg")

    # c11, c12 = st.columns((1, 1))
    # with c11:
    #     st.header("A cat")
    #     st.image("https://static.streamlit.io/examples/cat.jpg")
    #
    # with c12:
    #     st.header("A dog")
    #     st.image("https://static.streamlit.io/examples/dog.jpg")

    # with c3:
    #     st.header("An owl")
    #     st.image("https://static.streamlit.io/examples/owl.jpg")
    #
    # with c4:
    #     st.header("An owl")
    #     st.image("https://static.streamlit.io/examples/owl.jpg")

    chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["CS520", "CS646", "CS70"])

    st.area_chart(chart_data)
    # Space out the maps so the first one is 2x the size of the other three


