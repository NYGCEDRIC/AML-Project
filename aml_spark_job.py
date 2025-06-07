from pyspark.sql import SparkSession, functions as F, Window

spark = SparkSession.builder.appName("AML_Data_Processing").getOrCreate()

# 1. Read raw CSV from landing zone
raw = (spark.read
             .option("header", "true")
             .option("inferSchema", "true")   # swap for explicit schema later
             .csv("s3://aml-project-cedric/landing/SAML-D.csv"))

# 2. Clean + cast
df = (raw
      .withColumn("transaction_ts_str",
                  F.concat_ws(" ", "Date", "Time"))
      .withColumn("transaction_timestamp",
                  F.to_timestamp("transaction_ts_str", "yyyy-MM-dd HH:mm:ss"))
      .drop("transaction_ts_str"))

# 3. Feature engineering (examples from roadmap)
df = (df
      .withColumn("transaction_hour", F.hour("transaction_timestamp"))
      .withColumn("transaction_dow", F.dayofweek("transaction_timestamp"))
      .withColumn("is_structuring_amount",
                  (F.col("Amount") > 9000) & (F.col("Amount") < 10000))
      .withColumn("is_sender_high_risk",
                  F.col("Sender_bank_location").isin("IRN", "AFG", "PRK"))
      )

# Rolling 24h txn count per sender
w24h = (Window.partitionBy("Sender_account")
              .orderBy(F.col("transaction_timestamp").cast("long"))
              .rangeBetween(-24*60*60, 0))
df = df.withColumn("sender_txn_count_24h", F.count("*").over(w24h))

# 4. Write back as Parquet
(df.repartition(1)             # small dev cluster; drop for prod
   .write
   .mode("overwrite")
   .parquet("s3://aml-project-cedric/processed/transactions_enriched/"))

spark.stop()
