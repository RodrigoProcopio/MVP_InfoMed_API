# Use uma imagem base do Python para o Flask
FROM python:3.9-slim

# Defina o diretório de trabalho no container
WORKDIR /app

# Copie os arquivos necessários para o diretório de trabalho
COPY . .

# Instale as dependências do Python
RUN pip install --no-cache-dir -r requirements.txt

# Exponha a porta 5000 para o Flask
EXPOSE 5000

# Comando para iniciar o Flask
CMD ["flask", "run", "--host", "0.0.0.0", "--port", "5000"]
