import psycopg2
from fastapi import HTTPException
from contextlib import contextmanager

@contextmanager
def get_connection():
    connection = None
    try:
        connection = psycopg2.connect(
            host='localhost',
            database='verdecdb',
            user='postgres',
            password='#su1su10719202i%'
        )
        print("databasae.py:Connection successful")
        yield connection
    except psycopg2.Error as e:
        print("保存失敗:", str(e))  # エラーメッセージを詳細に出力
        raise HTTPException(status_code=500, detail=f"Database connection error: {e}")
    # finally:
    #     if connection:
    #         connection.close()