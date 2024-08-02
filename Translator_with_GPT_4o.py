import os
import json
import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
import openai 

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

# Configure openai api key
working_dire = os.path.dirname(os.path.abspath(__file__))
config_data = json.load(open(f"{working_dire}/config.json"))

OPENAI_API_KEY = config_data["OPENAI_API_KEY"]
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

llm = ChatOpenAI(
    model="gpt-4o",
    temperature=0
)

def translate(input_language, output_language, input_text):
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", "You are a helpful assistant that translate {input_language} to {output_language}."),
            ("hmage", "{input}")
        ]
    )

    chain = prompt | llm
    response = chain.invoke(
        {
            "input_language":input_language,
            "output_language":output_language,
            "input":input_text
        }
    )
    return response.context