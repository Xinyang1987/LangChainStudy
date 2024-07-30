# 输出解析器
from langchain.schema import BaseOutputParser

class CommaSeparatedListOutputParser(BaseOutputParser):
    def parse(self,text:str):
        return text.strip().split(",")
    
print(CommaSeparatedListOutputParser().parse("hi,bye"))