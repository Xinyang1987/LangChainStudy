# 提示
from langchain.prompts import ChatPromptTemplate

prompt = ChatPromptTemplate.from_template("can you use Chinese to tell me a joker about {topic}")

prompt_value = prompt.invoke({"topic":"ice_cream"})

print(prompt_value) # messages=[HumanMessage(content='can you use Chinese to tell me a joker about ice_cream')]
print(prompt_value.to_messages()) # [HumanMessage(content='can you use Chinese to tell me a joker about ice_cream')]
print(prompt_value.to_string()) # Human: can you use Chinese to tell me a joker about ice_cream