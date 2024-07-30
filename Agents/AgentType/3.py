from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
from langchain.chains.llm import LLMChain
from langchain_core.output_parsers import StrOutputParser
load_dotenv()

model = ChatOpenAI()
output_parser = StrOutputParser()
prompt = ChatPromptTemplate.from_template("can you use Chinese to tell me a short joker about {topic}")
chain = LLMChain(
    llm=model,
    prompt=prompt,
    output_parser=output_parser

)
res = chain.invoke("鲁迅是谁")
# {'topic': '鲁迅是谁', 'text': '鲁迅是谁？他是一个文学家，也是一个思想家。有人说他是中国现代文学的奠基人，但有些人却说他是一个“鲁莽”的人。哈哈，你懂了吗？'}
print(res)