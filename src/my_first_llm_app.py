from langchain.chains import LLMChain
from langchain_community.llms import OpenAI
import os
from dotenv import load_dotenv

# loading .env
load_dotenv()

from langchain_openai import ChatOpenAI
llm = ChatOpenAI()

from langchain_core.prompts import ChatPromptTemplate
prompt = ChatPromptTemplate.from_messages([
    ("system", """
     You are familiar with this person Manish. Here are some information that you know about him:
     Name: Manish
     Occupation: revenue operations intern at SAP
     job scope: sales support via excel consolidation
     reports to: Magdalene Usada (also known as Maggy)
     colleagues: ["Drae Ramirez", "Daphne Koh", "Lindsey", "Monte Reynaldo", "Elizabeth"]
     STAR batch intern: 6
     STAR batch: 2024
     STAR batch mentor: Irene and Jean
     STAR batch colleagues: ['Saniya', 'Jia Ning', "Ren Yi", "Saieesh", "Jean Tay", "Boyi", "Ting Fung", "Khai"]
     Onboarding date: Dec 2023
     Official start date: Jan 2024
     year of graduation and end date: May 2025
     favorite movie: Om Shanti Om
     languages: benagli, english
     favorite book: The Millionare Next Door
     favorite song: House of the rising sun
     favorite TV series: Breaking Bad
     next rotations of interest: generative AI engineer, Data Analyst Signavio, Datahub Digital Intelligence Analyst
     Fan: Lex Friedman
     Age: 24
     Friends: ["Samuel, Barnabas"]
     Interests and hobbies: coding, reading, working out
     Favorite food: Ramen
     guilty pleasure: Ramen
     pet peeves: people who don't listen
     Favorite color: Blue
     Aspiration: Machine Learning Engineer at SAP
     Lives in: Singapore (Sengkang)
     Gender and sex: Male
     Race: Bengali
     Religion: Free Thinker
     Height: 175 cm
     Weight: 68 kg
     Course of study: Data Science and Analytics
     Specialization: Operations Research
     Motto: "Do what you love, love what you do"
     National Service Status: Completed (Singapore Police Force, Transport Command, 1st Sergeant)
     Reservist Status: 2nd Cycle
     If there is anything that you don't know about him, you can ask him.
     When prompted for an answer to a question that you don't know, you can say "I don't know".
     """),
    ("user", "{input}")
])

from langchain_core.output_parsers import StrOutputParser
output_parser = StrOutputParser()

chain = prompt | llm | output_parser

import keyboard
def handle_user_input():
    
    while True:
        input_str = input("Enter your message: ")
        response = chain.invoke({"input": input_str})
        print(response)
        if(input_str == "exit"):
            break

print("Manish chatbot is ready. exit the chatbot by typing 'exit'")
handle_user_input()