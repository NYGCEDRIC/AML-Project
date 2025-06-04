# 💼 Anti-Money Laundering (AML) Data Engineering Pipeline

This is a real-world data engineering project simulating AML (Anti-Money Laundering) transaction monitoring, built using:
- Apache Spark & Hive (Hadoop Ecosystem)
- AWS (S3, Lambda, EMR)
- Snowflake (Data Warehousing)

## 🔍 Objective
To ingest, transform, and analyze large-scale financial transactions and detect suspicious patterns using both rule-based and ML-based anomaly detection.

## 🧱 Tech Stack
- **Big Data:** Apache Spark, Hive
- **Cloud:** AWS S3, Lambda, EMR
- **Warehouse:** Snowflake
- **Orchestration & Automation:** AWS Lambda, Shell Scripts
- **Language:** Python (PySpark), SQL

## 🗂️ Project Structure
aml-pipeline/
│
├── ingestion/
│ └── lambda_s3_trigger.py
├── processing/
│ └── spark_etl.py
├── detection/
│ └── anomaly_detection.py
├── snowflake/
│ └── snowpipe_setup.sql
├── data/
│ └── sample_data.csv
├── README.md
└── requirements.txt


## 📊 Features
- Ingests transaction logs into S3
- Cleans and enriches data using PySpark on EMR
- Detects suspicious activity via:
    - Rule-based logic (e.g., structuring, high value transfers)
    - Isolation Forest anomaly detection
- Loads results into Snowflake for analysis & BI

## 🚀 To Run
1. Set up AWS CLI and configure EMR cluster.
2. Deploy Lambda trigger for ingestion.
3. Run `spark_etl.py` with sample data.
4. Load output to Snowflake using `snowpipe_setup.sql`.

## 📈 Future Improvements
- Real-time ingestion via Kinesis
- Graph-based laundering ring detection
- Streamlit dashboard for visual analytics

---

## 🧠 Author

Cedric Nyagatare
Data Engineer @ Citi (AML Team)

---

## 📄 License

MIT License
