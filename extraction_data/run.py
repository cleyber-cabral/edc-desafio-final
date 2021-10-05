import logging
import os
import zipfile
import requests
from io import BytesIO
from google.cloud import storage

# Cria um diretório para armazenar o conteúdo do enade
os.makedirs('../data/educ_superior', exist_ok=True)

print("Extracting data...")

# Define a url e faz o download do conteúdo
url = "https://download.inep.gov.br/microdados/microdados_educacao_superior_2019.zip"
filebytes = BytesIO(requests.get(url).content)

print("Unzip files...")
# Extrai o conteúdo do zipfile
myzip = zipfile.ZipFile(filebytes)
myzip.extractall('../data/educ_superior')

print("Upload to GCS...")

client = storage.Client()

bucket = client.get_bucket('desafio-igti')
blob = bucket.get_blob('../data/educ_superior')

print("Upload realizado com sucesso !")