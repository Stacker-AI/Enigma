from langchain.chains import LLMChain 
from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

llm = ChatOpenAI()

template = """Question: {question}

Given above conversation between doctor and patient with some placeholders in it like "<email>" etc.
Generate a summary of the whole conversation nothing else. 
If you want to return placeholders, feel free.

Answer: """

prompt = PromptTemplate(template=template, input_variables=["question"])
llm_chain = LLMChain(prompt=prompt, llm=llm)

def send_prompt(text: str):
    response = llm_chain.invoke(text)
    return response