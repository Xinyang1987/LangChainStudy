# 接口 Runnable协议
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI()
prompt = ChatPromptTemplate.from_template("tell me a joke about {topic}")
chain = prompt | model

response = chain.invoke("basketball")
"""
content="Why did the basketball go to the team's party? Because it heard they were going to have a ball!" 
response_metadata={'token_usage': {'completion_tokens': 22, 'prompt_tokens': 13, 'total_tokens': 35},
 'model_name': 'gpt-35-turbo', 'system_fingerprint': 'fp_811936bd4f', 'finish_reason': 'stop', 'logprobs': None}
   id='run-e83342dd-58fa-4508-939e-0f7b3c57070d-0' usage_metadata={'input_tokens': 13, 'output_tokens': 22, 'total_tokens': 35}
"""

re_1 = chain.batch([{"topic": "bears"}, {"topic": "cats"}])
"""
[AIMessage(content="Sure, here's a bear joke for you:\n\nWhy did the bear dissolve in water?\n\nBecause it was polar!", 
response_metadata={'token_usage': {'completion_tokens': 23, 'prompt_tokens': 6, 'total_tokens': 29},
 'model_name': 'gpt-3.5-turbo', 'system_fingerprint': None, 'finish_reason': 'stop', 'logprobs': None}, 
 id='run-02f7461d-0f93-4ddc-bf9b-0bdd2774e82a-0', usage_metadata={'input_tokens': 6, 'output_tokens': 23, 'total_tokens': 29}),

 AIMessage(content='Why was the cat sitting on the computer?\n\nBecause it wanted to keep an eye on the mouse!',
 response_metadata={'token_usage': {'completion_tokens': 20, 'prompt_tokens': 13, 'total_tokens': 33},
'model_name': 'gpt-35-turbo', 'system_fingerprint': 'fp_811936bd4f', 'finish_reason': 'stop', 'logprobs': None},
id='run-6cce3563-2058-4aa8-9515-1590d41c8b8c-0', usage_metadata={'input_tokens': 13, 'output_tokens': 20, 'total_tokens': 33})]
"""


