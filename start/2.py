# 使用 predict_message 处理消息列表
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from dotenv import load_dotenv
from langchain.schema import HumanMessage,SystemMessage

# 读取.env配置文件
load_dotenv()

llm = OpenAI()
chat_model = ChatOpenAI()

text = "制造多彩袜子的公司的好名字是什么?"
# 定义消息列表
messages = [
    SystemMessage("我将用西班牙语回答您"),
    HumanMessage(content=text)
]

print(llm.predict_messages(messages).content) # 彩虹袜子工坊
print(chat_model.predict_messages(messages).content) # "彩织足迹"