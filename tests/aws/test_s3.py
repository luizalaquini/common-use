import os
import boto3
from dotenv import load_dotenv
from urllib.parse import urlparse
from botocore.exceptions import NoCredentialsError, ClientError

# Carrega as variáveis do arquivo .env para o ambiente do sistema
load_dotenv()

def test_s3_connection():
    # Obtém a URI da variável de ambiente
    s3_uri = os.getenv('S3_BUCKET_URI')

    if not s3_uri:
        print("Erro: A variável S3_BUCKET_URI não foi encontrada no arquivo .env")
        return

    parsed_uri = urlparse(s3_uri)
    bucket_name = parsed_uri.netloc
    prefix = parsed_uri.path.lstrip('/')

    s3 = boto3.client('s3')

    try:
        print(f"--- Conectando ao Bucket: {bucket_name} ---")
        
        # Listagem usando Paginator
        paginator = s3.get_paginator('list_objects_v2')
        pages = paginator.paginate(Bucket=bucket_name, Prefix=prefix)

        for page in pages:
            if 'Contents' in page:
                for obj in page['Contents']:
                    print(f"Arquivo: {obj['Key']} | Tamanho: {obj['Size']} bytes")
            else:
                print("Conexão OK, mas nenhum arquivo foi encontrado neste caminho.")

    except ClientError as e:
        print(f"Erro de Cliente AWS: {e.response['Error']['Message']}")
    except Exception as e:
        print(f"Erro inesperado: {e}")

if __name__ == "__main__":
    test_s3_connection()