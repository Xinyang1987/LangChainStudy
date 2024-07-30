# 会话
from langchain.agents import Tool,AgentType,initialize_agent
from langchain.memory import ConversationBufferMemory
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()

def solveMath(input):
    return "this is a Math question"

def solveChinese(input):
    return "this is a chinese question"

tools = [
    # 在观察工具的输出后，代理可以决定是使用该输出还是自己生成一个回应。
    Tool(
        name="math",
        func=solveMath,
        description="使用该工具回答数学问题"
    ),
    Tool(
        name="chinese",
        func=solveChinese,
        description="使用该工具回答文学相关问题"
    )
]
"""
LangChain 框架允许 AI 代理将工具输出与其自身的推理能力相结合。因此，即使工具没有提供直接的答案（例如 getStr() 的输出）
，代理仍然能够处理问题并生成合适的回应。这种设计有助于确保 AI 能够在工具功能有限或不够全面时，依然提供有用的答案。
"""

memory = ConversationBufferMemory(memory_key="chat_history")

llm = ChatOpenAI()
agent_chain = initialize_agent(
    tools,
    llm,
    agent=AgentType.CONVERSATIONAL_REACT_DESCRIPTION,
    verbose=True,
    memory=memory
)

agent_chain.run(input="1+1=2怎么解释")