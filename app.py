import streamlit as st
import openai
import os
from cosmic.functions import cosmic_analyze, print_analysis

st.title("COMET")

tab1, tab2 = st.tabs(["Use case", "Analysis"])

def manage_tab1():
	if "analysis" not in st.session_state:
		st.session_state["analysis"] = ""
	openai.api_key = os.getenv('OPENAI_KEY')
	st.header("Use case")
	uc_name = st.text_input(label='Enter the use case name:', value="")
	input_text = st.text_area(label='Enter the use case content to measure:', value="", height=250)
	# on submit, we call cosmic_analyze
	st.button("submit", on_click=cosmic_analyze, kwargs={"uc_name": uc_name, "uc_content": input_text})
	output_text = st.text_area(label='GPT-3 response:', value=st.session_state["analysis"], height=250)


def manage_tab2():
	st.header("Analysis")
	lines = st.session_state["analysis"].split('\n')
	print_analysis(lines)

with tab1:
	manage_tab1()
	
with tab2:
	manage_tab2()
