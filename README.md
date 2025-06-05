# 💼 AML Data Engineering Pipeline – Hadoop, AWS, Snowflake

This portfolio project simulates a real-world **Anti-Money Laundering (AML) transaction monitoring system**, designed to detect suspicious financial activities using modern big data technologies. Built with Hadoop, Spark, AWS services, and Snowflake, the project showcases scalable data pipeline design, rule-based detection logic, and visualization via QuickSight.

---

## 🎯 Objective

To design and implement a **multi-layered AML data pipeline** that:
- Ingests and processes a large synthetic financial transactions dataset
- Applies AML typologies to detect suspicious behavior
- Stores curated data in Snowflake for rule-based and ML-based anomaly detection
- Visualizes AML alerts and KPIs using AWS QuickSight

---

## 🧰 Tech Stack

| Layer              | Tools & Technologies                           |
|-------------------|-------------------------------------------------|
| Storage           | AWS S3 (data lake)                              |
| Processing        | AWS EMR, Apache Spark, Hadoop, PySpark          |
| Warehousing       | Snowflake (SQL, Snowpark)                       |
| Automation        | AWS Glue, IAM, Lambda                           |
| Visualization     | AWS QuickSight                                  |
| Data Source       | SAML-D (Synthetic AML Dataset)                  |

---

## 🗂 Project Architecture

```
Raw Data (SAML-D)
    ↓
AWS S3 (Landing Zone)
    ↓
AWS EMR (Spark) – Cleanse, Transform, Feature Engineer
    ↓
AWS S3 (Processed Zone - Parquet)
    ↓
Snowflake – Transactions + Alerts Tables
    ↓
Snowflake SQL Rules & Optional ML (Snowpark)
    ↓
AWS QuickSight – AML Dashboard & KPIs
```

---

## 🧱 Data Pipeline Modules

1. **Ingestion Layer** – Upload SAML-D dataset to S3 (`landing/`)
2. **Processing Layer (EMR + Spark)**
  - Cleanses raw data
  - Engineers AML-relevant features (e.g., structuring flags, geo-risk)
  - Writes enriched Parquet files to `processed/`
3. **Data Warehouse Layer (Snowflake)**
  - Loads data from S3 into Snowflake
  - Applies AML detection rules
  - Stores flagged transactions in `ALERTS` table
4. **Visualization Layer (QuickSight)**
  - Connects to Snowflake
  - Displays AML alerts, risk KPIs, and trends
  - Supports threshold-based email alerts

---

## 📊 AML Typologies Detected

- **Structuring/Smurfing** – Transactions just below regulatory thresholds
- **Rapid Fund Movement** – Quick withdrawal/transfer after deposits
- **High-Risk Geographies** – Transactions involving flagged countries
- **Unusual Activity** – Deviations from historical transaction behavior
- **Funnel Accounts** – Multiple accounts feeding into or out of one account

---

## 🧪 Sample Detection Rule in Snowflake SQL

```sql
INSERT INTO ALERTS (TRANSACTION_ID, ALERT_TYPE, RULE_ID, DETAILS)
SELECT TRANSACTION_ID, 'Structuring', 'RULE_STRUCT_001',
       CONCAT('Amount $', AMOUNT::STRING, ' is near reporting threshold.')
FROM TRANSACTIONS
WHERE AMOUNT BETWEEN 9000 AND 9999.99
  AND PAYMENT_TYPE = 'Cash Deposit';
```

---

## 📁 Project Structure

```
aml-pipeline/
├── ingestion/
│   └── upload_to_s3.py
├── processing/
│   └── spark_transformations.py
├── snowflake/
│   ├── ddl/
│   │   └── create_tables.sql
│   └── rules/
│       └── aml_rules.sql
├── dashboard/
│   └── quicksight_design.json
├── data/
│   └── sample_saml_d.csv
├── README.md
└── requirements.txt
```

---

## 📚 Dataset

**SAML-D Dataset**
- ~9.5 million synthetic financial transactions
- 0.1% labeled as laundering (realistic class imbalance)
- Features include account IDs, transaction amounts, geo-locations, payment types, and laundering labels
- Publicly available on [Kaggle](https://www.kaggle.com/datasets)

---

## 📈 Future Enhancements

- 🔄 Real-time detection with AWS Kinesis + Spark Streaming
- 🤖 ML model scoring in Snowflake using Snowpark (e.g. Isolation Forest)
- 🧠 Graph-based laundering ring detection using GraphFrames or NetworkX
- 🔐 Role-based access + data governance with Lake Formation and Snowflake policies

---

## 🧠 Author

**Cedric Nyagatare**  
Incoming Data Engineer @ Citi (AML Systems)  
GitHub: [@cedricnyagatare](https://github.com/cedricnyagatare)

---

## 📜 License

This project is for educational and demonstration purposes only.  
All synthetic data used complies with privacy-safe guidelines.

---
