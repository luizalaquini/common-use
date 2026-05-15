import os
from dotenv import load_dotenv
import vertexai
from vertexai.generative_models import GenerativeModel

# 1. Carrega variáveis do arquivo .env
load_dotenv()
project_id = os.getenv("GCP_PROJECT_ID")
location = os.getenv("GCP_LOCATION")

# 2. Inicializa o SDK do Vertex AI
vertexai.init(project=project_id, location=location)

# 3. Instancia o modelo
model = GenerativeModel("gemini-2.5-flash-lite")

try:
    # 4. Tenta gerar conteúdo
    response = model.generate_content("Diga: Conexão Python-Vertex AI bem-sucedida!")
    print("-" * 30)
    print(f"RESPOSTA DO MODELO: {response.text}")
    print("-" * 30)
except Exception as e:
    print(f"Erro ao acessar o Vertex AI: {e}")