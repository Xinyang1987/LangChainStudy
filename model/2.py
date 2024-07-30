# 提示模板具有不同数量的变量
from langchain.prompts import PromptTemplate

no_input_prompt = PromptTemplate(input_variables=[],template="Tell me a joke")
no_input_prompt.format()

one_input_prompt = PromptTemplate(input_variables=["adjective"],template="Tell me {adjective} joke")
one_input_prompt.format(adjective="funny")

multiple_input_prompt =  PromptTemplate(
    input_variables=["adjective","content"],
    template="Tell me a {adjective} joke about {content}"
)

prompt = multiple_input_prompt.format(adjective="funny",content="chickens")

print(prompt)