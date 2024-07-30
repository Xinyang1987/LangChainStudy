# 文档转换器
# 意图:一旦加载了文档，您通常会希望对其进行转换，以更好地适应您的应用程序。最简单的例子是您可能希望将长文档拆分为更小的块，以适应您模型的上下文窗口。LangChain提供了许多内置的文档转换器，使得拆分、合并、过滤和其他文档操作变得容易。

from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import PyPDFLoader


text_spliter = RecursiveCharacterTextSplitter(
    chunk_size = 100,
    chunk_overlap = 20,
    length_function = len,
    add_start_index = True
)

loader = PyPDFLoader("./file/1.pdf")
fileData = loader.load_and_split(text_spliter)
print(fileData)
