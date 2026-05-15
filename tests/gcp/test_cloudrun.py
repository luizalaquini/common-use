import os
from dotenv import load_dotenv
from google.cloud import run_v2

# 1. Carrega as variáveis do .env
load_dotenv()
project_id = os.getenv("GCP_PROJECT_ID")
location = os.getenv("GCP_LOCATION") 

def test_cloudrun_connection():
    try:
        # 2. Inicializa o cliente do Cloud Run (v2)
        client = run_v2.ServicesClient()

        # 3. Define o caminho pai (projeto e localização)
        parent = f"projects/{project_id}/locations/{location}"

        print(f"--- Listando serviços do Cloud Run em {location} ---")

        # 4. Lista os serviços
        services = client.list_services(parent=parent)

        found = False
        for service in services:
            found = True
            print(f"Serviço encontrado: {service.name}")
            print(f"  URL: {service.uri}")
            print(f"  Última atualização: {service.update_time}")

        if not found:
            print(f"Conexão OK, mas nenhum serviço encontrado em {location}.")

    except Exception as e:
        print(f"Erro ao acessar o Cloud Run: {e}")

if __name__ == "__main__":
    test_cloudrun_connection()