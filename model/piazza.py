import streamlit as st
import sys
sys.path.append('../')
from read_syntatic_data import convert_piazzajson_to_csv
import numpy as np
from llm import generate_summary, get_prompts
import random
from view.view import View


def grade_piazza():
    # Use the full page instead of a narrow central column
    view = View(student_id=1001)
    # st.subheader('_Class MATH314 Grade scope_  :orange[Stats] :chart_with_upwards_trend:', divider='rainbow')
    st.subheader('_Discussion from piazza for LANG101_  :green[TOP Discussions] :coffee:', divider='rainbow')
    view.piazza_display(json_file_path ='./data/piazza/lang101.json')
    view.piazza_LLM_sample_caption(course='LANG101')

    st.subheader('_Discussion from piazza for MATH314_  :orange[TOP Discussions] :coffee:', divider='rainbow')
    view.piazza_display(json_file_path='./data/piazza/math314.json')
    view.piazza_LLM_sample_caption(course='MATH314')

    st.subheader('_Discussion from piazza for phys999_  :orange[TOP Discussions] :coffee:',divider='rainbow')
    view.piazza_display(json_file_path='./data/piazza/phys999.json')
    view.piazza_LLM_sample_caption(course='phys999')

    # Space out the maps so the first one is 2x the size of the other three


