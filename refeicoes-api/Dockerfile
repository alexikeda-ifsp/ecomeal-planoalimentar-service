FROM python:3.13.6

WORKDIR /app

# Copia os requisitos e instala
COPY ./requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY ecomeal-planoalimentar-service/refeicoes-api/ .

# Expõe a porta que o FastAPI vai usar
EXPOSE 8003

# Comando para rodar a API
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8003"]
