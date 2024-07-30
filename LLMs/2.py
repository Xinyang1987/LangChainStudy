# 聊天模型
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain.schema import (
    HumanMessage,
    SystemMessage,
    AIMessage
)

load_dotenv()

llm = ChatOpenAI(temperature=0.7)

message_List = [
    SystemMessage(content="你是一个非常有用的翻译小助手，能将英文翻译成西班牙语"),
    HumanMessage(content="3,2,1,你好马德里")
]
res = llm(message_List)
print(res)

