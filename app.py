from pyspark.sql import SparkSession
from pyspark.sql.functions import col

def iniciar_spark():
    return SparkSession.builder.appName("MeuTeste").getOrCreate()

def dobrar_valores(df):
    # Pega a coluna "valor" e multiplica por 2
    return df.withColumn("valor_dobrado", col("valor") * 2)
