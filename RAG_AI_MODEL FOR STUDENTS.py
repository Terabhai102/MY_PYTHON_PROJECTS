import pandas as pd
from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

CSV = 'PCM 11.csv'
df = pd.read_csv(CSV,encoding='utf-8')
markdown_context = df.to_markdown(index=False)

prompt_template = ChatPromptTemplate.from_messages([
    ("system", (
        "You are an AI assistant designed for helping Indian Class 11 Science students.\n"
        "Use the clean PCM formula database provided below to answer the student's question.\n\n"
        "CRITICAL RULES:\n"
        "1. Extract the exact variables, equations, and constants from the database.\n"
        "2. Do not attempt to compute complex numerical problems. Only set up the equation.\n"
        "3. If the formula is not present in the database, reply with 'This formula is not in my database yet.'\n"
        "4. BE KIND AND ALWAYS ENCOURAGE THEM FOR BETTER.\n\n"
        "FORMULA DATABASE:\n{csv_data}"
    )),
    ("human", "{question}")
])

llm = OllamaLLM(model="llama3.2", base_url="http://localhost:11434")
chain = prompt_template | llm

print("YOUR SMART CLASS AI IS READY :) (type q to exit)")

while True:
    user_input = input("\nYou: ").strip()

    if user_input.lower() == "q":
        print("Goodbye! Study hard!")
        break

    if not user_input:
        continue

    print("ai typing......")
    response = chain.invoke({
        "csv_data": markdown_context,
        "question": user_input
    })

    print("\nAssistant:")
    print(response)
    print("-" * 50)




