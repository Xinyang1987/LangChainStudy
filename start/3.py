# 提示模板
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate # OpenAI 提示模板
from langchain.prompts import ChatPromptTemplate # ChatOpenAI 提示模板

# 读取.env配置文件
load_dotenv()

llm = OpenAI()
chat_model = ChatOpenAI()

prompt = PromptTemplate.from_template("哪个城市适合{sport}") # such as 哪个城市适合{sport},使用{style}回答
human_message = prompt.format(
    sport="冲浪",
    # style
    # other
    # ...all each valible need to appear in str
)

chat_prompt = ChatPromptTemplate.from_template("哪个城市适合{doing}")
human_message_1 = chat_prompt.format_messages(
    doing="学习",
    # style
    # other
)

if __name__ == "__main__":
    # print(llm(human_message))
    print((chat_model(human_message_1)).content)

"""
冲浪是一项受欢迎的水上运动，适合在海岸线较长，有着稳定的海浪和适合冲浪的海滩的城市。以下是几个适合冲浪的城市：
1. 澳大利亚悉尼
澳大利亚悉尼是一个著名的冲浪目的地，拥有多处适合冲浪的海滩，如曼利海滩、邦迪海滩和弗朗茨·约瑟夫海滩。这里的海浪稳定，适合不同水平的冲浪者。
2. 美国夏威夷
夏威夷拥有世界级的冲浪场所，如北岸的邦波滩和威基基滩。这里的海浪强劲


不同城市有不同的学习环境和资源，因此适合学习的城市也会有所不同。一般来说，一些大城市如北京、上海、广州等拥有更多的优质学校和教育资源，适合深造和专业学习。而一些小城市或者乡村地
区可能更适合专注研究和自主学习，环境相对宁静适合深入思考和学习。最适合学习的城市还是要根据个人的学习目标和需求来选择。
"""