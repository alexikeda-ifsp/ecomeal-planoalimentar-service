import datetime
import decimal
import uuid

from psycopg2.extras import RealDictCursor


def convert_value(value):

    if isinstance(value, (datetime.date, datetime.datetime)):
        return value.isoformat()

    if isinstance(value, decimal.Decimal):
        return float(value)

    if isinstance(value, uuid.UUID):
        return str(value)

    return value



def select_operation(connection, table, id=None):

    cursor = connection.cursor(cursor_factory=RealDictCursor)

    try:

        if id:

            cursor.execute(
                f"SELECT * FROM {table} WHERE id = %s",
                (id,)
            )

        else:

            cursor.execute(
                f"SELECT * FROM {table}"
            )


        rows = cursor.fetchall()


        result = []

        for row in rows:

            item = {}

            for key, value in row.items():

                item[key] = convert_value(value)


            result.append(item)


        return result


    finally:

        cursor.close()