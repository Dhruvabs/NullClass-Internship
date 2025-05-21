from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import ollama
import streamlit as st
import os

prompt = ChatPromptTemplate.from_messages(
    [
        {
            "system",
            "You are expert and helpful assistant. Your task is to generate article for the given topic. "
        },
        {
            "user",
            "Topic: {topic}"
        }
    ]
)
st.title ("Article Generator using three differenr llms")
input = st.text_input("Enter the topic on which you want article...........")

choices = ['gemma3:12b','phi4','llama2:13b']
llm_model = st.selectbox("Choose the model in the list ", choices)
llm = ollama(model = llm_model )

output_parser = StrOutputParser()
chain = prompt | llm | output_parser

if input:
    st.write("Article Topic: {input}")
    st.write(chain.invoke({"Topic":input}))