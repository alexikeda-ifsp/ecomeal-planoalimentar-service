from psycopg2.extras import RealDictCursor


def select_operation(connection, table, id=None):

    if table is None:
        raise Exception("Tabela não encontrada.")


    cursor = connection.cursor(
        cursor_factory=RealDictCursor
    )


    if id:

        cursor.execute(
            f"""
            SELECT *
            FROM {table}
            WHERE id = %s
            """,
            (id,)
        )

        result = cursor.fetchone()


    else:

        cursor.execute(
            f"""
            SELECT *
            FROM {table}
            """
        )

        result = cursor.fetchall()


    cursor.close()
    connection.close()

    return result