from openai import AzureOpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_KEY"),
    api_version="2023-12-01-preview",
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT")
)

DEPLOYMENT = os.getenv("AZURE_OPENAI_DEPLOYMENT_ID", "gpt-35-turbo")

def chat(question: str) -> str:
    resp = client.chat.completions.create(
        model=DEPLOYMENT,
        messages=[
            {"role": "system", "content": "Você é um assistente de estudos de IA generativa."},
            {"role": "user", "content": question}
        ]
    )
    return resp.choices[0].message.content

print("💬 Chatbot simples com Azure OpenAI\n")

while True:
    q = input("> ")
    if q.strip().lower() in {"sair", "exit"}:
        break
    print("🤖:", chat(q))
