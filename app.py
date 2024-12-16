# import os
# from langchain_core.prompts import ChatPromptTemplate
# from langchain_groq import ChatGroq

# human_prompt = input("Enter your prompt: ")
# gorq_apiKey = os.getenv("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")

# chat = ChatGroq(temperature=0, groq_api_key=gorq_apiKey, model_name="mixtral-8x7b-32768")

# system = "You are a superintelligent and helpful assistant."
# human = "{text}"
# prompt = ChatPromptTemplate.from_messages([("system", system), ("human", human)])

# chain = prompt | chat
# message = chain.invoke({"text": human_prompt})
# print("JARVIS:" + message.content)


from flask import Flask
app=Flask(__name__)
@app.route('/')
def hello():
    return "Hello World"