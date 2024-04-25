from langchain_experimental.data_anonymizer import PresidioAnonymizer
from langchain_core.prompts.prompt import PromptTemplate
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from utils import phone_number_operator
from prompt import prompt_template
import json

load_dotenv()

anonymizer = PresidioAnonymizer()
anonymizer.add_operators(phone_number_operator)

llm = ChatOpenAI(
    temperature=0.5, model="gpt-3.5-turbo-0125", response_format={"type": "json_object"}
)

prompt = PromptTemplate.from_template(prompt_template)


chain = {"anonymized_text": anonymizer.anonymize} | prompt | llm

text = ""


response = chain.invoke(text)

if response is None:
    print("No response from chain")
    exit()


response_json = json.loads(str(response.content), strict=False)

print(response_json)
