# 🏗️ Lakehouse Data Pipeline Project

## 📊 Overview
Complete data lakehouse implementation with Bronze, Silver, and Gold layers using Apache Spark, Jupyter, and Docker.

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

👨‍💻 Author

Tercio Alves Parente

    Email: tercio1parente@gmail.com

    LinkedIn: Tercio Alves Parente

    GitHub: Tercio01

📄 License

This project is for portfolio and educational purposes.
🤝 Contributing

Feel free to fork this project and submit pull requests for any improvements.


