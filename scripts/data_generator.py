import pandas as pd
from faker import Faker
import random
from datetime import datetime, timedelta
import os
import boto3
from io import BytesIO

fake = Faker('pt_BR')

def generate_ecommerce_data():
    """Gera dados completos de e-commerce"""
    
    # Gerar produtos
    categories = ['Eletrônicos', 'Livros', 'Roupas', 'Casa', 'Esportes', 'Brinquedos']
    products = []
    for i in range(100):
        products.append({
            'product_id': i + 1,
            'product_name': f"{fake.word().capitalize()} {fake.word().capitalize()}",
            'product_category': random.choice(categories),
            'product_price': round(random.uniform(10, 500), 2),
            'cost_price': round(random.uniform(5, 300), 2),
            'stock_quantity': random.randint(0, 1000),
            'supplier': fake.company()
        })
    
    # Gerar clientes
    customers = []
    for i in range(200):
        signup_date = fake.date_between(start_date='-2y', end_date='today')
        customers.append({
            'customer_id': i + 1,
            'customer_name': fake.name(),
            'customer_email': fake.email(),
            'customer_city': fake.city(),
            'customer_state': fake.state_abbr(),
            'signup_date': signup_date.strftime('%Y-%m-%d'),
            'customer_segment': random.choice(['standard', 'premium', 'vip']),
            'credit_score': random.randint(300, 850)
        })
    
    # Gerar pedidos
    orders = []
    for i in range(5000):
        order_date = fake.date_time_between(start_date='-30d', end_date='now')
        orders.append({
            'order_id': i + 1,
            'customer_id': random.randint(1, 200),
            'product_id': random.randint(1, 100),
            'quantity': random.randint(1, 10),
            'order_amount': round(random.uniform(20, 1000), 2),
            'order_date': order_date.strftime('%Y-%m-%d %H:%M:%S'),
            'order_status': random.choice(['pending', 'completed', 'cancelled', 'shipped']),
            'payment_method': random.choice(['credit_card', 'debit_card', 'paypal', 'bank_transfer'])
        })
    
    return {
        'products': pd.DataFrame(products),
        'customers': pd.DataFrame(customers),
        'orders': pd.DataFrame(orders)
    }

def upload_to_minio(df, bucket_name, file_name, format='csv'):
    """Faz upload de DataFrame para MinIO"""
    try:
        # Configurar cliente S3
        s3 = boto3.client(
            's3',
            endpoint_url='http://localhost:9000',
            aws_access_key_id='admin',
            aws_secret_access_key='password123',
            config=boto3.session.Config(signature_version='s3v4')
        )
        
        # Converter DataFrame para bytes
        if format == 'csv':
            csv_buffer = BytesIO()
            df.to_csv(csv_buffer, index=False)
            content = csv_buffer.getvalue()
            content_type = 'text/csv'
        else:  # parquet
            parquet_buffer = BytesIO()
            df.to_parquet(parquet_buffer, index=False)
            content = parquet_buffer.getvalue()
            content_type = 'application/parquet'
        
        # Fazer upload
        s3.put_object(
            Bucket=bucket_name,
            Key=file_name,
            Body=content,
            ContentType=content_type
        )
        print(f"Uploaded {file_name} to {bucket_name}")
        
    except Exception as e:
        print(f"Error uploading {file_name}: {str(e)}")

def main():
    """Função principal"""
    print("Iniciando geração de dados...")
    
    # Gerar dados
    data = generate_ecommerce_data()
    
    # Criar diretório local
    os.makedirs('../data/bronze', exist_ok=True)
    
    # Salvar localmente
    data['orders'].to_csv('../data/bronze/orders.csv', index=False)
    data['customers'].to_csv('../data/bronze/customers.csv', index=False)
    data['products'].to_csv('../data/bronze/products.csv', index=False)
    
    data['orders'].to_parquet('../data/bronze/orders.parquet', index=False)
    data['customers'].to_parquet('../data/bronze/customers.parquet', index=False)
    data['products'].to_parquet('../data/bronze/products.parquet', index=False)
    
    # Fazer upload para MinIO
    print("Fazendo upload para MinIO...")
    upload_to_minio(data['orders'], 'bronze', 'orders.csv')
    upload_to_minio(data['customers'], 'bronze', 'customers.csv')
    upload_to_minio(data['products'], 'bronze', 'products.csv')
    
    upload_to_minio(data['orders'], 'bronze', 'orders.parquet', 'parquet')
    upload_to_minio(data['customers'], 'bronze', 'customers.parquet', 'parquet')
    upload_to_minio(data['products'], 'bronze', 'products.parquet', 'parquet')
    
    # Estatísticas
    print("\n✅ Dados gerados com sucesso!")
    print(f"Orders: {len(data['orders'])} registros")
    print(f"Customers: {len(data['customers'])} registros")
    print(f"Products: {len(data['products'])} registros")
    print("Arquivos salvos localmente e no MinIO")

if __name__ == "__main__":
    main()
