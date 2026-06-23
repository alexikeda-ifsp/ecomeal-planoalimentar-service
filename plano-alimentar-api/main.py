from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse

from database import select_operation
from connection_api import create_connection


app = FastAPI()


@app.get("/planos/")
async def busca_planos():

    connection = create_connection()

    if connection is None:
        raise HTTPException(
            status_code=500,
            detail="Erro na conexão com banco"
        )


    planos = select_operation(
        connection,
        "plano_alimentar"
    )


    return JSONResponse(
        content=planos,
        status_code=200
    )



@app.get("/planos/{id}")
async def busca_plano(id: str):

    connection = create_connection()

    if connection is None:
        raise HTTPException(
            status_code=500,
            detail="Erro na conexão com banco"
        )


    plano = select_operation(
        connection,
        "plano_alimentar",
        id
    )


    if not plano:
        raise HTTPException(
            status_code=404,
            detail="Plano alimentar não encontrado"
        )


    return JSONResponse(
        content=plano,
        status_code=200
    )