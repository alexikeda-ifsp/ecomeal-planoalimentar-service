from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse

from database import select_operation
from connection_api import create_connection


app = FastAPI()



@app.get("/refeicoes/")
async def busca_refeicoes():

    connection = create_connection()


    if connection is None:
        raise HTTPException(
            status_code=500,
            detail="Erro na conexão com banco"
        )


    refeicoes = select_operation(
        connection,
        "refeicao"
    )


    return JSONResponse(
        content=refeicoes,
        status_code=200
    )



@app.get("/refeicoes/{id}")
async def busca_refeicao(id:str):

    connection = create_connection()


    if connection is None:
        raise HTTPException(
            status_code=500,
            detail="Erro na conexão com banco"
        )


    refeicao = select_operation(
        connection,
        "refeicao",
        id
    )


    if not refeicao:

        raise HTTPException(
            status_code=404,
            detail="Refeição não encontrada"
        )


    return JSONResponse(
        content=refeicao,
        status_code=200
    )