# 文本嵌入模型
from langchain_community.embeddings import BaichuanTextEmbeddings
from langchain.embeddings import HuggingFaceBgeEmbeddings
from dotenv import load_dotenv
load_dotenv()


embedding_model = HuggingFaceBgeEmbeddings()

embedded_query = embedding_model.embed_query("What was the name mentioned in the conversation?")
print(embedded_query[:5])