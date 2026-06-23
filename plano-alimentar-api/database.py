def select_operation(client,table,id_paciente=None):
    """
    Faz a operação de SELECT no Banco de Dados, passando uma query e retornando um registro Lista
    de Dicionários.
    """
    if table is None:
        raise Exception("Tabela não encontrada.")
    if id_paciente is not None:
        paciente = client.table(table).select("*").eq("id", id_paciente).execute()
        return paciente.data
    pacientes = client.table(table).select("*").execute()
    return pacientes.data

    


