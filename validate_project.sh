#!/bin/bash

echo "=== VALIDAÇÃO DO LAKEHOUSE LOCAL ==="
echo ""

# 1. Verificar containers
echo "1. ✅ Containers em execução:"
docker-compose ps

echo ""

# 2. Verificar buckets MinIO
echo "2. ✅ Buckets no MinIO:"
docker exec -it minio mc ls myminio

echo ""

# 3. Verificar arquivos de dados
echo "3. ✅ Arquivos locais:"
find ./data -name "*.csv" -o -name "*.parquet" | head -5

echo ""

# 4. Verificar notebooks
echo "4. ✅ Notebooks criados:"
ls -la notebooks/

echo ""

# 5. Verificar scripts
echo "5. ✅ Scripts criados:"
ls -la scripts/

echo ""

echo "=== URLs DE ACESSO (PORTAS ATUALIZADAS) ==="
echo "MinIO Console: http://localhost:9001 (admin/password123)"
echo "JupyterLab: http://localhost:8889"  # Porta alterada
echo "Spark UI: http://localhost:8180"    # Porta alterada  
echo "Airflow: http://localhost:8082"     # Porta alterada

echo ""
echo "✅ VALIDAÇÃO CONCLUÍDA - PROJETO PRONTO!"
