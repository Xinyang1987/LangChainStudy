# 提示模板初步
# 目的：是生成语言模型提示的预定义配方
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate

template = """/
You are naming consultant for new companies.
What is a good name for a company that makes {product}?
"""

prompt = PromptTemplate.from_template(template)
response = prompt.format(product="colorful socks") # 变量值赋予模板

print(response)