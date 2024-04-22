from langchain.chains import LLMChain
from langchain_community.llms import OpenAI
import os
from dotenv import load_dotenv


# loading .env
load_dotenv()

from langchain_openai import ChatOpenAI
openai = ChatOpenAI()