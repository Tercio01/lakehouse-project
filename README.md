# 🏗️ Lakehouse Data Pipeline Project

## 📊 Overview
Complete data lakehouse implementation with Bronze, Silver, and Gold layers using Apache Spark, Jupyter, and Docker.

[![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?logo=python&logoColor=white)]()
[![Spark](https://img.shields.io/badge/Apache_Spark-E25A1C?logo=apachespark&logoColor=white)]()
[![Docker](https://img.shields.io/badge/Docker-2496ED?logo=docker&logoColor=white)]()
[![Airflow](https://img.shields.io/badge/Apache_Airflow-017CEE?logo=apacheairflow&logoColor=white)]()
[![License](https://img.shields.io/badge/License-MIT-green)]()
[![Status](https://img.shields.io/badge/Status-Completed-brightgreen)]()


## 🎯 Project Architecture

📁 lakehouse-local/
├── 📊 data/ # Data layers (not versioned)
│ ├── bronze/ # Raw data in CSV
│ ├── silver/ # Cleaned data in Parquet
│ └── gold/ # Aggregated data for analysis
├── 📓 notebooks/ # Jupyter notebooks
│ ├── 01_bronze_to_silver.ipynb
│ └── 02_silver_to_gold.ipynb
├── 🐍 scripts/ # Python scripts
│ ├── data_generator.py
│ └── upload_to_adls.py
├── 🐳 docker-compose.yml
├── 📋 README.md
└── 🔧 .gitignore

## 🛠️ Technologies Used
- **Apache Spark**: Data processing and transformations
- **JupyterLab**: Interactive development
- **Docker**: Containerization
- **Parquet**: Columnar storage format
- **Python**: Data generation and scripting

## 📈 Data Pipeline
1. **Bronze Layer**: Raw CSV data generation
2. **Silver Layer**: Data cleaning and transformation
3. **Gold Layer**: Business analytics and aggregations

Pipeline Automation

    Data Generation: Automated data creation

    Bronze to Silver: Spark transformations

    Silver to Gold: Business analytics

    Scheduled: Daily pipeline execution

## 🔄 Orchestration with Airflow

The project includes Apache Airflow for pipeline orchestration:

```yaml
dags/
└── lakehouse_dag.py      # DAG for complete pipeline orchestration

## 🚀 Getting Started

### Prerequisites
- Docker and Docker Compose
- Python 3.8+
- Git

### Installation
```bash
# Clone the repository
git clone https://github.com/Tercio01/lakehouse-project.git
cd lakehouse-project

# Start services
docker-compose up -d

# Access JupyterLab
http://localhost:8889

Usage

    Generate sample data: python scripts/data_generator.py

    Run Bronze to Silver transformations: Execute 01_bronze_to_silver.ipynb

    Run Silver to Gold analytics: Execute 02_silver_to_gold.ipynb

📊 Features Implemented

    ✅ Synthetic e-commerce data generation

    ✅ Data cleaning and transformation

    ✅ Parquet format optimization

    ✅ Customer analytics

    ✅ Sales analysis by category

    ✅ Customer 360 view

## 📊 Project Metrics

- **Data Volume**: 5,000+ synthetic records generated
- **Transformations**: 10+ data processing operations
- **Technologies**: 5+ tools integrated (Spark, Docker, Airflow, etc.)
- **Containerization**: Full Docker compose setup
- **Automation**: Airflow DAG for complete orchestration
- **Testing**: CI/CD pipeline with GitHub Actions
- **Documentation**: Comprehensive README and technical docs

👨‍💻 Author

Tercio Alves Parente

    Email: tercio1parente@gmail.com

    LinkedIn: Tercio Alves Parente

    GitHub: Tercio01

## 🚀 Future Roadmap

- [ ] Real-time data streaming with Kafka
- [ ] Machine Learning integration
- [ ] Cloud deployment (AWS/Azure/GCP)
- [ ] Advanced monitoring with Grafana/Prometheus
- [ ] Data quality framework with Great Expectations
- [ ] Advanced analytics with dbt
- [ ] Kubernetes deployment
- [ ] Data catalog implementation

📄 License

This project is for portfolio and educational purposes.
🤝 Contributing

Feel free to fork this project and submit pull requests for any improvements.


