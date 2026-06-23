from fastapi import FastAPI
from database import select_operation
from connection_api import create_connection
from fastapi import HTTPException
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/refeicoes")
async def verifica_refeicoes():
    """
    Retorna uma Lista de Objetos Refeicao. Se não houver, é retornado uma Lista vazia.
    """
    client = create_connection()
    if client is None:
        raise HTTPException(status_code=500, detail="Erro na Conexão com o Banco de Dados.")
    refeicoes = select_operation(client,"refeicao")
    return JSONResponse(content=refeicoes, status_code=200)
@app.get("/refeicoes/{id}")
async def verifica_refeicao(id:str):
    """
    Busca e retorna um Objeto Refeicao pelo seu ID. Se não encontrado,
    retorna 404.
    """
    client = create_connection()
    if client is None:
        raise HTTPException(status_code=500, detail="Falha na Conexão com o Banco de Dados")
    try:
        refeicao = select_operation(client,"refeicao",id)
    except Exception as e:
        if e.code=="22P02":
            raise HTTPException(status_code=400,detail="ID deve estar no formato UUID. ID fornecido é Inválido")
    if not refeicao:
        raise HTTPException(status_code=404,detail="Refeição não encontrada.")
    return JSONResponse(content=refeicao,status_code=200)