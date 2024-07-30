# 基础示例 : 提示 + 模型 + 输出解析器
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain.chains.llm import LLMChain
from dotenv import load_dotenv
load_dotenv()


prompt = ChatPromptTemplate.from_template("can you use Chinese to tell me a short joker about {topic}")
model = ChatOpenAI()
output_parser = StrOutputParser()

# chain的简易定义方式 chain = prompt | model | output_parser
# | 符号类似于 unix 管道操作符，它将不同的组件链接在一起，将一个组件的输出作为下一个组件的输入
chain = LLMChain(
    llm=model,
    prompt=prompt,
    output_parser=output_parser

)


response = chain.invoke({"topic":"ice-cream"})

print(response)
"""
output:
Why did the ice cream go to therapy? 

Because it had too many toppings and couldn't find its sundae-self.
"""