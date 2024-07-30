# langchain 链
from langchain.chat_models import ChatOpenAI
from dotenv import load_dotenv
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate
)
from langchain.chains.llm import LLMChain
from langchain.schema import BaseOutputParser

load_dotenv()

class CommaSeparatedListOutputParser(BaseOutputParser):
    """Parse the output of an LLM call to a comma-separated list."""

    def parse(self, text: str):
        """Parse the output of an LLM call."""
        return text.strip().split(", ") # 将结果分割并返回列表

template = """您是一个有用的助手，可以生成逗号分隔的列表。
用户将传入一个类别，您应该在逗号分隔的列表中在该类别中生成 5 个对象。
只需要返回一个逗号分隔的列表，仅此而已。"""

system_message_prompt = SystemMessagePromptTemplate.from_template(template)
human_template = "{text}"
human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)
chat_prompt = ChatPromptTemplate.from_messages([system_message_prompt,human_message_prompt])

chain = LLMChain(
    llm = ChatOpenAI(),
    prompt = chat_prompt,
    output_parser = CommaSeparatedListOutputParser()
)

print(chain.run("colors")) # ['red', 'blue', 'green', 'yellow', 'purple']
