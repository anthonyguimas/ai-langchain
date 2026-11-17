from dotenv import load_dotenv
from anthropic import Anthropic
load_dotenv()

model = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

result = model.invoke("Este é um teste. Se você recebeu a requisição responda 'Teste OK'. ")