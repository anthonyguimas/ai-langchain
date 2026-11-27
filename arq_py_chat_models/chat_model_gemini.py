import os
import time

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_google_genai.chat_models import GoogleAPIError

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

model_lite = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash-lite",
    timeout=20,
    max_retries=2,
    google_api_key=api_key,
)

model_flash = ChatGoogleGenerativeAI(
    model="gemini-3.8-flash",
    thinking_level="low",
    timeout=30,
    max_retries=2,
    google_api_key=api_key,
)

model_hydrogen = ChatGoogleGenerativeAI(
    model="gemini-4-hydrogen",
    timeout=30,
    max_retries=2,
    google_api_key=api_key,
)

model = model_lite.with_fallbacks([model_flash, model_hydrogen])
 
print("Enviando pergunta para o Gemini...")

for tentativa in range(1, 4):
    try:
        resposta = model.invoke("Olá como você está? Atualmente eu estou fazendo um projeto em langchain o que você acha disso?")
        break
    except GoogleAPIError as e:
        if "503" in str(e) and tentativa < 3:
            print(f"Servidores ocupados (503). Tentando novamente em 5s... ({tentativa}/3)")
            time.sleep(5)
        else:
            raise

print("--------RESPOSTA AIMessage:---------")
print(resposta)
print("-------------------------------------")

print("--------RESPOSTA Somente Texto:------")
print(resposta.text)
print("-------------------------------------")