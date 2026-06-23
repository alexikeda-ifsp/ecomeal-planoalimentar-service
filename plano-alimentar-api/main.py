from fastapi import FastAPI
from database import select_operation
from connection_api import create_connection
from fastapi import HTTPException
from fastapi.responses import JSONResponse
app = FastAPI()

@app.get("/planos")
async def verifica_planos():
    """
    Verifica os Planos Alimentares existentes. Retorna uma
    Lista de Objetos Plano Alimentar
    """
    client = create_connection()
    if client is None:
        raise HTTPException(
            status_code=500,
            detail="Erro na Conexão com o Banco de Dados."
        )
    planos_alimentar = select_operation(client,"plano_alimentar")
    return JSONResponse(content=planos_alimentar, status_code=200)

@app.get("/planos/{id}")
async def verifica_plano(id):
    """
    Verifica um plano específico pelo seu ID, retornando um objeto
    Plano Alimentar. Se não existir, retornar code 404.
    """
    client = create_connection()
    if client is None:
        raise HTTPException(
            status_code=500,
            detail="Erro na Conexão com o Banco de Dados."
        )
    try:
        plano_alimentar = select_operation(client, "plano_alimentar",id)
    except Exception as e:
        if e.code=="22P02":
            raise HTTPException(status_code=400, detail="ID deve estar no formato UUID. ID fornecido é Inválido")
    if not plano_alimentar:
        raise HTTPException(status_code=404,detail="Plano Alimentar não encontrado.") 
    return JSONResponse(content=plano_alimentar,status_code=200)

