from pyspark.sql import SparkSession
import os

spark = SparkSession.builder.appName("TestSilver").getOrCreate()

silver_path = "/home/jovyan/data/silver/"

try:
    # Testar leitura
    df = spark.read.parquet(f"{silver_path}orders")
    print(f"✅ Success! Orders silver: {df.count()} records")
    df.show(2)
except Exception as e:
    print(f"❌ Error: {str(e)}")
    print("Tentando listar o diretório silver:")
    print(os.listdir(silver_path))
