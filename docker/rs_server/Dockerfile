FROM i386/python:3.11-alpine

# Instalar dependências para compilar pacotes e configurar ambiente 32 bits
RUN apk add --no-cache gcc musl-dev libffi-dev openssl-dev libc6-compat

# Definir o diretório de trabalho
WORKDIR /work

# Atualizar pip para a última versão
RUN pip install --upgrade pip

# Copiar e instalar as dependências do projeto
COPY requiriments.txt .
RUN pip install -r requiriments.txt
