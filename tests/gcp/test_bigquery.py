import os
from dotenv import load_dotenv
from google.cloud import bigquery

# 1. Carrega as variáveis do .env
load_dotenv()
project_id = os.getenv("GCP_PROJECT_ID")

def test_bigquery_connection():
    try:
        # 2. Inicializa o cliente do BigQuery
        client = bigquery.Client(project=project_id)

        print(f"--- Testando conexão com BigQuery no projeto: {project_id} ---")

        # 3. Teste 1: Listar Datasets
        datasets = list(client.list_datasets())
        if datasets:
            print("Conexão estabelecida! Datasets encontrados:")
            for ds in datasets:
                print(f" - {ds.dataset_id}")
        else:
            print("Conexão estabelecida, mas não foram encontrados datasets privados.")

        # 4. Teste 2: Executar uma Query simples em dados públicos
        # Esta query conta linhas numa tabela pública de amostra
        query = "SELECT count(*) as total FROM `bigquery-public-data.usa_names.usa_1910_current` LIMIT 1"
        query_job = client.query(query)
        results = query_job.result()

        for row in results:
            print(f"Teste de Query: Sucesso! Total de linhas processadas na tabela pública: {row.total}")

    except Exception as e:
        print(f"Erro ao acessar o BigQuery: {e}")

if __name__ == "__main__":
    test_bigquery_connection()