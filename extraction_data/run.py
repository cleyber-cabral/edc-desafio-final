import logging
import os
import zipfile
import requests
from io import BytesIO
from google.cloud import storage

# Cria um diretório para armazenar o conteúdo do enade

base_path = '../data/educ_superior'
os.makedirs(base_path, exist_ok=True)

print("Extracting data...")

# Define a url e faz o download do conteúdo
url = "https://download.inep.gov.br/microdados/microdados_educacao_superior_2019.zip"
filebytes = BytesIO(requests.get(url).content)

print("Unzip files...")
# Extrai o conteúdo do zipfile
myzip = zipfile.ZipFile(filebytes)
myzip.extractall('../data/educ_superior')


print("Upload to GCS...")


client = storage.Client(project = 'edc-desafio-final')

bucket = client.get_bucket('desafio-igti')
filename = "%s/%s" % ("raw-data", "ALUNO_2019.csv")
blob = bucket.blob(filename)
blob.upload_from_filename('../data/educ_superior/Microdados_Educaç╞o_Superior_2019/dados/SUP_ALUNO_2019.csv')

filename2 = "%s/%s" % ("raw-data", "CURSO_2019.csv")
blob2 = bucket.blob(filename2)
blob2.upload_from_filename('../data/educ_superior/Microdados_Educaç╞o_Superior_2019/dados/SUP_CURSO_2019.csv')

filename3 = "%s/%s" % ("raw-data", "IES_2019.csv")
blob3 = bucket.blob(filename3)
blob3.upload_from_filename('../data/educ_superior/Microdados_Educaç╞o_Superior_2019/dados/SUP_IES_2019.csv')

filename4 = "%s/%s" % ("raw-data", "DOCENTE_2019.csv")
blob4 = bucket.blob(filename4)
blob4.upload_from_filename('../data/educ_superior/Microdados_Educaç╞o_Superior_2019/dados/SUP_DOCENTE_2019.csv')

filename5 = "%s/%s" % ("raw-data", "LOCAL_OFERTA_2019.csv")
blob5 = bucket.blob(filename5)
blob5.upload_from_filename('../data/educ_superior/Microdados_Educaç╞o_Superior_2019/dados/SUP_IES_2019.csv')

filename6 = "%s/%s" % ("raw-data", "IES_2019.csv")
blob6 = bucket.blob(filename6)
blob6.upload_from_filename('../data/educ_superior/Microdados_Educaç╞o_Superior_2019/dados/TB_AUX_CINE_BRASIL_2019.csv')

print("Upload realizado com sucesso !")