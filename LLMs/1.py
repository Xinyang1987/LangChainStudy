from langchain_openai import ChatOpenAI # 结果包括多个属性对象
from langchain.llms import OpenAI # 定义的大模型，结果直接是字符串
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI()

# 最简单的调用方法 String in -> String out
res = llm("tell me a joke")
print(res)
"""
Why couldn't the bicycle stand up by itself?

Because it was two-tired!
"""

# 批处理调用，更丰富的输出
# res_list = llm.generate(["tell me a joke","teach me how to play basketball"]*15)
# print(res_list)

