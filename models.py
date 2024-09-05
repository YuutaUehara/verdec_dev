import psycopg2
from database import get_connection

def create_tables():
    try:
        # `get_connection()` を使って接続を取得
        connection = next(get_connection())  
        with connection.cursor() as cursor:
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    id SERIAL PRIMARY KEY,
                    username VARCHAR(50) UNIQUE NOT NULL,
                    email VARCHAR(100) UNIQUE NOT NULL,
                    password_hash TEXT NOT NULL,
                    password_salt TEXT,
                    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
                    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
                    last_login_at TIMESTAMP WITH TIME ZONE
                )
            """)
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS items (
                    id SERIAL PRIMARY KEY,
                    title VARCHAR NOT NULL,
                    description TEXT,
                    owner_id INTEGER REFERENCES users(id)
                )
            """)
            connection.commit()
    except psycopg2.Error as e:
        print(f"Error: {e}")
    # finally:
    #     if connection:
    #         connection.close()

# テーブル作成関数を呼び出す
create_tables()


# import psycopg2
# from database import get_connection

# def create_tables():
#     try:
#         # `get_connection()` を使って接続を取得
#         connection = next(get_connection())  
#         with connection.cursor() as cursor:
#             cursor.execute("""
#                 CREATE TABLE IF NOT EXISTS account_info (
#                     id SERIAL PRIMARY KEY,
#                     username VARCHAR NOT NULL,
#                     email VARCHAR UNIQUE NOT NULL,
#                     password VARCHAR NOT NULL,
#                     is_active BOOLEAN DEFAULT TRUE
#                 )
#             """)
#             cursor.execute("""
#                 CREATE TABLE IF NOT EXISTS items (
#                     id SERIAL PRIMARY KEY,
#                     title VARCHAR NOT NULL,
#                     description VARCHAR,
#                     owner_id INTEGER REFERENCES account_info(id)
#                 )
#             """)
#             connection.commit()
#     except psycopg2.Error as e:
#         print(f"Error: {e}")
#     finally:
#         # 接続を閉じる
#         if connection:
#             connection.close()

# # テーブル作成関数を呼び出す
# create_tables()
