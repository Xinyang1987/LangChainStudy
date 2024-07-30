# 文档加载器
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain.document_loaders import TextLoader

load_dotenv()
# llm = ChatOpenAI()

loader = TextLoader("./file/data.txt",encoding="utf-8") # 需指出编码
res = loader.load()

print(res) # [Document(metadata={'source': './file/data.txt'}, page_content='3,2,1,你好马德里')]

