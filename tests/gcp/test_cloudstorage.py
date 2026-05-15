import os
from dotenv import load_dotenv
from google.cloud import storage

# 1. Carrega as variáveis do .env
load_dotenv()
project_id = os.getenv("GCP_PROJECT_ID")

def test_gcs_connection():
    try:
        # 2. Inicializa o cliente do Storage
        # Ele usará automaticamente o 'application-default login' que você fez no gcloud
        client = storage.Client(project=project_id)

        print(f"--- Testando conexão com o projeto: {project_id} ---")

        # 3. Tenta listar os buckets do projeto
        buckets = list(client.list_buckets())

        if buckets:
            print("Conexão bem-sucedida! Buckets encontrados:")
            for bucket in buckets:
                print(f" - {bucket.name}")
        else:
            print("Conexão bem-sucedida, mas nenhum bucket foi encontrado neste projeto.")
            print("Dica: Crie um bucket no console para ver o nome listado aqui.")

    except Exception as e:
        print(f"Erro ao acessar o Cloud Storage: {e}")

if __name__ == "__main__":
    test_gcs_connection()