from langchain.chains import LLMChain
from langchain_community.llms import OpenAI
import os
from dotenv import load_dotenv


# loading .env
load_dotenv()

from langchain_openai import ChatOpenAI
llm = ChatOpenAI(temperature=0)

from langchain.document_loaders import TextLoader

path = "data/general_data.txt"
loader = TextLoader(path)
documents = loader.load()

# document chunking
from langchain.text_splitter import CharacterTextSplitter
text_splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
chunks = text_splitter.split_documents(documents)

# setting up the vector store
from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma
db = Chroma.from_documents(chunks, OpenAIEmbeddings())

# retreival
retriever = db.as_retriever()

# augmented
from langchain.prompts import ChatPromptTemplate
template = """You are an assistant for question-answering tasks. 
Use the following pieces of retrieved context to answer the question. 
If you don't know the answer, just say that you don't know. 
Use three sentences maximum and keep the answer concise.
Question: {question} 
Context: {context} 
Answer:
"""
prompt = ChatPromptTemplate.from_template(template)

# generation
from langchain.schema.runnable import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
rag_chain = (
    {"context": retriever,  "question": RunnablePassthrough()} 
    | prompt 
    | llm
    | StrOutputParser() 
)

# handling user input
def handle_user_input():
    
    while True:
        input_str = input("Enter your message: ")
        if(input_str == "exit"):
            break
        response = rag_chain.invoke(input_str)
        print(response)

print("#====================================================================#")
print("Manish chatbot is ready. Exit the chatbot by typing 'exit'")
handle_user_input()