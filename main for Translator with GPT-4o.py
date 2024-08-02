import streamlit as st
from Translator_with_GPT_4o import translate


st.set_page_config(
    page_title="Translator.AI",
    layout="centered"
)

# Streamlit page title
st.title("Translator app - GPT-4o")

column_1, column_2 = st.columns()

with column_1:
    input_languages_list = ["English", "French", "German", "Latin", "Spanish", "Hindi", "Tamdi"]
    input_language = st.selectbox(label="Enput Language", options=input_languages_list)

with column_2:
    output_languages_list = [x for x in input_languages_list if x != input_languages]
    output_language = st.selectbox(label="Output Languages", options=output_languages_list)

input_text = st.text_area("Type the text to be translated")

if st.button("Translate"):
    translated_text = translate(input_language, output_language, input_text)

    st.success(translated_text)