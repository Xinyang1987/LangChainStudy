from langchain_openai import ChatOpenAI
from langchain.agents import initialize_agent,Tool
from dotenv import load_dotenv

load_dotenv()

def func_1(input):
    llms = ChatOpenAI()
    res = llms(input)
    return res

def func_2(input):
    llms = ChatOpenAI()
    res = llms(input)
    return res

tools = [
    Tool(
        name="tool_1",
        func=func_1,
        description="用于回答不含数字的题目"
    ),
    Tool(
        name="tool_2",
        func=func_2,
        description="用于回答含数字的题目"
    )
]

llm = ChatOpenAI()
agent_chain = initialize_agent(
    tools,
    llm,
    verbose=True
)

response = agent_chain.invoke(input="鲁迅是谁")
print(response)
# {'input': '鲁迅是谁', 'output': '鲁迅是中国现代文学史上具有重要影响的作家、思想家和文化评论家。'}