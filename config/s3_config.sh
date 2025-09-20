#!/bin/bash
# Configurar acesso S3 para Spark

echo "Configurando acesso ao MinIO (S3)..."

# Configurar core-site.xml para Spark
cat > /opt/spark/conf/core-site.xml << 'XML'
<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>
<configuration>
  <property>
    <name>fs.s3a.endpoint</name>
    <value>http://minio:9000</value>
  </property>
  <property>
    <name>fs.s3a.access.key</name>
    <value>admin</value>
  </property>
  <property>
    <name>fs.s3a.secret.key</name>
    <value>password123</value>
  </property>
  <property>
    <name>fs.s3a.path.style.access</name>
    <value>true</value>
  </property>
  <property>
    <name>fs.s3a.connection.ssl.enabled</name>
    <value>false</value>
  </property>
</configuration>
XML

echo "Configuração S3 concluída!"
