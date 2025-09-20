from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Test").getOrCreate()
df = spark.createDataFrame([(1, "test"), (2, "data")], ["id", "value"])
print("✅ Spark funcionando!")
print(f"Registros: {df.count()}")
df.show()
spark.stop()
