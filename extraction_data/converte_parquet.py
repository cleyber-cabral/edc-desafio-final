# Comentário para modificar o arquivo .py
from pyspark import SparkConf
from pyspark.sql.functions import mean, max, min, col, count
from pyspark.sql import SparkSession
from io import BytesIO
from google.cloud import storage

spark = (
    SparkSession.builder.appName("ExerciseSpark")
    .getOrCreate()
)

project_id = "edc-desafio-igti"
bucket = 'desafio-igti'

# # set conf
# conf = (
#     SparkConf()
#         .set("spark.haddop.fs.gs.project.id", project_id)
#         .set("spark.haddop.fs.gs.system.bucket", bucket)
# )

    # df = (
    #     spark
    #     .read
    #     .format("csv")
    #     .options(header='true', inferSchema='true', delimiter='|')
    #     .load("gs://desafio-igti/raw-data/ALUNO_2019.csv")
    # )

    # df.printSchema()
    # (df
    #  .write
    #  .mode("overwrite")
    #  .format("parquet")
    #  .save("gs://desafio-igti/processing/Aluno")
    # )

df = (
        spark
        .read
        .format("csv")
        .options(header='true', inferSchema='true', delimiter='|')
        .load("gs://desafio-igti/raw-data/CURSO_2019.csv")
    )

df.printSchema()
(df
     .write
     .mode("overwrite")
     .format("parquet")
     .save("gs://desafio-igti/processing/Curso")
)

df = (
        spark
        .read
        .format("csv")
        .options(header='true', inferSchema='true', delimiter='|')
        .load("gs://desafio-igti/raw-data/DOCENTE_2019.csv")
)

df.printSchema()
(df
     .write
     .mode("overwrite")
     .format("parquet")
     .save("gs://desafio-igti/processing/Docente")
)

print("*********************")
print("Escrito com sucesso!")
print("*********************")