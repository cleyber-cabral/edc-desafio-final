from pyspark import SparkContext, SparkConf
from pyspark.sql import SparkSession
import os

gcp_credentials = os.environ['GOOGLE_APPLICATION_CREDENTIALS']

project_id = "edc-desafio-igti"
bucket = 'desafio-igti'

# set conf
conf = (
    SparkConf()
        .set("spark.haddop.fs.gs.project.id", project_id)
        .set("spark.haddop.fs.gs.system.bucket", bucket)
)

sc = SparkContext(conf=conf).getOrCreate()

if __name__ == "__main__":

    spark = SparkSession\
            .builder\
            .appName("Educ_Superior")\
            .getOrCreate()

    spark.sparkContext.setLogLevel("WARN")

    df = (
        spark
        .read
        .format("csv")
        .options(header='true', inferSchema='true', delimiter='|')
        .load("gs://desafio-igti/raw-data/ALUNO_2019.csv")
    )

    df.printSchema()
    (df
     .write
     .mode("overwrite")
     .format("parquet")
     .save("gs://desafio-igti/processing/Aluno")
    )

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

    spark.stop()    