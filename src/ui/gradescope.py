import streamlit as st
import sys
sys.path.append('../')
import pandas as pd

from ui.view import View

def gradescope():
    view = View(student_id=1003)

    st.subheader('_Class MATH314 Grade scope_  :orange[Stats] :chart_with_upwards_trend:', divider='rainbow')
    view.gradescope_display(json_file_path ='../data/gradescope/math314.json')

    st.subheader('_Class PHYS999 Grade scope_  :green[Stats] :chart_with_upwards_trend:', divider='rainbow')
    view.gradescope_display(json_file_path='../data/gradescope/phys999.json')

    st.subheader('_Class LANG101 Grade scope_  :red[No Stats] :coffee:', divider='rainbow')
    st.caption('Check Moodle for this course')
    # gradescope_display(json_file_path='./data/gradescope/math314.json')



