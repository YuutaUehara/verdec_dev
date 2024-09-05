# import hashlib
# import psycopg2
# from .schemas import UserCreate, ItemCreate, infoCreate
# from .database import get_connection

# def get_user_by_email(connection, email: str):
#     try:
#         with connection.cursor() as cursor:
#             cursor.execute("SELECT * FROM account_info WHERE email = %s", (email,))
#             return cursor.fetchone()
#     except psycopg2.Error as e:
#         print(f"Error: {e}")
#     finally:
#         connection.close()

# def create_acc_info(connection, user: infoCreate):
#     try:
#         with connection.cursor() as cursor:
#             hashed_password = hashlib.sha256(user.password.encode()).hexdigest()
#             cursor.execute("""
#                 INSERT INTO account_info (username, email, password)
#                 VALUES (%s, %s, %s) RETURNING id
#             """, (user.username, user.email, hashed_password))
#             user_id = cursor.fetchone()[0]
#             connection.commit()
#             return user_id
#     except psycopg2.Error as e:
#         print(f"Error: {e}")
#     finally:
#         connection.close()

# def get_items(connection, skip: int = 0, limit: int = 100):
#     try:
#         with connection.cursor() as cursor:
#             cursor.execute("SELECT * FROM items OFFSET %s LIMIT %s", (skip, limit))
#             return cursor.fetchall()
#     except psycopg2.Error as e:
#         print(f"Error: {e}")
#     finally:
#         connection.close()

import hashlib
import os
import psycopg2
from .schemas import UserCreate

def get_user_by_email(connection, email: str):
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
            return cursor.fetchone()
    except psycopg2.Error as e:
        print(f"Error: {e}")
    # finally:
    #     connection.close()

def create_user(connection, user: UserCreate):
    try:
        with connection.cursor() as cursor:
            password_salt = os.urandom(16).hex()  # ソルトの生成
            hashed_password = hashlib.sha256((user.password + password_salt).encode()).hexdigest()
            cursor.execute("""
                INSERT INTO users (username, email, password_hash, password_salt)
                VALUES (%s, %s, %s, %s) RETURNING id
            """, (user.username, user.email, hashed_password, password_salt))
            user_id = cursor.fetchone()[0]
            connection.commit()
            return user_id
    except psycopg2.Error as e:
        print(f"Error(失敗): {e}")
    finally:
        connection.close()

def get_items(connection, skip: int = 0, limit: int = 100):
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM items OFFSET %s LIMIT %s", (skip, limit))
            return cursor.fetchall()
    except psycopg2.Error as e:
        print(f"Error: {e}")
    finally:
        connection.close()
