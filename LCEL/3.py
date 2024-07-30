# 模型
from langchain_openai import ChatOpenAI,OpenAI
from dotenv import load_dotenv
from langchain.prompts import ChatPromptTemplate

load_dotenv()

# 情况一 在这种情况下，我们的 model 是一个 ChatModel，这意味着它将输出一个 BaseMessage
model = ChatOpenAI()

# 情况二 如果我们的 model 是一个 LLM，它将输出一个字符串
model_1 = OpenAI(model="gpt-3.5-turbo-instruct")

# 定义模板
prompt = ChatPromptTemplate.from_template("can you tell me a joker about {topic}")
prompt_value = prompt.invoke({"topic":"basketball"})

print(model.invoke(prompt_value))
"""
content='Why did the basketball go to therapy? 
\n\nBecause it had too many bounce issues!' 
response_metadata={'token_usage': {'completion_tokens': 17,
 'prompt_tokens': 16, 'total_tokens': 33}, 'model_name': 
 'gpt-35-turbo', 'system_fingerprint': 'fp_811936bd4f', 
 'finish_reason': 'stop', 'logprobs': None} 
 id='run-a5488bb9-4160-4943-bde1-39fa8835e74f-0'
 usage_metadata={'input_tokens': 16, 'output_tokens': 17, 'total_tokens': 33}
"""

print(model_1.invoke(prompt_value))
"""
Sure! Why did the basketball player bring a ladder to the game?

Because he wanted to shoot some hoops!
"""
