# use openai two way
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

llm = OpenAI()
chat_model = ChatOpenAI()

print(llm.predict("what is 1+1")) # 1+1 is equal to 2.
print(chat_model.predict("what is 1+2")) # 1 + 2 equals 3.